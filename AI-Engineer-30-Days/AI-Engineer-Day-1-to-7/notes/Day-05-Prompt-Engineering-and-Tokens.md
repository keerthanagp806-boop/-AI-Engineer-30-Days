# Day 5 — Prompt Engineering, Tokens and Cost

## Prompt engineering
Prompt engineering is the practice of writing clear instructions and providing useful context so a model can produce a relevant response.

## A useful prompt structure
- **Role:** Who should the model act as?
- **Task:** What should it do?
- **Context:** What background information does it need?
- **Constraints:** What should it include or avoid?
- **Output format:** How should the answer be organised?

**Example:** “Act as a beginner-friendly Java tutor. Explain arrays using a small example. Use simple English and finish with two practice questions.”

## Tokens
Tokens are pieces of text processed by a model. They can be words, parts of words, punctuation, or symbols.

## Context window
The context window is the amount of input and conversation information a model can process for a request, measured in tokens. It is not the same as the maximum response length.

## Maximum output tokens
This setting limits how many tokens the model may generate. A low limit can cause a response to stop early.

## API pricing
Many model APIs charge separately for input and output tokens. Rates vary by model and can change, so check the current provider pricing before estimating a real request.

`estimated cost = (input tokens × input rate) + (output tokens × output rate)`

Use the provider's stated billing unit, often price per million tokens, when calculating.

## Token management
- Remove irrelevant prompt details.
- Avoid repeating the same context.
- Ask for the required format and level of detail.
- Keep conversation history only as long as useful.
- Choose a model that fits the task and budget.

## Practice
Write one prompt that asks for a 5-mark exam answer and another that asks for a beginner-friendly explanation.
