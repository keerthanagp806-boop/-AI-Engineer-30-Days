# Beginner reference program: AI providers and model families
# This prints a study reference. It does NOT call live AI APIs.

providers = [
    {
        "provider": "OpenAI",
        "model_family": "GPT",
        "common_uses": "Chatbots, coding, text generation, reasoning"
    },
    {
        "provider": "Anthropic",
        "model_family": "Claude",
        "common_uses": "Document analysis, coding, writing, reasoning"
    },
    {
        "provider": "Google",
        "model_family": "Gemini",
        "common_uses": "Text and multimodal applications"
    },
    {
        "provider": "Mistral AI",
        "model_family": "Mistral",
        "common_uses": "General-purpose models and open-weight deployment options"
    },
    {
        "provider": "Cohere",
        "model_family": "Command, Embed, Rerank",
        "common_uses": "Enterprise language tasks, embeddings and search"
    }
]


def show_providers():
    print("AI PROVIDERS AND MODEL FAMILIES")
    print("-" * 78)

    for item in providers:
        print("Provider:", item["provider"])
        print("Model family:", item["model_family"])
        print("Common uses:", item["common_uses"])
        print("-" * 78)


def compare_selection():
    print("\nWhich provider would you investigate for your project?")
    for number, item in enumerate(providers, start=1):
        print(f"{number}. {item['provider']}")

    choice = input("Enter a number from 1 to 5: ")

    if choice.isdigit() and 1 <= int(choice) <= len(providers):
        selected = providers[int(choice) - 1]
        print("\nYou selected:", selected["provider"])
        print("Model family:", selected["model_family"])
        print("Remember to evaluate real models for accuracy, speed, cost, context, capabilities and privacy.")
    else:
        print("Please run the program again and enter a number from 1 to 5.")


if __name__ == "__main__":
    show_providers()
    compare_selection()
