# ============================================================
# chains/extraction_chain.py
# LangChain LCEL Chain for Skill Extraction (Step 1)
# ============================================================
# Uses PromptTemplate | LLM | JsonOutputParser pattern.
# ============================================================

from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.extraction_prompt import get_extraction_prompt


def get_extraction_chain(llm: ChatGoogleGenerativeAI = None):
    """
    Builds and returns the skill extraction chain using LCEL.
    
    Chain: extraction_prompt | llm | JsonOutputParser
    
    Args:
        llm: Optional ChatGoogleGenerativeAI instance. Creates default if None.
    
    Returns:
        A runnable LCEL chain that accepts {"resume_text": str}
        and returns a dict with skills, experience, tools, etc.
    """
    # Use provided LLM or create a default one
    if llm is None:
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    
    # Get the prompt template
    prompt = get_extraction_prompt()
    
    # JSON output parser for structured output
    parser = JsonOutputParser()
    
    # Build LCEL chain: prompt → LLM → parser
    chain = prompt | llm | parser
    
    return chain
