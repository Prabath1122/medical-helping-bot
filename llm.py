from openrouter import OpenRouter
from dotenv import load_dotenv
import os

load_dotenv()


def ask_llm(prompt):
    with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:
        response = client.chat.send(
            model="openai/gpt-4.1-mini",
            max_tokens=500,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        return response.choices[0].message.content