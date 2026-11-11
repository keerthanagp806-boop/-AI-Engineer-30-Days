"""Day 13: A simple local chatbot using Ollama.

Setup:
1. Install Ollama: https://ollama.com/download
2. Run: ollama pull llama3.2:1b
3. Install client: python -m pip install ollama
4. Make sure the Ollama app/service is running.
"""

import ollama

MODEL = "llama3.2:1b"

def main():
    print("Local AI Study Chatbot")
    print("Ask a question. Type 'exit' to stop.\n")

    # Keep recent messages so the model can use conversation context.
    messages = [
        {
            "role": "system",
            "content": "You are a helpful study assistant. Explain concepts in simple English and give one example."
        }
    ]

    while True:
        user_text = input("You: ").strip()
        if user_text.lower() == "exit":
            print("Goodbye!")
            break
        if not user_text:
            continue

        messages.append({"role": "user", "content": user_text})

        try:
            response = ollama.chat(model=MODEL, messages=messages)
            assistant_text = response.message.content
            print("\nAI:", assistant_text, "\n")
            messages.append({"role": "assistant", "content": assistant_text})

            # Keep the system instruction and the latest 10 messages.
            messages = [messages[0]] + messages[-10:]
        except Exception as error:
            print("Could not reach Ollama. Check that Ollama is running and")
            print("that the model is downloaded.")
            print("Technical detail:", error)
            break

if __name__ == "__main__":
    main()
