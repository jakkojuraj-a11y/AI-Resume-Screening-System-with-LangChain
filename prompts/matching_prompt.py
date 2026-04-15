# ============================================================
# prompts/matching_prompt.py
# Prompt Template for Resume-JD Matching (Step 2)
# ============================================================
# Compares extracted resume data against job description
# requirements. Identifies matched, missing, and partial matches.
# ============================================================

from langchain_core.prompts import PromptTemplate


def get_matching_prompt() -> PromptTemplate:
    """
    Returns a PromptTemplate for matching extracted resume skills
    against job description requirements.
    
    Output schema:
        - matched_skills: skills present in both resume and JD
        - missing_skills: skills required by JD but absent from resume
        - partial_matches: skills with some overlap
        - experience_match: whether experience meets the requirement
        - education_match: whether education meets the requirement
    """

    template = """You are an expert recruitment matching system.

TASK: Compare the candidate's extracted profile against the job description 
requirements and identify matches, gaps, and partial overlaps.

STRICT RULES:
1. Only mark a skill as "matched" if it is explicitly present in BOTH 
   the extracted resume data AND the job description.
2. Mark skills as "missing" if they are required in the JD but NOT in 
   the resume data.
3. Use "partial_matches" for skills that are related but not exact 
   (e.g., "basic Python" vs "advanced Python proficiency").
4. For experience_match, compare the candidate's years against the 
   JD's minimum requirement.
5. Return valid JSON only — no markdown, no explanation, no extra text.

EXTRACTED RESUME DATA:
{extracted_data}

JOB DESCRIPTION:
{job_description}

OUTPUT (JSON only):
{{
    "matched_skills": ["list of matched skills"],
    "missing_skills": ["list of missing skills"],
    "partial_matches": ["list of partial matches with notes"],
    "experience_match": {{
        "required_years": <number>,
        "candidate_years": <number>,
        "meets_requirement": <true/false>
    }},
    "education_match": {{
        "required": "description",
        "candidate_has": "description",
        "meets_requirement": <true/false>
    }}
}}"""

    return PromptTemplate(
        input_variables=["extracted_data", "job_description"],
        template=template
    )
