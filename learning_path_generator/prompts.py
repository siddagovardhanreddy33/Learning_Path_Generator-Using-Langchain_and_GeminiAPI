from langchain_core.prompts import PromptTemplate

roadmap_prompt = PromptTemplate(
    input_variables=["skill"],
    template="""
You are an expert learning mentor.

Generate a structured learning roadmap for:

{skill}

Requirements:

1. Create logical learning stages.
2. Order topics from beginner to advanced.
3. Keep roadmap concise.
4. Make it suitable for self-learning.
5. Return information matching the requested schema.

Focus only on the given skill.
"""
)