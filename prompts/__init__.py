# prompts/__init__.py
"""Prompts module containing all PromptTemplates for the screening pipeline."""

from prompts.extraction_prompt import get_extraction_prompt
from prompts.matching_prompt import get_matching_prompt
from prompts.scoring_prompt import get_scoring_prompt
from prompts.explanation_prompt import get_explanation_prompt
