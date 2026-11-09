"""Offline AI Engineer Study Assistant. Run: py app.py"""

TOPICS = {
    "1": {
        "title": "Artificial Intelligence (AI)",
        "meaning": "AI is the broad field of building computer systems that perform tasks that normally require human-like intelligence.",
        "example": "A navigation app recommending a route based on traffic."
    },
    "2": {
        "title": "Machine Learning (ML)",
        "meaning": "ML is a part of AI in which a system learns patterns from data and uses them to make predictions or decisions.",
        "example": "An email filter learning to identify spam messages from examples."
    },
    "3": {
        "title": "Deep Learning (DL)",
        "meaning": "DL is a part of ML that uses neural networks with multiple layers to learn complex patterns.",
        "example": "A model recognising objects in photographs."
    },
    "4": {
        "title": "Large Language Models (LLMs)",
        "meaning": "An LLM is trained on large amounts of text to process and generate language. It generates text by predicting likely next tokens from context.",
        "example": "A chatbot explaining a programming concept."
    },
    "5": {
        "title": "Tokens and Tokenization",
        "meaning": "A token is a piece of text processed by a language model. It can be a word, part of a word, punctuation, or a symbol. Tokenization splits text into tokens.",
        "example": "A long or uncommon word may be split into multiple tokens."
    },
    "6": {
        "title": "Prompt Engineering",
        "meaning": "Prompt engineering means writing clear instructions and useful context so a model can produce a relevant response.",
        "example": "Ask: 'Explain recursion in Java in three simple steps with an example.'"
    },
    "7": {
        "title": "Fine-tuning",
        "meaning": "Fine-tuning means further training an already-trained model on a focused dataset so it adapts better to a particular task, domain, or style.",
        "example": "Adapting a model to classify customer support tickets using labelled examples."
    },
    "8": {
        "title": "API Integration",
        "meaning": "An API lets software applications communicate. A client sends a request, and the service returns a response. Authentication often uses a secret API key.",
        "example": "A Python chatbot sends a prompt to a model API and displays the reply."
    }
}

QUIZ = [
    {
        "question": "Which statement best describes Machine Learning?",
        "options": ["A. A type of hardware", "B. A part of AI that learns patterns from data",
                    "C. A programming language", "D. A database"],
        "answer": "B",
        "explanation": "Machine Learning learns patterns from data to make predictions or decisions."
    },
    {
        "question": "What is a token?",
        "options": ["A. Always a full sentence", "B. Only a complete English word",
                    "C. A piece of text processed by a language model", "D. An API password"],
        "answer": "C",
        "explanation": "Tokens can be words, word parts, punctuation, or symbols."
    },
    {
        "question": "What does temperature influence in text generation?",
        "options": ["A. Computer temperature", "B. Randomness and diversity",
                    "C. The API key", "D. The training dataset size"],
        "answer": "B",
        "explanation": "Lower values are generally more predictable; higher values allow more variation."
    },
    {
        "question": "What is fine-tuning?",
        "options": ["A. Renaming a model", "B. Adding a longer prompt only",
                    "C. Further training a pretrained model on focused data", "D. Counting words"],
        "answer": "C",
        "explanation": "Fine-tuning uses additional training examples to adapt a pretrained model."
    },
    {
        "question": "What is the normal API flow?",
        "options": ["A. Response then request", "B. Client sends request; service returns response",
                    "C. API deletes the client", "D. API key writes the program"],
        "answer": "B",
        "explanation": "The client sends a request to a service, which processes it and returns a response."
    }
]


def revise_concept():
    print("\n--- CONCEPT LIBRARY ---")
    for number, topic in TOPICS.items():
        print(f"{number}. {topic['title']}")

    choice = input("\nChoose a topic number (Enter to return): ").strip()
    topic = TOPICS.get(choice)
    if topic is None:
        print("Returning to menu.")
        return

    print(f"\n{topic['title']}")
    print(f"Explanation: {topic['meaning']}")
    print(f"Example: {topic['example']}")


def take_quiz():
    score = 0
    print("\n--- WEEK 1 QUIZ ---")
    for index, item in enumerate(QUIZ, start=1):
        print(f"\n{index}. {item['question']}")
        for option in item["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. Correct answer: {item['answer']}.")
        print(item["explanation"])

    print(f"\nFinal score: {score}/{len(QUIZ)}")


def prompt_lab():
    print("\n--- PROMPT WRITING LAB ---")
    print("A useful prompt can include: role + task + context + output format.")
    topic = input("What topic should be explained? ").strip()
    audience = input("Who is the explanation for? ").strip()
    output_format = input("What format do you want (e.g. 3 bullet points)? ").strip()

    if not topic or not audience or not output_format:
        print("Please fill in all three fields.")
        return

    prompt = (
        f"You are a helpful tutor. Explain {topic} for {audience}. "
        f"Use {output_format}. Include one simple example."
    )
    print("\nYour structured prompt:\n")
    print(prompt)


def estimate_tokens():
    print("\n--- ROUGH TOKEN ESTIMATOR ---")
    print("This is only a rough estimate; exact counts depend on the model tokenizer.")
    text = input("Enter text: ")
    word_count = len(text.split())
    estimate = round(len(text) / 4) if text else 0
    print(f"Word count: {word_count}")
    print(f"Very rough token estimate: about {estimate}")
    print("Use the specific model's tokenizer for an accurate count.")


def main():
    print("\n====================================")
    print("       AI ENGINEER STUDY ASSISTANT")
    print("====================================")

    while True:
        print("\n1. Revise a concept")
        print("2. Take the Week 1 quiz")
        print("3. Practise prompt engineering")
        print("4. Estimate tokens (roughly)")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            revise_concept()
        elif choice == "2":
            take_quiz()
        elif choice == "3":
            prompt_lab()
        elif choice == "4":
            estimate_tokens()
        elif choice == "5":
            print("Keep learning. Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
