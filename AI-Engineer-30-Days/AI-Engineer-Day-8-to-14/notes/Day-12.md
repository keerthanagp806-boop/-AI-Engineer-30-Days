# Day 12 – Hugging Face Hub and Pre-trained Models

## 📚 Topics Learned
Hugging Face is a platform and ecosystem for discovering, sharing, and using machine-learning models, datasets, and applications.

## 🧠 Key Concepts

- **Hugging Face Hub:** An online hub where developers can discover model repositories, datasets, and demos.
- **Model card:** Documentation describing a model's intended use, limitations, training details, and other information.
- **AI task:** The kind of job a model performs, such as text classification, sentiment analysis, translation, summarization, or image classification.
- **Transformers:** A Python library that provides tools to load and use many pre-trained transformer models.
- **Model licence:** The terms that describe how a model may be used. Check it before using a model in a project.

## 🧠 Example
A sentiment-analysis model receives “I really enjoyed this course” and predicts a positive sentiment label.

## 💻 Practical Work
Run `practicals/day12_huggingface_sentiment.py`.

Install dependencies:

```bash
python -m pip install transformers torch
```

The first run downloads model files, so internet access is needed. The model may require memory and processing resources.

## How to choose a model
1. Search for the task on the Hub.
2. Read the model card.
3. Check the licence and limitations.
4. Check supported languages and input size.
5. Try sample inputs and evaluate results.

## 🎤 Interview Preparation
1. What is Hugging Face?
2. What is the Hugging Face Hub?
3. What is a model card?
4. What does the Transformers library do?

## 📌 Status
A sentiment-analysis practical is included.
