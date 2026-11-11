# Day 14 – Hosted AI Platforms and Model Deployment Choices

## 📚 Topics Learned
AI models can run on your own infrastructure or be accessed through hosted platforms. Hosted services manage much of the model infrastructure and expose APIs or managed tools.

## 🧠 Key Concepts

- **Hosted inference:** A provider runs the model and your application sends requests over a network.
- **Cloud AI platform:** A cloud service that supports building, deploying, or using AI/ML workloads.
- **API:** A defined way for one application to communicate with another.
- **Local inference:** Your computer or server runs the model.
- **Trade-off:** A decision balancing cost, control, speed, privacy, maintenance, and scale.

## Examples of platforms
- **Microsoft Azure AI:** Cloud services for building AI applications.
- **Amazon SageMaker:** Services for building, training, and deploying machine-learning models.
- **Replicate:** A platform for running many models through hosted APIs.
- **Mistral AI:** A company offering language models and hosted services.
- **Cohere:** A company offering language, embedding, reranking, and related AI services.

Platform features and pricing change; check official documentation before choosing a service.

## 🧠 Example
A prototype chatbot might use a local model through Ollama. A production application with many users might choose a hosted model to avoid managing model-serving hardware. The correct choice depends on workload, privacy, budget, and operational needs.

## Local vs Hosted

| Local | Hosted |
|---|---|
| You manage the machine and deployment | Provider manages model infrastructure |
| Can offer more control over deployment and data flow | Requests travel to the provider under its service terms |
| Hardware and maintenance are your responsibility | Usually charged by usage or plan |
| Can work offline after model download | Usually needs network access |
| Capacity depends on your hardware | Can scale through provider services, subject to limits and cost |

## 💻 Practical Work
Run `practicals/day14_model_access_comparison.py` to print a decision checklist for local and hosted approaches.

## 🎤 Interview Preparation
1. What is hosted inference?
2. Give two examples of cloud AI platforms.
3. What is one advantage and one disadvantage of local models?
4. What should you check before selecting a hosted provider?

## 📌 Status
A local-versus-hosted comparison practical is included.
