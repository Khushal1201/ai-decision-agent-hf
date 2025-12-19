<<<<<<< HEAD
# AI Decision Agent – Level 2 Challenge

## Overview
This project implements a **Data-Driven AI Decision Agent** that interprets ambiguous, indirect, and emotional customer instructions to generate actionable recommendations. The agent reads order data, reasons about customer intent, identifies risks, and provides a recommended action while applying restraint when appropriate.  

It demonstrates **decision-making under ambiguity**, focusing on reasoning, risk assessment, and applying restraint rather than hard-coded rules.

---

## Folder Structure

ai-decision-agent-hf/
│
├── run.py # Entry point to run the agent
├── agent/
│ ├── init.py # Required for package structure
│ └── decision_agent.py # Main agent logic
├── data/
│ └── orders_level2.csv # Input CSV with customer orders
└── outputs/ # Generated outputs (JSON + TXT)

---

## How to run

1. Clone the repository

2. Create Python environment 

3. Install dependencies
pip install -r requirements.txt

4. Prepare input data

5. Run the agent
python run.py

6. Check outputs

After execution, the agent will generate outputs in the outputs/ folder:

decision_dossier.json → structured JSON with all decisions

decision_dossier.txt → human-readable recommendations

Agent Reasoning

Reads customer notes and delivery context for each order.

Interprets implicit intent rather than relying on keywords or rules.

Identifies potential risks, such as ambiguous instructions or expectation mismatches.

Recommends a cautious action that balances customer needs and operational safety.

Considers alternative actions, explaining why they are rejected.

Explicitly acknowledges uncertainty when instructions are vague.

Applies restraint, avoiding forced or risky decisions.

Produces human-readable output for easy evaluation.

Notes

Uses Google FLAN-T5-base for reasoning.

Decisions are structured via code; LLM generates natural-language reasoning.

Designed to demonstrate AI agent behavior under ambiguity rather than deterministic logic.

Safe for Level-2 evaluation: handles vague, emotional, and contradictory customer notes effectively.

#### Summary

This project provides a full AI Decision Agent pipeline:

Reads order CSV with customer notes

Uses LLM to reason about intent and risks

Generates structured JSON and TXT decision dossiers

Applies restraint and cautious recommendations when uncertainty exists

This demonstrates the ability to think, reason, and act under ambiguity, fulfilling the Level-2 challenge requirements.
=======
# ai-decision-agent-hf
>>>>>>> de25e7a079997ebb07ec6980eb7d0b973c98add6
