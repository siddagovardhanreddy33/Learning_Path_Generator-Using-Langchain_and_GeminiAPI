import os
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel

from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import roadmap_prompt


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    try:
        import streamlit as st
        api_key = st.secrets["GOOGLE_API_KEY"]
    except Exception:
        raise ValueError("GOOGLE_API_KEY not found.")


class LearningPath(BaseModel):
    learning_stages: List[str]
    key_topics: List[str]
    learning_goal_summary: str


llm = ChatGoogleGenerativeAI( model="gemini-2.5-flash",
                             google_api_key=api_key,
                             temperature=0.3,
                             )

structured_llm = llm.with_structured_output(LearningPath)


def generate_learning_path(skill: str):
    chain = roadmap_prompt | structured_llm

    result = chain.invoke({"skill": skill})

    return result.model_dump()