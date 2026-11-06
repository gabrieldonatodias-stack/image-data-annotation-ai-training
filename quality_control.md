# Quality Control

## Purpose

Quality control identifies incorrect, incomplete, inconsistent or ambiguous annotations before the dataset is considered final.

## Review Checklist

Each annotation should be checked for:
- Correct image ID
- Correct filename
- Valid category
- Clear object description
- Appropriate confidence level
- Notes completed when necessary
- Consistency with the annotation guidelines

## QC Status

- Approved — annotation follows the guidelines.
- Needs Review — annotation contains uncertainty or requires additional verification.
- Corrected — an issue was identified and corrected.

## Common Quality Issues

### Incorrect Category
Example: a smartphone incorrectly classified as Vehicle.
Action: change the category to Electronic Device.

### Missing Information
If a required field is empty, complete it before approval.

### Inconsistent Labeling
If similar objects receive different categories, review the guidelines and standardize the labels.

### Low Confidence
If the subject is difficult to identify, mark it Needs Review and explain the uncertainty.

## Quality-Control Objective

Create a dataset that is reliable, consistent and suitable as a demonstration of an AI data-preparation workflow.
