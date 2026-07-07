from langchain_core.output_parsers import StrOutputParser

from .llm import model
from .prompts import summary_prompt

# LCEL : langchain expression language which allows us to chain together prompts and models in a more readable way

summary_chain = summary_prompt | model | StrOutputParser()