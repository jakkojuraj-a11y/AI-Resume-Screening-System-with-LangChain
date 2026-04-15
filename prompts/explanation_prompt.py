# ============================================================
# prompts/explanation_prompt.py
# Prompt Template for Score Explanation (Step 4)
# ============================================================
# Generates a human-readable explanation of why the candidate
# received their score. Provides actionable feedback.
# ============================================================

from langchain_core.prompts import PromptTemplate


def get_explanation_prompt() -> PromptTemplate:
    """
    Returns a PromptTemplate for generating a detailed explanation
    of the candidate's screening results.
    
    Output schema:
        - summary: one-paragraph overall assessment
        - strengths: list of strong points
        - weaknesses: list of gaps/concerns
        - recommendation: hire / consider / reject with reasoning
        - improvement_suggestions: actionable advice for the candidate
    """

    template = """You are an expert recruitment advisor providing candidate feedback.

TASK: Based on the candidate's extracted profile, matching results, and score, 
generate a clear, detailed explanation of the screening outcome.

STRICT RULES:
1. Reference SPECIFIC skills, experiences, and qualifications in your explanation.
2. Do NOT use vague language like "the candidate seems good." Be precise.
3. Every strength must cite an actual skill or achievement from the resume.
4. Every weakness must cite a specific missing requirement from the JD.
5. The recommendation must logically follow from the score and analysis.
6. Return valid JSON only — no markdown, no extra text.

CANDIDATE NAME: {candidate_name}

EXTRACTED PROFILE:
{extracted_data}

MATCHING RESULTS:
{matching_results}

SCORE DATA:
{score_data}

JOB DESCRIPTION:
{job_description}

OUTPUT (JSON only):
{{
    "summary": "One paragraph overall assessment",
    "strengths": [
        "Specific strength 1 with evidence",
        "Specific strength 2 with evidence"
    ],
    "weaknesses": [
        "Specific gap 1 referencing JD requirement",
        "Specific gap 2 referencing JD requirement"
    ],
    "recommendation": {{
        "decision": "<Strongly Recommend / Recommend with Reservations / Do Not Recommend>",
        "reasoning": "2-3 sentence justification"
    }},
    "improvement_suggestions": [
        "Actionable suggestion 1",
        "Actionable suggestion 2"
    ]
}}"""

    return PromptTemplate(
        input_variables=[
            "candidate_name",
            "extracted_data", 
            "matching_results", 
            "score_data",
            "job_description"
        ],
        template=template
    )
