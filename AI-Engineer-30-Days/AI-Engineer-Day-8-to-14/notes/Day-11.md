# Day 11 – Open-Weight and Closed-Source Models

## 📚 Topics Learned
AI models can be made available in different ways. The choice affects control, deployment, cost, privacy, and maintenance.

## 🧠 Key Concepts

- **Open-weight model:** Model weights are available for download. The licence may allow some uses and restrict others. “Open-weight” does not automatically mean fully open-source.
- **Closed-source model:** The provider does not publicly release the model weights. Developers commonly access it through a hosted product or API.
- **Pre-trained model:** A model that has already learned patterns from training data before a developer uses it.
- **Self-hosted model:** A model deployed on infrastructure managed by you or your organization.
- **Model selection trade-offs:** Compare quality, latency, cost, privacy, hardware, licence, customization, and scale.

## 🧠 Examples
- Llama-family models have downloadable model weights under model-specific licences.
- GPT models are generally accessed through provider-hosted services rather than downloadable public weights.

A model can be both **pre-trained** and **self-hosted**. These terms describe different things: training history versus deployment location.

## Model selection checklist

| Factor | Question |
|---|---|
| Quality | Does it perform well on my task? |
| Cost | What are inference and hosting costs? |
| Latency | Is the response fast enough? |
| Privacy | Where does data go and how is it handled? |
| Hardware | Can my server run it? |
| Licence | Does the licence permit my intended use? |
| Scale | Can the setup handle expected traffic? |

## 💻 Practical Work
Run `practicals/day11_model_selector.py` to see a simple rule-based selection example. It is illustrative, not a benchmark.

## 🎤 Interview Preparation
1. What is an open-weight model?
2. What is a closed-source model?
3. What is the difference between pre-trained and self-hosted?
4. What factors influence model selection?

## 📌 Status
Comparison notes and a simple selection exercise are included.
