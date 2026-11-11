# Day 10 – Implementing Basic AI Safety

## 📚 Topics Learned
This day focuses on adding safety checks around an AI application.

## 🧠 Key Concepts

- **Moderation:** Checking text or other content for categories of harmful or disallowed material. A moderation service can help classify content; it does not replace application security.
- **End-user ID:** A pseudonymous identifier used to distinguish users for monitoring, rate limits, or abuse investigation. Avoid sending unnecessary personal information.
- **Adversarial testing:** Deliberately testing with unusual, misleading, or malicious inputs to find weaknesses.
- **Robust prompt:** A prompt with clear role, task, boundaries, and expected output.
- **Input constraints:** Rules applied before processing user input, such as length limits and accepted file types.
- **Output constraints:** Rules applied to generated responses, such as schema validation, length limits, and safety checks.
- **Safety best practices:** Validate inputs, protect secrets, apply access controls, moderate when appropriate, check outputs, log carefully, and test regularly.

## 🧠 Example
A college chatbot can limit question length, verify that a student is authorized to see a record, check content for policy violations, and validate the response before showing it.

## 💻 Practical Work
Run `practicals/day10_safety_filter.py`. It demonstrates basic input validation and a simple output check.

## Important
A keyword filter can miss harmful content and can also flag harmless text. A robust system uses layered safeguards. Never treat this demo as a replacement for a real moderation system or authorization.

## 🎤 Interview Preparation
1. What does a moderation system do?
2. Why can an end-user ID be useful?
3. What is adversarial testing?
4. Explain input and output constraints.

## 📌 Status
Educational safety-filter prototype included.
