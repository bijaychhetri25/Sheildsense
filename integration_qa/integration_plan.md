# ShieldSense Integration Plan

## Purpose

The integration plan explains how the data, scam detection model and user interface will work together in the ShieldSense application.

## Proposed Workflow

1. The user enters an SMS or chat message.
2. The interface sends the message to the scam detection component.
3. The detection component analyses the message.
4. The system classifies the message as Low, Medium or High risk.
5. The system generates a plain-language explanation.
6. The result is returned to the interface.
7. The interface displays the appropriate risk level and colour cue.
8. QA checks that the displayed result matches the model output.

## Risk Display

| Risk Level | Interface Cue |
|---|---|
| Low | Green |
| Medium | Amber |
| High | Red |

## Team Integration

### Jaskaran Singh – Data & Labelling Lead

Responsible for the labelled dataset and risk taxonomy.

### Kapil Thapa Magar – Model & Evaluation Lead

Responsible for the rules-based baseline, machine-learning classifier and model evaluation.

### Alisha – Interface & Accessibility Lead

Responsible for the user interface, accessibility and presentation of the risk result.

### Bijay Bahadur Chhetri – Integration, Documentation & QA Lead

Responsible for integration, documentation and quality assurance.

## Integration Objective

The objective is to ensure that the dataset, model and interface can work together correctly and that the final risk classification displayed to the user matches the output produced by the detection component.
