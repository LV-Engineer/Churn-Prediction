Experiment Log

One row per experiment. Use the same validation split everywhere.

| # | Model | Key settings | Validation | ROC-AUC | Recall @ threshold | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Dummy classifier | `strategy="prior"` | 5-fold stratified CV on train (80/20 split, seed 42) | 0.500 | 0.000 @ 0.5 | Floor: predicts the class prior for everyone, never flags churn. Precision 0.000 (undefined, no positive predictions) |
| 2 | Logistic regression | `max_iter=1000`; StandardScaler on Tenure Months and Monthly Charges, one-hot on categoricals (`drop="if_binary"`, `handle_unknown="ignore"`) | 5-fold stratified CV on train (80/20 split, seed 42) | 0.858 | 0.575 @ 0.5 | Baseline. Precision 0.665 @ 0.5. Threshold is the default 0.5, not yet chosen by business cost |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |

# Conclusions

[What worked, what did not, what to try next]