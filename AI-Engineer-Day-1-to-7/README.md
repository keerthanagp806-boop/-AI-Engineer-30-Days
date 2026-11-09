<<<<<<< HEAD
# AI Engineer Journey — Days 1 to 7

A beginner-friendly Week 1 learning repository with revision notes and a practical Python study assistant.

## Project structure

```text
AI-Engineer-Day-1-to-7/
├── README.md
├── app.py
├── api_chatbot.py
├── requirements.txt
├── .env.example
├── .gitignore
└── notes/
    ├── Day-01-AI-ML-DL.md
    ├── Day-02-LLM-Basics.md
    ├── Day-03-LLM-Workflow.md
    ├── Day-04-Revision.md
    ├── Day-05-Prompt-Engineering-and-Tokens.md
    ├── Day-06-Playground-and-Fine-Tuning.md
    └── Day-07-API-and-Chatbot.md
```

## Practical application: AI Engineer Study Assistant

`app.py` is an offline Python application. It lets you:
- revise core concepts from Days 1–7;
- read short explanations and examples;
- take a multiple-choice quiz;
- practise writing structured prompts;
- get a rough token-count estimate.

It uses basic Python concepts such as functions, dictionaries, lists, loops, conditionals, and user input. It does **not** call an AI model, so it works without an API key, internet connection, or paid API credits.

## Run the application

Open this folder in VS Code, open **Terminal → New Terminal**, and run:

```bash
py app.py
```

No extra packages are needed for this offline application.

## Optional: API chatbot

`api_chatbot.py` demonstrates how a Python application can send messages to an OpenAI model API and display the response. This requires:
1. an API key;
2. available API billing/credits;
3. the dependencies in `requirements.txt`.

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

Copy `.env.example` to a new file named `.env`, then add your own API key:

```env
OPENAI_API_KEY=your_actual_api_key
```

Run:

```bash
py api_chatbot.py
```

**Security:** Never upload `.env` or share your API key. `.gitignore` is configured to exclude `.env`.

## Learning tracker

Update each day's note with your own examples, questions, and learning reflections as you progress. Update your existing GitHub tracker separately with the days you have completed.

## Notes

These are concise revision notes for the Week 1 topics discussed. Day 3 and Day 4 are structured foundation/revision notes; add any additional topics from your own study-plan PDF if your exact syllabus differs.
=======
# -AI-Engineer-30-Days
My 30-Day Journey to Becoming an AI Engineer
>>>>>>> 6c7e74fa3bfe7cf018a2c3d597543e38e103451d
