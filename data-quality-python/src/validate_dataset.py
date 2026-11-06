from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "sample_data" / "ai_annotations.csv"
REPORT = ROOT / "reports" / "generated_quality_report.md"

ALLOWED_CATEGORIES = {"Person", "Vehicle", "Animal", "Food", "Electronic Device"}
MIN_CONFIDENCE = 0.0
MAX_CONFIDENCE = 1.0

def main():
    df = pd.read_csv(DATASET)

    required_columns = [
        "record_id", "image_file", "category",
        "confidence", "review_status"
    ]

    missing_columns = [c for c in required_columns if c not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    missing_values = int(df[required_columns].isna().sum().sum())
    duplicate_records = int(df.duplicated().sum())
    duplicate_record_ids = int(df["record_id"].duplicated().sum())

    invalid_categories = int((~df["category"].isin(ALLOWED_CATEGORIES)).sum())
    invalid_confidence = int(
        ((df["confidence"] < MIN_CONFIDENCE) |
         (df["confidence"] > MAX_CONFIDENCE)).fillna(False).sum()
    )

    confidence_missing = int(df["confidence"].isna().sum())
    review_needs_attention = int(
        (df["review_status"].astype(str).str.strip() == "Needs Review").sum()
    )

    category_distribution = df["category"].value_counts(dropna=False)

    quality_issues = (
        missing_values
        + duplicate_records
        + duplicate_record_ids
        + invalid_categories
        + invalid_confidence
    )

    status = "PASS" if quality_issues == 0 else "REVIEW REQUIRED"

    lines = [
        "# AI Dataset Quality Report",
        "",
        f"**Status:** {status}",
        f"**Records analyzed:** {len(df)}",
        "",
        "## Validation results",
        f"- Missing values: {missing_values}",
        f"- Duplicate rows: {duplicate_records}",
        f"- Duplicate record IDs: {duplicate_record_ids}",
        f"- Invalid categories: {invalid_categories}",
        f"- Invalid confidence scores: {invalid_confidence}",
        f"- Missing confidence scores: {confidence_missing}",
        f"- Records marked Needs Review: {review_needs_attention}",
        "",
        "## Category distribution",
    ]

    for category, count in category_distribution.items():
        lines.append(f"- {category}: {count}")

    lines.extend([
        "",
        "## Interpretation",
        "The dataset intentionally contains quality issues so the validation script can demonstrate how an AI data-quality workflow detects them before downstream use.",
        "",
        "## Recommended actions",
        "1. Normalize inconsistent labels such as vehicle.",
        "2. Investigate missing confidence values.",
        "3. Correct confidence values outside the 0–1 range.",
        "4. Review records explicitly marked Needs Review.",
    ])

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    print(f"Dataset: {DATASET}")
    print(f"Records: {len(df)}")
    print(f"Quality status: {status}")
    print(f"Missing values: {missing_values}")
    print(f"Duplicate rows: {duplicate_records}")
    print(f"Invalid categories: {invalid_categories}")
    print(f"Invalid confidence scores: {invalid_confidence}")
    print(f"Report written to: {REPORT}")

if __name__ == "__main__":
    main()
