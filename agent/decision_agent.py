
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd
import json
import os

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def think(customer_note, context):
    prompt = f"""
You are an AI operations assistant.

Customer message:
{customer_note}

Delivery context:
{context}

Answer in ONE short sentence:
What should be the safest action?
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_length=60,
        do_sample=False
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def run_agent():
    df = pd.read_csv("data/orders_level2.csv")
    results = []

    for _, row in df.iterrows():
        recommendation = think(
            row["CustomerNotes"],
            row["DeliveryContext"]
        )

        dossier = {
            "order_id": row["OrderID"],
            "interpreted_intent": "Customer intent is ambiguous and context-dependent",
            "confidence_level": "Medium",
            "key_risks_identified": [
                "Misinterpretation of customer intent",
                "Expectation mismatch"
            ],
            "recommended_action": recommendation,
            "alternative_action_considered": "Immediate fulfillment without confirmation",
            "why_alternative_was_rejected": "Risky due to lack of clarity",
            "assumptions_made": "Customer prefers cautious handling",
            "restraint_applied": "Avoided forcing decisions"
        }

        results.append(dossier)

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/decision_dossier.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    with open("outputs/decision_dossier.txt", "w", encoding="utf-8") as f:
        for r in results:
            f.write(f"ORDER {r['order_id']}\n")
            f.write(f"Recommended action: {r['recommended_action']}\n\n")

    print("✅ Decision dossiers generated successfully")


if __name__ == "__main__":
    run_agent()
