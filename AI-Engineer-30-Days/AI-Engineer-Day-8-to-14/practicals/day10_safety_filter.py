"""Day 10: Basic input/output constraints demonstration.

This is a tiny educational example, not a complete moderation system.
"""

MAX_INPUT_LENGTH = 500
BLOCKED_OUTPUT_TERMS = ["confidential student record", "api_secret="]

def validate_input(text):
    if not text.strip():
        return False, "Input cannot be empty."
    if len(text) > MAX_INPUT_LENGTH:
        return False, f"Input is too long (maximum {MAX_INPUT_LENGTH} characters)."
    return True, "Input accepted."

def check_output(text):
    lowered = text.lower()
    if any(term in lowered for term in BLOCKED_OUTPUT_TERMS):
        return False, "Output blocked by the demo safety check."
    return True, "Output passed the demo check."

if __name__ == "__main__":
    user_text = input("Ask a question: ")
    allowed, message = validate_input(user_text)
    print("Input check:", message)

    if allowed:
        # A real app would call its model here.
        simulated_response = "I can help explain your study topic."
        safe, result = check_output(simulated_response)
        print("Output check:", result)
        if safe:
            print("Assistant:", simulated_response)

    print("\nReminder: production systems need proper moderation, authorization,")
    print("secret management, logging, and security testing.")
