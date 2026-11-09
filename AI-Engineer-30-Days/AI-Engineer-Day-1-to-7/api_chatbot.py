"""Optional OpenAI API chatbot. Requires API key and available API credits."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise SystemExit(
        "OPENAI_API_KEY was not found. Create a .env file using .env.example."
    )

client = OpenAI(api_key=api_key)
history = []

print("\nAI API Chatbot")
print("Type 'exit' to stop or 'clear' to clear the conversation.\n")

while True:
    user_text = input("You: ").strip()

    if not user_text:
        continue
    if user_text.lower() == "exit":
        print("Bot: Goodbye!")
        break
    if user_text.lower() == "clear":
        history.clear()
        print("Bot: Conversation cleared.\n")
        continue

    history.append({"role": "user", "content": user_text})

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions=(
                "You are a friendly AI study assistant. "
                "Explain concepts in simple English and include examples."
            ),
            input=history,
            max_output_tokens=400,
        )
        answer = response.output_text
        print(f"Bot: {answer}\n")
        history.append({"role": "assistant", "content": answer})

        if response.usage:
            print(
                "Token usage — "
                f"input: {response.usage.input_tokens}, "
                f"output: {response.usage.output_tokens}, "
                f"total: {response.usage.total_tokens}\n"
            )

    except Exception as error:
        history.pop()
        print(f"Request failed: {error}")
        print("Check internet, model access, API key, and API billing/credits.\n")
