# Day 2 — Large Language Model Basics

## What is an LLM?
A Large Language Model (LLM) is a model trained on large amounts of text so it can process and generate language.

**Example:** A chatbot that explains a programming concept.

## How does an LLM generate text?
1. The user's text is converted into tokens.
2. The model processes the tokens and their context.
3. It predicts a likely next token.
4. It repeats the process to generate a response.

## Tokens and tokenization
A token is a piece of text. It may be a whole word, part of a word, punctuation, or a symbol. Tokenization splits text into tokens.

## Training vs inference
- **Training:** The model learns patterns by adjusting its internal parameters using data.
- **Inference:** The trained model is used to generate an answer for a new input.

## Pretrained models
A pretrained model has already completed an initial training process. Developers can use it directly, guide it with prompts, or adapt it for a task when supported.

## Limitations
- **Hallucination:** It may produce confident but incorrect information.
- **Bias:** Its output may reflect biases in training data.
- **Context window:** It can process only a limited amount of input and conversation context at once.
- **Cost and latency:** API usage can involve fees and response time.

**Remember:** An LLM generates likely text; it does not guarantee every statement is true.
