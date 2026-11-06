# AI Dataset Quality Report

**Status:** REVIEW REQUIRED

**Records analyzed:** 31

## Detected issues

- Missing values: 1
- Duplicate rows: 1
- Duplicate record IDs: 0
- Invalid categories: 1
- Invalid confidence scores: 1
- Missing confidence scores: 1
- Records marked Needs Review: 2

## Main findings

The sample dataset intentionally contains several issues that are common in AI data pipelines:

1. One category uses inconsistent capitalization: vehicle.
2. One confidence value is outside the valid 0–1 range: 1.08.
3. One confidence value is missing.
4. One duplicated annotation record is present.
5. Two records are explicitly marked for human review.

The purpose is to demonstrate how automated validation can identify problems before annotated data is used downstream.
