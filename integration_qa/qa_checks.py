# ShieldSense - Integration and QA Checks

VALID_RISK_LEVELS = {"Low", "Medium", "High"}


def validate_risk_level(risk_level):
    """Check that the risk level is one of the agreed categories."""
    return risk_level in VALID_RISK_LEVELS


def check_model_output(output):
    """Check that a model result contains the required fields."""
    if not isinstance(output, dict):
        return False

    if "risk_level" not in output:
        return False

    if "explanation" not in output:
        return False

    return validate_risk_level(output["risk_level"])


def run_basic_tests():
    """Run basic integration checks using sample model outputs."""

    test_outputs = [
        {
            "risk_level": "Low",
            "explanation": "No significant scam indicators detected."
        },
        {
            "risk_level": "Medium",
            "explanation": "Some suspicious indicators were detected."
        },
        {
            "risk_level": "High",
            "explanation": "Multiple scam indicators were detected."
        }
    ]

    for output in test_outputs:
        assert check_model_output(output)

    print("All basic integration checks passed.")


if __name__ == "__main__":
    run_basic_tests()
