# Day 8 – Prompt Engineering

## 📚 Topics Learned
Prompt engineering is the practice of writing clear instructions and providing useful context so an AI model can produce a relevant response.

## 🧠 Key Concepts

- **Prompt:** The input sent to an AI model.
- **Instruction:** What the model should do.
- **Context:** Background information that helps the model answer.
- **Constraint:** A rule or limit, such as “use fewer than 100 words.”
- **Output format:** The required shape of the answer, such as a list or JSON.
- **Zero-shot prompting:** Ask the model to do a task without giving examples.
- **Few-shot prompting:** Give examples before asking the model to perform the task.
- **Role prompting:** Give the model a role, such as “You are a patient Python tutor.”
- **Prompt chaining:** Split a larger task into smaller steps, where one step's result is used by the next.
- **Structured prompting:** Clearly separate the role, task, context, constraints, and output format.

## 🧠 Example

Weak prompt: `Explain Python.`

Clearer prompt: `You are a beginner-friendly Python tutor. Explain Python loops in simple English. Give one short example and keep the answer under 150 words.`

## 💻 Practical Work
Run `practicals/day08_prompt_patterns.py`. Compare the prompt templates and observe how adding context, examples, and output constraints changes the instructions.

## 🛠️ Tools Explored
- ChatGPT or another LLM interface
- Python prompt templates

## 🎯 What I Learned
Clear instructions, useful context, examples, and output constraints make prompts easier for a model to follow. Prompting improves the request; it does not guarantee factual correctness.

## 🎤 Interview Preparation
1. What is prompt engineering?
2. What is the difference between zero-shot and few-shot prompting?
3. What is prompt chaining?
4. Why do we specify an output format?

## 📌 Status
Learning notes and a prompt-template practical are included. Mark this day complete after practising the examples.
