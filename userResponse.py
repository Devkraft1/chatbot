import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

models = [
    "qwen/qwen3.8-27b",
    "openai/gpt-oss-20b",
    "openai/gpt-oss-120b"
]
def generateUserResponse(prompt: str):
    for model in models:
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=model
            )
            return chat_completion.choices[0].message.content

        except Exception as e:
            print(f"Model {model} failed: {e}")
            continue

    return "Chatbot nie działa, Spróbuj ponownie później."