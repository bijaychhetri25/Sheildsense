import csv
import random
from pathlib import Path

random.seed(42)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_DIR / "shieldsense_messages.csv"


# Different message components are combined to create varied messages.
scam_data = {
    "Bank Scam": {
        "risk": "Red",
        "subjects": [
            "Your bank account",
            "Your online banking access",
            "A recent transaction",
            "Your debit card",
            "Your account security"
        ],
        "problems": [
            "has been temporarily restricted",
            "requires immediate verification",
            "has detected unusual activity",
            "has a pending security alert",
            "requires an identity check"
        ],
        "actions": [
            "Verify your details",
            "Confirm your account",
            "Review the security alert",
            "Confirm the transaction",
            "Update your information"
        ]
    },

    "Delivery Scam": {
        "risk": "Red",
        "subjects": [
            "Your parcel",
            "Your delivery",
            "Your package",
            "Your shipment",
            "Your courier delivery"
        ],
        "problems": [
            "could not be delivered",
            "is waiting for address confirmation",
            "requires a delivery payment",
            "has been placed on hold",
            "requires additional information"
        ],
        "actions": [
            "Confirm your delivery address",
            "Pay the delivery fee",
            "Reschedule the delivery",
            "Update your delivery details",
            "Confirm your parcel"
        ]
    },

    "Government Scam": {
        "risk": "Red",
        "subjects": [
            "Your government account",
            "Your tax record",
            "Your government payment",
            "Your online government account",
            "Your outstanding notice"
        ],
        "problems": [
            "requires urgent verification",
            "has an outstanding issue",
            "is awaiting confirmation",
            "requires an immediate response",
            "has a pending notification"
        ],
        "actions": [
            "Verify your information",
            "Confirm your details",
            "Review the notice",
            "Complete the requested information",
            "Confirm your account"
        ]
    },

    "Job Scam": {
        "risk": "Red",
        "subjects": [
            "Your work-from-home application",
            "Your online job application",
            "A remote employment opportunity",
            "Your job offer",
            "A flexible work opportunity"
        ],
        "problems": [
            "has been selected for further processing",
            "requires an application payment",
            "has been shortlisted",
            "requires additional personal information",
            "is ready for immediate approval"
        ],
        "actions": [
            "Pay the registration fee",
            "Send your banking details",
            "Confirm your application",
            "Complete the employment form",
            "Provide your personal information"
        ]
    },

    "Investment Scam": {
        "risk": "Red",
        "subjects": [
            "Your investment opportunity",
            "A new investment offer",
            "Your investment account",
            "A limited investment opportunity",
            "A special financial opportunity"
        ],
        "problems": [
            "expires today",
            "requires immediate confirmation",
            "offers guaranteed returns",
            "has limited availability",
            "requires an initial transfer"
        ],
        "actions": [
            "Transfer the initial amount",
            "Confirm your investment",
            "Register for the opportunity",
            "Provide your payment details",
            "Secure your investment"
        ]
    },

    "Prize Scam": {
        "risk": "Red",
        "subjects": [
            "Your prize",
            "Your cash reward",
            "Your promotional reward",
            "Your competition prize",
            "Your selected reward"
        ],
        "problems": [
            "has been approved",
            "is waiting to be claimed",
            "requires a processing payment",
            "expires today",
            "requires identity confirmation"
        ],
        "actions": [
            "Claim your reward",
            "Confirm your details",
            "Pay the processing fee",
            "Complete the claim form",
            "Verify your information"
        ]
    },

    "Tech Support Scam": {
        "risk": "Red",
        "subjects": [
            "Your computer",
            "Your device",
            "Your security software",
            "Your internet connection",
            "Your account security"
        ],
        "problems": [
            "has detected a serious security problem",
            "may have been infected",
            "requires an urgent security check",
            "has an unusual security alert",
            "requires immediate technical support"
        ],
        "actions": [
            "Call the support number",
            "Download the security tool",
            "Contact technical support",
            "Confirm your device details",
            "Install the recommended software"
        ]
    }
}


legitimate_messages = [
    "Your appointment is confirmed for {day} at {time}.",
    "Your university class is scheduled for {day} at {time}.",
    "Your monthly statement is now available in your official online account.",
    "Your parcel has been delivered successfully.",
    "Your electricity bill is now available to view online.",
    "Your library book is due on {day}.",
    "Your scheduled service appointment is confirmed for {day}.",
    "Your account statement has been generated successfully.",
    "Your order has been dispatched and can be tracked through the official app.",
    "Your payment has been received successfully.",
    "Your membership renewal is scheduled for {day}.",
    "Your appointment reminder is for {day} at {time}.",
    "Your university timetable has been updated.",
    "Your online booking has been confirmed.",
    "Your subscription payment was processed successfully.",
    "Your delivery has been scheduled for {day}.",
    "Your account notification is available in the official application.",
    "Your scheduled maintenance appointment is confirmed.",
    "Your document is ready to collect from the service centre.",
    "Your application has been received successfully."
]


days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

times = [
    "9:00 AM",
    "10:30 AM",
    "12:00 PM",
    "2:00 PM",
    "3:30 PM",
    "4:30 PM"
]


records = []
used_messages = set()

message_id = 1


# Generate varied scam messages
for category, details in scam_data.items():

    combinations = []

    for subject in details["subjects"]:
        for problem in details["problems"]:
            for action in details["actions"]:
                combinations.append(
                    (subject, problem, action)
                )

    random.shuffle(combinations)

    # Generate 20 messages per scam category
    for subject, problem, action in combinations[:20]:

        message = (
            f"{subject} {problem}. "
            f"{action} now using the secure verification page."
        )

        if message not in used_messages:
            records.append({
                "message_id": f"SMS{message_id:03d}",
                "message": message,
                "category": category,
                "risk_level": details["risk"],
                "synthetic": True,
                "verification_status": "needs_review"
            })

            used_messages.add(message)
            message_id += 1

# Assign 20 scam messages as Amber for medium-risk examples.
# These remain scam messages, but represent situations where
# the user should be cautious and verify independently.

scam_records = [
    record for record in records
    if record["category"] != "Legitimate"
]

random.shuffle(scam_records)

for record in scam_records[:20]:
    record["risk_level"] = "Amber"
# Generate 60 legitimate messages
while len(records) < 200:

    template = random.choice(legitimate_messages)

    message = template.format(
        day=random.choice(days),
        time=random.choice(times)
    )

    if message not in used_messages:
        records.append({
            "message_id": f"SMS{message_id:03d}",
            "message": message,
            "category": "Legitimate",
            "risk_level": "Green",
            "synthetic": True,
            "verification_status": "needs_review"
        })

        used_messages.add(message)
        message_id += 1


# Shuffle the final dataset
random.shuffle(records)

# Rewrite message IDs after shuffling
for number, record in enumerate(records, start=1):
    record["message_id"] = f"SMS{number:03d}"


# Save CSV
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

    fieldnames = [
        "message_id",
        "message",
        "category",
        "risk_level",
        "synthetic",
        "verification_status"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(records)


print("=== ShieldSense Dataset Generation ===")
print(f"Dataset created successfully: {OUTPUT_FILE}")
print(f"Total messages: {len(records)}")
print(f"Unique messages: {len(set(r['message'] for r in records))}")
print("Verification status: needs_review")