# ============================================================
# chains/pipeline.py
# Full Resume Screening Pipeline Orchestration
# ============================================================
# Chains all 4 steps together: Extract → Match → Score → Explain
# Supports LangSmith tagging for tracing and debugging.
# ============================================================

import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langsmith import traceable

from chains.extraction_chain import get_extraction_chain
from chains.matching_chain import get_matching_chain
from chains.scoring_chain import get_scoring_chain
from chains.explanation_chain import get_explanation_chain


class ResumeScreeningPipeline:
    """
    Orchestrates the full AI resume screening pipeline.
    
    Pipeline Flow:
        Resume → Extract Skills → Match with JD → Score → Explain
    
    Each step is a separate LangChain LCEL chain. Results from
    each step flow into the next. LangSmith tracing captures
    every step for debugging and monitoring.
    """
    
    def __init__(self, model_name: str = "gemini-2.0-flash", temperature: float = 0):
        """
        Initialize the pipeline with a shared LLM instance.
        
        Args:
            model_name: Google Gemini model to use (default: gemini-2.0-flash)
            temperature: LLM temperature (default: 0 for deterministic output)
        """
        # Shared LLM instance for all chains (cost-efficient, consistent)
        self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=temperature)
        
        # Initialize all 4 chains with the shared LLM
        self.extraction_chain = get_extraction_chain(self.llm)
        self.matching_chain = get_matching_chain(self.llm)
        self.scoring_chain = get_scoring_chain(self.llm)
        self.explanation_chain = get_explanation_chain(self.llm)
    
    @traceable(name="Resume Screening Pipeline", run_type="chain")
    def screen_candidate(
        self, 
        resume_text: str, 
        job_description: str, 
        candidate_name: str = "Unknown",
        candidate_label: str = ""
    ) -> dict:
        """
        Run the full screening pipeline for a single candidate.
        
        Args:
            resume_text: Raw resume text
            job_description: Job description text
            candidate_name: Name of the candidate
            candidate_label: Label tag for LangSmith (e.g., "strong_candidate")
        
        Returns:
            dict with keys: extraction, matching, scoring, explanation
        """
        print(f"\n{'='*60}")
        print(f"  Screening: {candidate_name} ({candidate_label})")
        print(f"{'='*60}")
        
        # ── Step 1: Skill Extraction ──────────────────────────────
        print("\n📋 Step 1: Extracting skills from resume...")
        extracted_data = self.extraction_chain.invoke(
            {"resume_text": resume_text},
            config={"tags": [candidate_label, "extraction"]}
        )
        print(f"   ✅ Extracted {len(extracted_data.get('skills', []))} skills, "
              f"{extracted_data.get('experience_years', 0)} years experience")
        
        # ── Step 2: Matching ──────────────────────────────────────
        print("\n🔍 Step 2: Matching against job description...")
        matching_results = self.matching_chain.invoke(
            {
                "extracted_data": json.dumps(extracted_data, indent=2),
                "job_description": job_description
            },
            config={"tags": [candidate_label, "matching"]}
        )
        matched_count = len(matching_results.get("matched_skills", []))
        missing_count = len(matching_results.get("missing_skills", []))
        print(f"   ✅ Matched: {matched_count} skills | Missing: {missing_count} skills")
        
        # ── Step 3: Scoring ───────────────────────────────────────
        print("\n📊 Step 3: Calculating fit score...")
        score_data = self.scoring_chain.invoke(
            {"matching_results": json.dumps(matching_results, indent=2)},
            config={"tags": [candidate_label, "scoring"]}
        )
        print(f"   ✅ Score: {score_data.get('overall_score', 'N/A')}/100 "
              f"({score_data.get('category', 'N/A')})")
        
        # ── Step 4: Explanation ───────────────────────────────────
        print("\n💡 Step 4: Generating explanation...")
        explanation = self.explanation_chain.invoke(
            {
                "candidate_name": candidate_name,
                "extracted_data": json.dumps(extracted_data, indent=2),
                "matching_results": json.dumps(matching_results, indent=2),
                "score_data": json.dumps(score_data, indent=2),
                "job_description": job_description
            },
            config={"tags": [candidate_label, "explanation"]}
        )
        print(f"   ✅ Recommendation: "
              f"{explanation.get('recommendation', {}).get('decision', 'N/A')}")
        
        # ── Compile Final Results ─────────────────────────────────
        result = {
            "candidate_name": candidate_name,
            "candidate_label": candidate_label,
            "extraction": extracted_data,
            "matching": matching_results,
            "scoring": score_data,
            "explanation": explanation
        }
        
        return result
