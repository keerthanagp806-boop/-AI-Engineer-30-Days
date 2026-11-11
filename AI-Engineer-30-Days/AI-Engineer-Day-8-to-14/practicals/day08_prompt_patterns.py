"""Day 8: Prompt engineering patterns.
This script prints prompt templates; it does not call an AI API.
"""

def build_zero_shot_prompt(topic):
    return f"Explain {topic} in simple English and give one example."

def build_few_shot_prompt(review):
    return f"""
Classify each review as Positive or Negative.

Examples:
Review: "This app is wonderful." -> Positive
Review: "The service was terrible." -> Negative

Now classify:
Review: "{review}"
Answer with only Positive or Negative.
""".strip()

def build_role_prompt(question):
    return f"""
Role: You are a friendly Python tutor for beginners.
Task: Answer the question below.
Rules: Use simple English and give one short code example.
Question: {question}
""".strip()

if __name__ == "__main__":
    print("ZERO-SHOT PROMPT")
    print(build_zero_shot_prompt("Python loops"))
    print("\nFEW-SHOT PROMPT")
    print(build_few_shot_prompt("I love the new design."))
    print("\nROLE-BASED PROMPT")
    print(build_role_prompt("What is a variable?"))
