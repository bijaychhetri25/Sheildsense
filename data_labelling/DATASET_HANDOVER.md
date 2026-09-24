# ShieldSense Dataset Handover

## Handover From

Bijay Bahadur Chhetri  
Integration, Documentation & QA Lead

## Handover To

Jaskaran Singh  
Data & Labelling Lead

## Dataset

File: `data/shieldsense_messages.csv`

The current ShieldSense dataset contains 180 synthetic messages.

## Dataset Summary

| Risk Level | Number of Messages |
|---|---:|
| Red | 60 |
| Amber | 60 |
| Green | 60 |
| **Total** | **180** |

## Dataset Checks

The dataset generation and verification scripts were run successfully.

- Total messages: 180
- Unique messages: 180
- Duplicate messages: 0
- Empty messages: 0
- Required columns: Passed
- Risk levels: Red, Amber and Green
- Classes are balanced at 60 messages per risk level.

## Hard Negatives

Additional legitimate-style messages were included to provide harder examples for testing. These include:

- Bank statements
- Payment confirmations
- Delivery tracking
- Parcel updates
- ACU student notifications
- ACU tuition payment receipts
- Banking account information
- Scheduled payments

These examples are synthetic legitimate-style examples and should be reviewed and labelled according to the agreed taxonomy.

## Handover Responsibility

The dataset is now handed back to the Data & Labelling Lead for:

1. Reviewing the messages against the agreed risk taxonomy.
2. Checking label consistency.
3. Completing any required corrections.
4. Maintaining the dataset and labelling documentation.
5. Preparing the final dataset for model development and evaluation.

## Supporting Source Code

Dataset generation:

`src/create_dataset.py`

Dataset verification:

`src/verify_dataset.py`

## QA Note

The dataset has been checked for duplicates, empty messages and class balance. Further labelling review remains the responsibility of the Data & Labelling Lead.

**Handover status: Ready for Jaskaran's review.**
