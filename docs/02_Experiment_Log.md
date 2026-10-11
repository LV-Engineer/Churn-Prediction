Experiment Log

One row per experiment. Use the same validation split everywhere.

| # | Model | Key settings | Validation | ROC-AUC | Recall @ threshold | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Dummy classifier | `strategy="prior"` | 5-fold stratified CV on train (80/20 split, seed 42) | 0.500 | 0.000 @ 0.5 | Floor: predicts the class prior for everyone, never flags churn. Precision 0.000 (undefined, no positive predictions) |
| 2 | Logistic regression | `max_iter=1000`; StandardScaler on Tenure Months and Monthly Charges, one-hot on categoricals (`drop="if_binary"`, `handle_unknown="ignore"`) | 5-fold stratified CV on train (80/20 split, seed 42) | 0.858 | 0.575 @ 0.5 | Baseline. Precision 0.665 @ 0.5. Threshold is the default 0.5, not yet chosen by business cost |
| 3 | Random Forest | `n_estimators=300`, other params default; same preprocessing | 5-fold stratified CV on train (80/20 split, seed 42) | 0.830 | 0.497 @ 0.5 | Precision 0.630 @ 0.5. Not tuned |
| 4 | XGBoost (default params) | `n_estimators=300`, learning rate and depth left at defaults (0.3, 6); same preprocessing | 5-fold stratified CV on train (80/20 split, seed 42) | 0.826 | 0.523 @ 0.5 | Precision 0.594 @ 0.5. Run by mistake without the intended learning rate / depth; kept to show the effect of hyperparameters |
| 5 | XGBoost (`learning_rate=0.05`, `max_depth=4`) | `n_estimators=300`, `learning_rate=0.05`, `max_depth=4`; same preprocessing | 5-fold stratified CV on train (80/20 split, seed 42) | 0.858 | 0.553 @ 0.5 | Precision 0.663 @ 0.5. Matches logistic regression on ROC-AUC. Fold-to-fold spread not yet checked, so no model is declared better yet |
| 6 |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |

# Conclusions

[What worked, what did not, what to try next]