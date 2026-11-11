"""Day 12: Run a pre-trained sentiment-analysis model from Hugging Face.

Install first:
    python -m pip install transformers torch

The first run downloads model files and requires internet access.
"""

from transformers import pipeline

MODEL_ID = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

def main():
    print("Loading sentiment model. First run may download model files...")
    classifier = pipeline("sentiment-analysis", model=MODEL_ID)

    while True:
        text = input("\nEnter a review (or 'exit'): ").strip()
        if text.lower() == "exit":
            break
        if not text:
            print("Please enter some text.")
            continue

        result = classifier(text)[0]
        print("Sentiment:", result["label"])
        print("Confidence:", round(result["score"], 4))

if __name__ == "__main__":
    main()
