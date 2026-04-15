# ============================================================
# main.py – AI Resume Screening System Entry Point
# ============================================================
# This is the main entry point for the resume screening pipeline.
# It loads environment variables, initializes the pipeline,
# and runs screening for all 3 sample candidates.
#
# Usage:
#   python main.py
#
# Requirements:
#   - .env file with GOOGLE_API_KEY and LANGCHAIN_API_KEY
#   - pip install -r requirements.txt
# ============================================================

import os
import sys
import json
from dotenv import load_dotenv

# ── Fix Windows console encoding for emoji/unicode support ───
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# ── Load Environment Variables ────────────────────────────────
# Must be done BEFORE importing LangChain components
load_dotenv()

# Verify required environment variables
def verify_env():
    """Check that all required environment variables are set."""
    required = {
        "GOOGLE_API_KEY": "Google Gemini API key (get from https://aistudio.google.com/apikey)",
        "LANGCHAIN_API_KEY": "LangSmith API key (get from https://smith.langchain.com)"
    }
    
    missing = []
    for key, description in required.items():
        value = os.getenv(key)
        if not value or value.startswith("your_"):
            missing.append(f"  ❌ {key}: {description}")
    
    if missing:
        print("\n⚠️  Missing or invalid environment variables:")
        print("\n".join(missing))
        print("\n📝 Copy .env.example to .env and fill in your keys:")
        print("   cp .env.example .env")
        sys.exit(1)
    
    # Ensure LangSmith tracing is enabled (mandatory for assignment)
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ.setdefault("LANGCHAIN_PROJECT", "ai-resume-screening")
    
    print("✅ Environment variables verified")
    print(f"   📡 LangSmith Project: {os.getenv('LANGCHAIN_PROJECT')}")
    print(f"   🔍 Tracing: ENABLED")


def print_results(result: dict):
    """Pretty-print the screening results for a candidate."""
    print(f"\n{'━'*60}")
    print(f"  📄 RESULTS: {result['candidate_name']}")
    print(f"  🏷️  Label: {result['candidate_label']}")
    print(f"{'━'*60}")
    
    # Score Summary
    scoring = result.get("scoring", {})
    print(f"\n  🎯 Overall Score: {scoring.get('overall_score', 'N/A')}/100")
    print(f"  📊 Category: {scoring.get('category', 'N/A')}")
    
    # Score Breakdown
    breakdown = scoring.get("breakdown", {})
    if breakdown:
        print(f"\n  📈 Score Breakdown:")
        for dimension, score in breakdown.items():
            bar = "█" * (score // 5) + "░" * (20 - score // 5)
            print(f"     {dimension:<25} {bar} {score}/100")
    
    # Matched & Missing Skills
    matching = result.get("matching", {})
    matched = matching.get("matched_skills", [])
    missing = matching.get("missing_skills", [])
    
    if matched:
        print(f"\n  ✅ Matched Skills ({len(matched)}):")
        for skill in matched:
            print(f"     • {skill}")
    
    if missing:
        print(f"\n  ❌ Missing Skills ({len(missing)}):")
        for skill in missing:
            print(f"     • {skill}")
    
    # Explanation
    explanation = result.get("explanation", {})
    
    summary = explanation.get("summary", "")
    if summary:
        print(f"\n  📝 Summary:")
        # Word-wrap summary at 55 chars
        words = summary.split()
        line = "     "
        for word in words:
            if len(line) + len(word) + 1 > 60:
                print(line)
                line = "     " + word
            else:
                line += " " + word if line.strip() else "     " + word
        if line.strip():
            print(line)
    
    strengths = explanation.get("strengths", [])
    if strengths:
        print(f"\n  💪 Strengths:")
        for s in strengths:
            print(f"     ✦ {s}")
    
    weaknesses = explanation.get("weaknesses", [])
    if weaknesses:
        print(f"\n  ⚠️  Weaknesses:")
        for w in weaknesses:
            print(f"     ✧ {w}")
    
    recommendation = explanation.get("recommendation", {})
    if recommendation:
        print(f"\n  🏁 Recommendation: {recommendation.get('decision', 'N/A')}")
        print(f"     {recommendation.get('reasoning', '')}")
    
    suggestions = explanation.get("improvement_suggestions", [])
    if suggestions:
        print(f"\n  💡 Improvement Suggestions:")
        for s in suggestions:
            print(f"     → {s}")
    
    print(f"\n{'━'*60}\n")


def main():
    """Main function – runs the full screening pipeline for all candidates."""
    
    print("\n" + "="*60)
    print("  🤖 AI Resume Screening System")
    print("  Powered by LangChain + LangSmith")
    print("="*60 + "\n")
    
    # Step 0: Verify environment
    verify_env()
    
    # Import data and pipeline (after env is loaded)
    from data.resumes import RESUMES
    from data.job_description import JOB_DESCRIPTION
    from chains.pipeline import ResumeScreeningPipeline
    
    # Initialize the pipeline
    print("\n🔧 Initializing screening pipeline...")
    pipeline = ResumeScreeningPipeline(
        model_name="gemini-1.5-flash",
        temperature=0  # Deterministic output for reproducibility
    )
    print("✅ Pipeline ready\n")
    
    # Run screening for all 3 candidates
    all_results = []
    
    for candidate_key in ["strong", "average", "weak"]:
        candidate = RESUMES[candidate_key]
        
        result = pipeline.screen_candidate(
            resume_text=candidate["text"],
            job_description=JOB_DESCRIPTION,
            candidate_name=candidate["name"],
            candidate_label=f"{candidate_key}_candidate"
        )
        
        all_results.append(result)
        print_results(result)
    
    # ── Final Summary Table ───────────────────────────────────
    print("\n" + "="*60)
    print("  📊 FINAL COMPARISON SUMMARY")
    print("="*60)
    print(f"\n  {'Candidate':<20} {'Score':<10} {'Category':<12} {'Recommendation'}")
    print(f"  {'─'*18}   {'─'*8}   {'─'*10}   {'─'*25}")
    
    for r in all_results:
        name = r["candidate_name"]
        score = r["scoring"].get("overall_score", "N/A")
        category = r["scoring"].get("category", "N/A")
        decision = r["explanation"].get("recommendation", {}).get("decision", "N/A")
        print(f"  {name:<20} {score:<10} {category:<12} {decision}")
    
    print(f"\n{'='*60}")
    print("  ✅ Screening complete! Check LangSmith for detailed traces.")
    print(f"  🔗 https://smith.langchain.com/project/{os.getenv('LANGCHAIN_PROJECT')}")
    print(f"{'='*60}\n")
    
    # Save results to JSON for reference
    output_path = os.path.join(os.path.dirname(__file__), "screening_results.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"📁 Results saved to: {output_path}")


if __name__ == "__main__":
    main()
