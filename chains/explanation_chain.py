# ============================================================
# chains/explanation_chain.py
# LangChain LCEL Chain for Score Explanation (Step 4)
# ============================================================
# Generates human-readable reasoning for the screening result.
# ============================================================

from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.explanation_prompt import get_explanation_prompt


def get_explanation_chain(llm: ChatGoogleGenerativeAI = None):
    """
    Builds and returns the explanation chain using LCEL.
    
    Chain: explanation_prompt | llm | JsonOutputParser
    
    Args:
        llm: Optional ChatGoogleGenerativeAI instance. Creates default if None.
    
    Returns:
        A runnable LCEL chain that accepts candidate profile data
        and returns a dict with summary, strengths, weaknesses,
        recommendation, and improvement suggestions.
    """
    if llm is None:
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    
    prompt = get_explanation_prompt()
    parser = JsonOutputParser()
    
    # Build LCEL chain: prompt → LLM → parser
    chain = prompt | llm | parser
    
    return chain
