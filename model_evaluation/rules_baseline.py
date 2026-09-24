import re


# ShieldSense Week 3 - Proposed Rules-Based Baseline
# Student: Kapil Thapa Magar
# Role: Model & Evaluation Lead
#
# These are initial proposed rules.
# They may change after team and supervisor feedback.


# -----------------------------
# 1. Scam indicator keywords
# -----------------------------

URGENCY_WORDS = [
    "urgent",
    "immediately",
    "act now",
    "limited time"
]

FINANCIAL_WORDS = [
    "payment",
    "bank account",
    "transfer",
    "pay now"
]

SENSITIVE_INFO_WORDS = [
    "password",
    "pin",
    "card details",
    "bank details"
]

PRIZE_WORDS = [
    "winner",
    "prize",
    "claim reward",
    "congratulations"
]

THREAT_WORDS = [
    "account suspended",
    "account blocked",
    "account locked",
    "final warning"
]


# -----------------------------
# 2. Detection functions
# -----------------------------

def contains_keyword(message, keywords):
    """Check whether the message contains a listed keyword."""
    message = message.lower()
    return any(keyword in message for keyword in keywords)


def contains_url(message):
    """Check whether the message contains a URL."""
    url_pattern = r"https?://\S+|www\.\S+"
    return bool(re.search(url_pattern, message.lower()))


# -----------------------------
# 3. Rules-based classifier
# -----------------------------

def classify_message(message):

    score = 0
    reasons = []

    if contains_keyword(message, URGENCY_WORDS):
        score += 1
        reasons.append("Urgency language detected")

    if contains_keyword(message, FINANCIAL_WORDS):
        score += 2
        reasons.append("Financial/payment language detected")

    if contains_keyword(message, SENSITIVE_INFO_WORDS):
        score += 3
        reasons.append("Request for sensitive information detected")

    if contains_url(message):
        score += 2
        reasons.append("URL detected")

    if contains_keyword(message, PRIZE_WORDS):
        score += 2
        reasons.append("Prize/reward language detected")

    if contains_keyword(message, THREAT_WORDS):
        score += 2
        reasons.append("Threat or account-warning language detected")

    # Proposed thresholds - not final
    if score >= 5:
        risk = "HIGH"

    elif score >= 2:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    return {
        "message": message,
        "score": score,
        "risk": risk,
        "reasons": reasons
    }


# -----------------------------
# 4. Test messages
# -----------------------------

if __name__ == "__main__":

    test_messages = [
        "Hi, are we still meeting at 4pm today?",

        "Your payment is overdue. Please check your account.",

        "Congratulations! You have won a prize.",

        "URGENT! Your account has been suspended. "
        "Verify your password immediately at http://example.com"
    ]

    for message in test_messages:

        result = classify_message(message)

        print("\n-----------------------------------")
        print("Message:", result["message"])
        print("Score:", result["score"])
        print("Risk:", result["risk"])
        print("Reasons:", result["reasons"])