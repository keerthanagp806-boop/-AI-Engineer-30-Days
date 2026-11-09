# Day 7 — API Integration and Building a Chatbot

## What is an API?
An Application Programming Interface (API) allows software applications to communicate with each other.

## Basic request/response flow
1. Your Python application collects a user's message.
2. It authenticates with the API using a secret key.
3. It sends a request containing the prompt and settings.
4. The model service processes the request.
5. The service returns a response.
6. Your Python application displays the response.

## Important terms
- **API key:** A secret credential used to authenticate requests. Never publish it.
- **Request:** Data sent to the API.
- **Response:** Data returned by the API.
- **Error handling:** Code that handles invalid credentials, unavailable models, network failures, rate limits, or insufficient billing.

## Conversation history
A chatbot can send previous user and assistant messages with the latest question so the model can use earlier context. Long histories consume more tokens and may need to be shortened.

## This project's two modes
- `app.py`: Offline study assistant. Works without an API key or credits. It is a learning demo, not a real LLM.
- `api_chatbot.py`: Optional real API example. Requires an API key and available API billing/credits.

## Security checklist
- Keep your key in `.env`.
- Add `.env` to `.gitignore`.
- Never paste your key into GitHub, screenshots, or public messages.
- If a key is exposed, revoke it and create a replacement.

## Day 7 learning outcome
Be able to explain how a Python app sends a request to an LLM API, receives the generated response, and handles common errors.
