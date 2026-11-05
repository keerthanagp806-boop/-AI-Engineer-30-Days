# Beginner demonstration: training vs inference
# This is a tiny simulation, NOT a real trained language model.

def show_training():
    print("\nTRAINING (conceptual example)")
    print("A model is shown many examples during training.")
    print("It adjusts internal parameters to learn patterns.")
    print("This demo does not actually train a machine-learning model.")


def simple_inference_demo():
    print("\nINFERENCE (toy example)")
    print("A user gives a new input to an already-built system.")
    question = input("Ask a simple question: ")

    # A fixed response is used only to demonstrate the input/output flow.
    # A real LLM would generate its response using learned model parameters.
    print("\nInput received:", question)
    print("Toy system response: I received your question.")
    print("A real LLM would generate a context-aware answer here.")


def main():
    print("LLM Concepts: Training and Inference")
    show_training()
    simple_inference_demo()


if __name__ == "__main__":
    main()
