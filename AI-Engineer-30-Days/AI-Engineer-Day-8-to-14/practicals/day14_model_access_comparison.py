"""Day 14: Local vs hosted model decision checklist.

This script does not call a provider. It helps compare deployment choices
before selecting a model for a project.
"""

questions = [
    "Does the task require high answer quality or specialized capabilities?",
    "What is the expected number of users and requests?",
    "What is the budget for inference and infrastructure?",
    "What data privacy and residency requirements apply?",
    "Do you have hardware and skills to host and monitor a model?",
    "Does the model licence or provider agreement permit your use?",
    "What latency and uptime are required?",
]

if __name__ == "__main__":
    print("MODEL DEPLOYMENT DECISION CHECKLIST\n")
    for number, question in enumerate(questions, start=1):
        print(f"{number}. {question}")

    print("\nLOCAL OPTION: more infrastructure control; you manage hardware and operations.")
    print("HOSTED OPTION: provider manages serving; check pricing, limits, and data terms.")
    print("\nChoose only after testing candidate models on representative examples.")
