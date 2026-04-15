# ============================================================
# prompts/extraction_prompt.py
# Prompt Template for Skill Extraction (Step 1)
# ============================================================
# Extracts skills, experience, tools, and education from a resume.
# Uses few-shot prompting for reliable structured JSON output.
# Key rule: Do NOT assume skills not present in the resume.
# ============================================================

from langchain_core.prompts import PromptTemplate


def get_extraction_prompt() -> PromptTemplate:
    """
    Returns a PromptTemplate for extracting structured information
    from a candidate's resume.
    
    Output schema:
        - skills: list of technical skills mentioned
        - experience_years: total years of professional experience
        - tools: list of tools/platforms mentioned
        - education: list of degrees with fields
        - certifications: list of certifications
    """

    template = """You are an expert resume parser for a recruitment AI system.

TASK: Extract structured information from the following resume.

STRICT RULES:
1. Extract ONLY skills, tools, and technologies explicitly mentioned in the resume.
2. Do NOT assume or infer skills that are not clearly stated.
3. Do NOT hallucinate or add skills based on job titles alone.
4. Calculate experience_years from the work history dates provided.
5. Return valid JSON only — no markdown, no explanation, no extra text.

EXAMPLE OUTPUT:
{{
    "skills": ["Python", "Machine Learning", "SQL"],
    "experience_years": 4,
    "tools": ["TensorFlow", "AWS", "Docker"],
    "education": ["M.Tech in Computer Science - IIT Delhi"],
    "certifications": ["AWS Certified ML - Specialty"]
}}

RESUME:
{resume_text}

OUTPUT (JSON only):"""

    return PromptTemplate(
        input_variables=["resume_text"],
        template=template
    )
