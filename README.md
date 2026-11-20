# MLOps Project --- Group G178

## Project Details
- **Group ID**: G178
- **Problem ID**: MP262 --- ATM Cash Demand (Surat)
- **Client**: Surat Cooperative Bank
- **Target Variable**: `withdrawal_thousand_rs` (Regression, Evaluation Metric: MAE)
- **Faculty**: Richa Sharma (Batch 47)

## Team Members
| Enrolment No. | Name | GitHub / Role |
|---|---|---|
| S24CSEU1832 | Harshit Ranjan | Data / MLOps |
| S24CSEU0097 | Uday Singh Pratap | Team Member |
| S24CSEU1852 | Prithul Jaiswal | Team Member |
| S24CSEU1855 | Yashvardhan Singh | Team Member |

## Project Layout
```
Mlops-project/
├── data/
│   └── raw/
│       ├── train.csv.dvc          # DVC tracking for training data
│       ├── later.csv.dvc          # DVC tracking for later data
│       └── holdout_features.csv   # Features for holdout prediction
├── docs/                          # Documentation, GROUP.md, PROBLEM.md, HANDBOOK.md
├── reports/
│   └── findings.yaml              # Findings & audit report
├── src/                           # Source code
├── .dvc/                          # DVC internal configuration
├── .dvcignore
├── .gitignore
├── requirements.txt
└── README.md
```

## Stage 1 Setup
- Raw datasets placed in `data/raw/` (`train.csv`, `later.csv`, `holdout_features.csv`).
- `train.csv` and `later.csv` are tracked with DVC.
- `holdout_features.csv` is tracked with Git.
