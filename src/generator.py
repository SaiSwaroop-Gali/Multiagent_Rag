import os
import requests


MODEL_NAME = "nvidia/nemotron-3-super-120b-a12b:free"


def generate_answer(query, contexts):

    openrouter_api_key = os.getenv(
        "OPENROUTER_API_KEY"
    )

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

    headers = {
        "Authorization": f"Bearer {openrouter_api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",

        headers=headers,

        json={
            "model": MODEL_NAME,

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    result = response.json()

    if "choices" not in result:

        return f"OpenRouter API Error: {result}"

    return result["choices"][0]["message"]["content"]