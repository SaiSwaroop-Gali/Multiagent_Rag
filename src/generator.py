import os

import google.generativeai as genai


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def generate_answer(query, contexts):

    combined_context = "\n\n".join(contexts)

    prompt = f"""
You are a helpful AI assistant.

Answer the question ONLY using the provided context.

If the answer cannot be found in the context, say:
"I could not find the answer in the provided documents."

Context:
{combined_context}

Question:
{query}

Answer:
"""

    response = model.generate_content(
        prompt
    )

    return response.text