# ShieldSense QA Test Cases

## Purpose

These test cases are designed to check that ShieldSense correctly processes messages, produces the expected risk classification, and displays the result correctly in the user interface.

## Test Cases

| Test ID | Test Description | Expected Result | Status |
|---|---|---|---|
| TC01 | Enter a low-risk message | System displays Low risk and Green cue | Pending |
| TC02 | Enter a medium-risk message | System displays Medium risk and Amber cue | Pending |
| TC03 | Enter a high-risk message | System displays High risk and Red cue | Pending |
| TC04 | Submit an empty message | System displays an appropriate validation message | Pending |
| TC05 | Submit a normal non-scam message | System provides a risk classification | Pending |
| TC06 | Submit a message containing scam indicators | System identifies the appropriate risk level | Pending |
| TC07 | Compare model output with interface output | Interface result matches model result | Pending |
| TC08 | Check risk explanation | Plain-language explanation is displayed correctly | Pending |
| TC09 | Enter a long message | System processes the message without unexpected failure | Pending |
| TC10 | Test all three risk levels | Correct Green, Amber or Red cue is displayed | Pending |

## QA Objective

The purpose of these tests is to verify that the ShieldSense components work together correctly and that the risk classification produced by the detection component is accurately displayed by the interface.

Testing will be performed when the model and interface components are available for integration.
