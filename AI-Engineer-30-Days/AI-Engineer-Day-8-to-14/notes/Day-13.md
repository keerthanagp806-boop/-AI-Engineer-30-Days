# Day 13 – Running Local Models with Ollama

## 📚 Topics Learned
A local language model runs on a computer or server that you control, rather than sending every inference request to a hosted model provider.

## 🧠 Key Concepts

- **Inference:** Using a trained model to generate a prediction or response.
- **Inference SDK/client:** A software library that makes it easier for an application to send requests to a model.
- **Ollama:** A tool for downloading and running supported language models locally and exposing a local API.
- **Local LLM:** A large language model running on your own machine or infrastructure.
- **Transformers:** A Python library for using many pre-trained models; it is different from Ollama, although both can be used in AI workflows.

## 🧠 Example
Download a small Llama model with Ollama, then write a Python chatbot that sends messages to the local Ollama service.

## 💻 Practical Work

1. Install Ollama from https://ollama.com/download
2. In a terminal, download a model:

```bash
ollama pull llama3.2:1b
```

3. Check that it runs:

```bash
ollama run llama3.2:1b
```

4. Install the Python client:

```bash
python -m pip install ollama
```

5. Run `practicals/day13_ollama_chatbot.py`.

Ollama must be running locally. Model performance depends on available RAM, CPU/GPU, and model size. The model download needs internet; after downloading, local inference can work offline.

## 🎤 Interview Preparation
1. What is a local LLM?
2. What does Ollama do?
3. What is inference?
4. What are the trade-offs of running a model locally?

## 📌 Status
A local Python chatbot practical is included. It keeps a short conversation history during the current run.
