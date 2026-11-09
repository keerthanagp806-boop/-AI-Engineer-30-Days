# Day 6 — Playground, Model Parameters and Fine-tuning

## Model experimentation
A model playground lets you try prompts and model settings without first building a complete application. Compare outputs and record what changes.

## Temperature
Temperature influences randomness and diversity in generated output.
- Lower temperature: usually more predictable and consistent.
- Higher temperature: usually more varied and creative.
- A higher value does not automatically mean a better answer.

## Top-P
Top-P (nucleus sampling) limits next-token candidates to a set whose cumulative probability reaches the chosen threshold. It is another way to influence output diversity.

**Experiment tip:** Change one sampling setting at a time so you can understand its effect.

## Maximum output tokens
Sets an upper limit on generated response length. It does not tell the model how many tokens it must use.

## Fine-tuning
Fine-tuning is additional training of an already pretrained model on a focused dataset. It can help a model adapt to a specialised task, format, or domain.

## Prompt engineering vs fine-tuning
- **Prompt engineering:** Changes the instructions or context supplied for a request; it does not itself retrain the model.
- **Fine-tuning:** Uses training examples to update the model's learned parameters.

## Evaluate model capabilities
Test accuracy, latency, cost, context capacity, safety, and performance on examples from your actual task.

## Experiment log
Record the model and settings, exact prompt, response quality, errors or missing details, and what you will change next.
