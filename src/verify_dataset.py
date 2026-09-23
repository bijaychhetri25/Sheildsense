import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "shieldsense_messages.csv"


def verify_dataset():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    print("=== ShieldSense Dataset Verification ===")
    print(f"Total messages: {len(rows)}")

    # Check required columns
    required_columns = {
        "message_id",
        "message",
        "category",
        "risk_level",
        "synthetic",
        "verification_status"
    }

    missing_columns = required_columns - set(rows[0].keys())

    if missing_columns:
        print(f"Missing columns: {missing_columns}")
    else:
        print("Required columns: PASS")

    # Check duplicate messages
    messages = [row["message"].strip().lower() for row in rows]
    duplicates = len(messages) - len(set(messages))

    print(f"Duplicate messages: {duplicates}")

    # Check empty messages
    empty_messages = sum(
        1 for row in rows if not row["message"].strip()
    )

    print(f"Empty messages: {empty_messages}")

    # Check categories
    categories = sorted(set(row["category"] for row in rows))

    print("Categories:")
    for category in categories:
        count = sum(
            1 for row in rows if row["category"] == category
        )
        print(f"  - {category}: {count}")

    # Check risk levels
    risk_levels = sorted(set(row["risk_level"] for row in rows))

    print("Risk levels:")
    for risk in risk_levels:
        count = sum(
            1 for row in rows if row["risk_level"] == risk
        )
        print(f"  - {risk}: {count}")

    # Check verification status
    statuses = sorted(
        set(row["verification_status"] for row in rows)
    )

    print("Verification status:")
    for status in statuses:
        count = sum(
            1 for row in rows
            if row["verification_status"] == status
        )
        print(f"  - {status}: {count}")

    print("\nVerification check completed.")


if __name__ == "__main__":
    verify_dataset()