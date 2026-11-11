# AI Engineer Roadmap – Days 8 to 14

This folder contains learning notes and small Python practicals for Week 2 of the AI Engineer roadmap.

## Folder structure

```text
AI-Engineer-Day-8-to-14/
├── README.md
├── PROGRESS-TRACKER.md
├── requirements.txt
├── notes/
│   ├── Day-08.md
│   ├── Day-09.md
│   ├── Day-10.md
│   ├── Day-11.md
│   ├── Day-12.md
│   ├── Day-13.md
│   └── Day-14.md
└── practicals/
    ├── day08_prompt_patterns.py
    ├── day09_prompt_injection_demo.py
    ├── day10_safety_filter.py
    ├── day11_model_selector.py
    ├── day12_huggingface_sentiment.py
    ├── day13_ollama_chatbot.py
    └── day14_model_access_comparison.py
```

## How to use this folder

1. Read the relevant file in `notes/`.
2. Open the matching Python file in `practicals/`.
3. Run the practical after installing its requirements.
4. Experiment with different inputs and write down what you observe.
5. Update `PROGRESS-TRACKER.md` only after completing the work.

## Setup

Use Python 3.10–3.12 if possible for smoother compatibility with machine-learning packages.

Create and activate a virtual environment (Windows PowerShell):

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If Python 3.12 is not installed, use an installed compatible Python version and adjust the first command.

## Run the practicals

From this folder, for example:

```powershell
python practicals/day08_prompt_patterns.py
python practicals/day09_prompt_injection_demo.py
python practicals/day10_safety_filter.py
python practicals/day11_model_selector.py
python practicals/day12_huggingface_sentiment.py
python practicals/day13_ollama_chatbot.py
python practicals/day14_model_access_comparison.py
```

Some practicals require extra setup:
- **Day 12:** downloads a Hugging Face model the first time; internet is required for the initial download.
- **Day 13:** install Ollama separately, download a model with `ollama pull llama3.2:1b`, and keep Ollama running.
- **Day 14:** the comparison script runs locally and does not need an API key.

## Important safety notes

- Never upload API keys, passwords, `.env` files, or private data to GitHub.
- The Day 9 injection example and Day 10 safety filter are educational demonstrations, not complete security systems.
- A prompt or keyword filter alone cannot guarantee safety. Real applications need layered security, access controls, validation, monitoring, and appropriate moderation.
- Check each model's licence, usage restrictions, hardware needs, and privacy terms before using it.

## Suggested Git commit

```text
Day 8–14: Added prompt engineering, AI safety, model selection and Hugging Face/Ollama practicals
```
