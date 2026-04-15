# ============================================================
# prompts/scoring_prompt.py
# Prompt Template for Candidate Scoring (Step 3)
# ============================================================
# Assigns a 0–100 fit score based on matching results.
# Uses weighted criteria for fair, reproducible scoring.
# ============================================================

from langchain_core.prompts import PromptTemplate


def get_scoring_prompt() -> PromptTemplate:
    """
    Returns a PromptTemplate for scoring a candidate based on
    their match results against the job description.
    
    Output schema:
        - overall_score: integer 0–100
        - category: "Strong" / "Average" / "Weak"
        - breakdown: dict with sub-scores per dimension
    """

    template = """You are an expert recruitment scoring system.

TASK: Based on the matching results below, assign a fit score (0–100) 
to the candidate for the given job role.

SCORING CRITERIA (use these weights):
- Technical Skills Match: 35% (matched vs required skills)
- Experience Level: 25% (years + relevance of experience)
- Education Fit: 15% (degree level + field relevance)
- Tools & Platforms: 15% (cloud, MLOps, frameworks)
- Certifications & Extras: 10% (relevant certs, publications)

SCORING GUIDELINES:
- 80–100: Strong Candidate – Meets or exceeds most/all requirements
- 50–79: Average Candidate – Meets some requirements, has notable gaps
- 0–49: Weak Candidate – Does not meet most requirements

STRICT RULES:
1. Score ONLY based on the matching data provided. Do NOT assume 
   additional context.
2. The score must reflect the actual match percentage, not general 
   impressions.
3. Return valid JSON only — no markdown, no explanation, no extra text.

MATCHING RESULTS:
{matching_results}

OUTPUT (JSON only):
{{
    "overall_score": <0-100>,
    "category": "<Strong/Average/Weak>",
    "breakdown": {{
        "technical_skills": <0-100>,
        "experience": <0-100>,
        "education": <0-100>,
        "tools_platforms": <0-100>,
        "certifications_extras": <0-100>
    }}
}}"""

    return PromptTemplate(
        input_variables=["matching_results"],
        template=template
    )
