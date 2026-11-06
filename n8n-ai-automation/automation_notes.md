# Automation Notes

## Business problem

AI evaluation teams can receive large volumes of structured evaluation records. Before those records enter a downstream process, basic validation can be automated.

## Rule implemented

The workflow accepts five evaluation dimensions:

- Accuracy
- Relevance
- Clarity
- Instruction Following
- Completeness

Each score must be between 1 and 5.

The workflow then calculates the average score.

### PASS

The payload is structurally valid and the calculated score is at least 3.5.

### REVIEW

The payload contains missing or invalid fields or the calculated score is below 3.5.

## Why n8n

n8n makes it possible to connect webhooks, validation logic, conditional routing, APIs, databases, spreadsheets, and AI services through visual workflows.

This portfolio example deliberately keeps the automation credential-free so a reviewer can import and understand the workflow immediately.

## Possible production extensions

- Store valid evaluations in PostgreSQL.
- Send review cases to Slack or email.
- Add an LLM-based secondary evaluation.
- Create a daily quality dashboard.
- Connect the workflow to a labeling or evaluation platform API.
