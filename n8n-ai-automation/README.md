# AI Data Evaluation Automation with n8n

## Overview

This project demonstrates a practical automation workflow built with n8n.

The workflow receives an AI evaluation record through a webhook, validates required fields, calculates a quality score, applies a decision rule, and returns a structured result.

No confidential API, client data, or employer workflow is used.

## Automation flow

Webhook → Validate & Score → Quality Check → Valid Result or Human Review

## Example input

    {
      "evaluation_id": "EVAL_011",
      "accuracy": 5,
      "relevance": 5,
      "clarity": 4,
      "instruction_following": 5,
      "completeness": 4
    }

## Example output

    {
      "status": "PASS",
      "evaluation_id": "EVAL_011",
      "overall_score": 4.6,
      "message": "Evaluation passed automated quality checks."
    }

## What the workflow demonstrates

- Webhook-based automation
- Structured JSON handling
- Data validation
- Conditional branching
- Automated quality scoring
- Error handling
- Workflow documentation

## How to use

1. Open n8n.
2. Import workflow.json.
3. Activate the workflow or run it manually in test mode.
4. Copy the Webhook test URL.
5. Send the example JSON payload with an HTTP POST request.
6. Inspect the returned JSON.

## Portfolio positioning

This project demonstrates practical AI workflow automation with n8n, connecting data intake, validation, business rules, and automated responses without requiring a custom backend.

## Important

The workflow is intentionally self-contained. It does not require an OpenAI API key, paid service, or external credential to demonstrate the automation logic.
