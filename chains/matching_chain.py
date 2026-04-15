# ============================================================
# chains/matching_chain.py
# LangChain LCEL Chain for Resume-JD Matching (Step 2)
# ============================================================
# Compares extracted resume data against job requirements.
# ============================================================

from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.matching_prompt import get_matching_prompt


def get_matching_chain(llm: ChatGoogleGenerativeAI = None):
    """
    Builds and returns the matching chain using LCEL.
    
    Chain: matching_prompt | llm | JsonOutputParser
    
    Args:
        llm: Optional ChatGoogleGenerativeAI instance. Creates default if None.
    
    Returns:
        A runnable LCEL chain that accepts 
        {"extracted_data": str, "job_description": str}
        and returns a dict with matched/missing/partial skills.
    """
    if llm is None:
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    
    prompt = get_matching_prompt()
    parser = JsonOutputParser()
    
    # Build LCEL chain: prompt → LLM → parser
    chain = prompt | llm | parser
    
    return chain
