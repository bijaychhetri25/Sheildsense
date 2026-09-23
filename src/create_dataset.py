import csv
import os
from itertools import product


# ============================================================
# ShieldSense Dataset Generator
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "data",
    "shieldsense_messages.csv"
)


# ============================================================
# Scam message components
# ============================================================

scam_data = {
    "Bank Scam": {
        "subjects": [
            "your bank account",
            "your online banking account",
            "your bank card",
            "your banking profile",
            "your account security",
            "your recent transaction"
        ],
        "problems": [
            "has been temporarily restricted",
            "requires immediate verification",
            "has detected suspicious activity",
            "needs a security confirmation",
            "has been flagged for unusual activity",
            "requires identity confirmation"
        ],
        "actions": [
            "Confirm your details using the secure verification page.",
            "Verify your account immediately to avoid suspension.",
            "Confirm your banking information now.",
            "Use the verification link to restore access.",
            "Update your details before the account is restricted."
        ]
    },

    "Delivery Scam": {
        "subjects": [
            "your parcel",
            "your delivery",
            "your package",
            "your shipment",
            "your courier delivery",
            "your delivery order"
        ],
        "problems": [
            "could not be delivered",
            "is waiting for address confirmation",
            "has been placed on hold",
            "requires a delivery fee",
            "has an incorrect delivery address",
            "is waiting for payment"
        ],
        "actions": [
            "Pay the required fee using the attached link.",
            "Confirm your delivery details immediately.",
            "Update your address to arrange delivery.",
            "Complete the payment before the parcel is returned.",
            "Use the link to reschedule the delivery."
        ]
    },

    "Government Scam": {
        "subjects": [
            "your government payment",
            "your tax account",
            "your government benefit",
            "your tax refund",
            "your official account",
            "your government record"
        ],
        "problems": [
            "requires additional information",
            "has an outstanding issue",
            "is waiting for identity verification",
            "has been flagged for review",
            "requires urgent confirmation",
            "cannot be processed"
        ],
        "actions": [
            "Submit your personal information immediately.",
            "Confirm your identity using the attached link.",
            "Pay the outstanding amount now.",
            "Verify your details to avoid further action.",
            "Complete the online verification process."
        ]
    },

    "Job Scam": {
        "subjects": [
            "your job application",
            "your employment opportunity",
            "your online job application",
            "your work-from-home position",
            "your interview application",
            "your employment offer"
        ],
        "problems": [
            "requires additional personal information",
            "has been selected for further processing",
            "requires an application payment",
            "needs identity verification",
            "has been approved for the next stage",
            "requires your banking details"
        ],
        "actions": [
            "Pay the registration fee to continue.",
            "Send your personal details immediately.",
            "Provide your bank information for salary processing.",
            "Complete the verification form now.",
            "Pay the required application charge."
        ]
    },

    "Investment Scam": {
        "subjects": [
            "your investment opportunity",
            "your investment account",
            "your trading account",
            "your cryptocurrency investment",
            "your investment withdrawal",
            "your trading opportunity"
        ],
        "problems": [
            "has generated a large return",
            "requires a withdrawal fee",
            "needs account verification",
            "has been selected for a special opportunity",
            "requires an urgent deposit",
            "has a pending withdrawal"
        ],
        "actions": [
            "Pay the required fee to release your funds.",
            "Deposit the requested amount immediately.",
            "Confirm your banking details to withdraw your money.",
            "Use the secure link to claim your investment return.",
            "Complete verification before the opportunity expires."
        ]
    },

    "Prize Scam": {
        "subjects": [
            "your prize",
            "your competition prize",
            "your reward",
            "your promotional prize",
            "your winning notification",
            "your cash reward"
        ],
        "problems": [
            "has been selected for collection",
            "requires a small processing fee",
            "is waiting for your confirmation",
            "has been approved for delivery",
            "will expire today",
            "requires identity confirmation"
        ],
        "actions": [
            "Pay the processing fee to receive your prize.",
            "Confirm your details immediately.",
            "Use the link to claim your reward.",
            "Provide your banking details for payment.",
            "Complete the claim form before the deadline."
        ]
    },

    "Tech Support Scam": {
        "subjects": [
            "your computer",
            "your device",
            "your account security",
            "your antivirus protection",
            "your device security",
            "your online security"
        ],
        "problems": [
            "has detected a serious security threat",
            "may have been infected",
            "has detected suspicious activity",
            "requires immediate technical support",
            "has a critical security problem",
            "requires urgent protection"
        ],
        "actions": [
            "Call the support number immediately.",
            "Install the security software from the provided link.",
            "Confirm your device details now.",
            "Allow the support team to access your computer.",
            "Pay for the security service immediately."
        ]
    }
}


# ============================================================
# Legitimate and hard-negative messages
# These are synthetic examples.
# ============================================================

legitimate_templates = [

    "Your bank statement is ready to view in your official account.",
    "Your payment has been processed successfully.",
    "Your delivery is ready to track through the official service.",
    "Your parcel delivery status has been updated.",
    "Your ACU student account has a new notification.",
    "Your ACU tuition payment receipt is available in your student portal.",
    "Your bank account balance is available in your online banking app.",
    "Your scheduled payment has been successfully processed.",
    "Your library account has been updated.",
    "Your university enrolment confirmation is available.",
    "Your class attendance record has been updated.",
    "Your official appointment reminder has been issued.",
    "Your service request has been received.",
    "Your order confirmation is available in the official application.",
    "Your membership details have been updated.",
    "Your utility account statement is available online.",
    "Your account information has been updated successfully.",
    "Your booking confirmation is available in the official system.",
    "Your application status has been updated.",
    "Your scheduled maintenance notification is available.",

    # Hard-negative legitimate-style examples
    "Your bank statement is ready to view at https://www.example.com/account.",
    "Your payment has been processed. View your receipt at https://www.example.com/receipt.",
    "Your delivery is ready to track at https://www.example.com/track.",
    "Your parcel delivery has been updated. Check the status at https://www.example.com/delivery.",
    "Your ACU student account has a new notification. Check your student portal at https://www.example.com/student.",
    "Your ACU tuition payment receipt is available at https://www.example.com/receipt.",
    "Your bank account balance is available in your online banking app. Visit https://www.example.com/banking.",
    "Your scheduled payment has been successfully processed. View details at https://www.example.com/payment."
]


# ============================================================
# Create 120 scam messages
# ============================================================

scam_records = []

# Exactly 120 scam messages:
# Bank = 18
# Other 6 categories = 17 each

target_counts = {
    "Bank Scam": 18,
    "Delivery Scam": 17,
    "Government Scam": 17,
    "Job Scam": 17,
    "Investment Scam": 17,
    "Prize Scam": 17,
    "Tech Support Scam": 17
}


for category, target in target_counts.items():

    data = scam_data[category]

    combinations = list(
        product(
            data["subjects"],
            data["problems"],
            data["actions"]
        )
    )

    created = 0

    for subject, problem, action in combinations:

        if created >= target:
            break

        message = f"Your {subject} {problem}. {action}"

        scam_records.append({
            "message": message,
            "category": category,
            "synthetic": True,
            "verification_status": "needs_review"
        })

        created += 1

    if created != target:
        raise RuntimeError(
            f"{category}: expected {target}, created {created}"
        )


# ============================================================
# Assign 60 Amber and 60 Red
# ============================================================

for index, record in enumerate(scam_records):

    if index < 60:
        record["risk_level"] = "Amber"
    else:
        record["risk_level"] = "Red"


# ============================================================
# Create final records
# ============================================================

records = []
message_id = 1


# Add scam records

for record in scam_records:

    records.append({
        "message_id": f"SMS{message_id:03d}",
        "message": record["message"],
        "category": record["category"],
        "risk_level": record["risk_level"],
        "synthetic": record["synthetic"],
        "verification_status": record["verification_status"]
    })

    message_id += 1


# ============================================================
# Create exactly 60 Green messages
# ============================================================

green_messages = []

# First create variations using day/time
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

times = [
    "9:00 AM",
    "11:30 AM",
    "2:00 PM",
    "6:30 PM"
]


for template in legitimate_templates:

    if len(green_messages) >= 60:
        break

    # If the message is already unique, add it directly
    green_messages.append(template)

    if len(green_messages) >= 60:
        break

    # Add controlled variations
    for day in days:

        if len(green_messages) >= 60:
            break

        for time in times:

            if len(green_messages) >= 60:
                break

            variation = f"{template} Notification received on {day} at {time}."

            green_messages.append(variation)


# Make sure exactly 60 Green messages exist
green_messages = green_messages[:60]


if len(green_messages) != 60:
    raise RuntimeError(
        f"Expected 60 Green messages, created {len(green_messages)}"
    )


# Add Green records

for message in green_messages:

    records.append({
        "message_id": f"SMS{message_id:03d}",
        "message": message,
        "category": "Legitimate",
        "risk_level": "Green",
        "synthetic": True,
        "verification_status": "needs_review"
    })

    message_id += 1


# ============================================================
# Final checks
# ============================================================

if len(records) != 180:
    raise RuntimeError(
        f"Expected 180 records, but created {len(records)}"
    )


messages = [
    record["message"]
    for record in records
]

if len(messages) != len(set(messages)):
    raise RuntimeError("Duplicate messages detected.")


red_count = sum(
    record["risk_level"] == "Red"
    for record in records
)

amber_count = sum(
    record["risk_level"] == "Amber"
    for record in records
)

green_count = sum(
    record["risk_level"] == "Green"
    for record in records
)


if red_count != 60:
    raise RuntimeError(f"Expected 60 Red, found {red_count}")

if amber_count != 60:
    raise RuntimeError(f"Expected 60 Amber, found {amber_count}")

if green_count != 60:
    raise RuntimeError(f"Expected 60 Green, found {green_count}")


# ============================================================
# Write CSV
# ============================================================

os.makedirs(
    os.path.dirname(OUTPUT_FILE),
    exist_ok=True
)


fieldnames = [
    "message_id",
    "message",
    "category",
    "risk_level",
    "synthetic",
    "verification_status"
]


with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(records)


# ============================================================
# Display result
# ============================================================

print("========================================")
print("ShieldSense Dataset Generation")
print("========================================")
print(f"Dataset created successfully:")
print(OUTPUT_FILE)
print()
print(f"Total messages: {len(records)}")
print(f"Unique messages: {len(set(messages))}")
print()
print("Risk levels:")
print(f"Red:   {red_count}")
print(f"Amber: {amber_count}")
print(f"Green: {green_count}")
print()
print("========================================")
print("Dataset generation completed successfully.")
print("========================================")