Experiment Log

One row per experiment. Use the same validation split everywhere.

| # | Model | Key settings | Validation | ROC-AUC | Recall @ threshold | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Dummy classifier | `strategy="prior"` | 5-fold stratified CV on train (80/20 split, seed 42) | 0.500 | 0.000 @ 0.5 | Floor: predicts the class prior for everyone, never flags churn. Precision 0.000 (undefined, no positive predictions) |
| 2 | Logistic regression | `max_iter=1000`; StandardScaler on Tenure Months and Monthly Charges, one-hot on categoricals (`drop="if_binary"`, `handle_unknown="ignore"`) | 5-fold stratified CV on train (80/20 split, seed 42) | 0.858 | 0.575 @ 0.5 | Baseline. Precision 0.665 @ 0.5. Threshold is the default 0.5, not yet chosen by business cost |
| 3 | Random Forest | `n_estimators=300`, other params default; same preprocessing | 5-fold stratified CV on train (80/20 split, seed 42) | 0.830 | 0.497 @ 0.5 | Precision 0.630 @ 0.5. Not tuned |
| 4 | XGBoost (`learning_rate=0.05`, `max_depth=4`) | `n_estimators=300`, `learning_rate=0.05`, `max_depth=4`; same preprocessing | 5-fold stratified CV on train (80/20 split, seed 42) | 0.858 | 0.553 @ 0.5 | Precision 0.663 @ 0.5. Matches logistic regression on ROC-AUC. Fold-to-fold spread not yet checked, so no model is declared better yet |
| 5 | Random Forest (tuned) | `RandomizedSearchCV`, 30 iterations, scoring ROC-AUC. Best: `max_depth=10`, `min_samples_leaf=14`, `max_features=0.5`, `n_estimators=280` | 5-fold stratified CV on train (80/20 split, seed 42) | 0.861 | not computed | `best_score_` is the maximum over 30 trials, so it is slightly optimistic. Recall and precision were not computed for the tuned model |
| 6 | XGBoost (tuned) | `RandomizedSearchCV`, 30 iterations, scoring ROC-AUC. Best: `max_depth=2`, `learning_rate=0.067`, `n_estimators=180`, `min_child_weight=8`, `subsample=0.71`, `colsample_bytree=0.80` | 5-fold stratified CV on train (80/20 split, seed 42) | 0.865 | not computed | `best_score_` is the maximum over 30 trials, so it is slightly optimistic. `max_depth=2` is the lower edge of the search range. Differences between 0.858, 0.861 and 0.865 are small, no model is declared better yet |
| 7 | PyTorch MLP | Hidden layers (64, 32), ReLU, dropout 0.3; Adam `lr=1e-3`, `weight_decay=1e-4`, batch 128; early stopping with `patience=15` on a 20% validation split of each fold's training part; same preprocessing | 5-fold stratified CV on train (same folds as above, seed 42) | 0.857 | 0.552 @ 0.5 | Precision 0.670 @ 0.5. ROC-AUC per fold 0.840 to 0.871 (std about 0.012); early stopping epochs 12 to 43. Not tuned. Practically equal to logistic regression and tuned trees, differences are smaller than fold-to-fold spread |
| 8 | Logistic regression, final evaluation on test | Fit on the whole train set; threshold 0.05 chosen by expected profit on out-of-fold probabilities of train (V=890, c=20, p=0.3, simulated) | Held-out test set (20%, 1409 customers), evaluated once | 0.847 | 0.987 @ 0.05 | Precision 0.369 @ 0.05, 71.0% of customers contacted. Expected profit per 1000 customers (simulated): nobody 0, everyone 50872, model 55730 (about +9.5% over contacting everyone). Single estimate on a small test set, no confidence interval |

# Conclusions

[What worked, what did not, what to try next]