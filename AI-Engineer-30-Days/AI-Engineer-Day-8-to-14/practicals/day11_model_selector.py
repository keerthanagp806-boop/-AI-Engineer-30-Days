"""Day 11: A simple illustrative model-selection exercise."""

models = [
    {
        "name": "Local open-weight model",
        "access": "Run on your own hardware",
        "control": "More deployment control",
        "considerations": "Hardware, setup, licence, maintenance",
    },
    {
        "name": "Hosted closed-source model",
        "access": "Provider API",
        "control": "Provider manages model serving",
        "considerations": "Usage cost, network, provider data terms",
    },
]

if __name__ == "__main__":
    print("MODEL ACCESS COMPARISON")
    for model in models:
        print(f"\n{model['name']}")
        print("Access:", model["access"])
        print("Control:", model["control"])
        print("Consider:", model["considerations"])

    print("\nChoose based on task quality, latency, cost, privacy, hardware,")
    print("licence, customization, and expected traffic.")
