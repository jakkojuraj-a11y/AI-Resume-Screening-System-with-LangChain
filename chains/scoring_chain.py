# ============================================================
# chains/scoring_chain.py
# LangChain LCEL Chain for Candidate Scoring (Step 3)
# ============================================================
# Assigns a 0–100 score based on matching results.
# ============================================================

from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.scoring_prompt import get_scoring_prompt


def get_scoring_chain(llm: ChatGoogleGenerativeAI = None):
    """
    Builds and returns the scoring chain using LCEL.
    
    Chain: scoring_prompt | llm | JsonOutputParser
    
    Args:
        llm: Optional ChatGoogleGenerativeAI instance. Creates default if None.
    
    Returns:
        A runnable LCEL chain that accepts {"matching_results": str}
        and returns a dict with overall_score, category, breakdown.
    """
    if llm is None:
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    
    prompt = get_scoring_prompt()
    parser = JsonOutputParser()
    
    # Build LCEL chain: prompt → LLM → parser
    chain = prompt | llm | parser
    
    return chain
