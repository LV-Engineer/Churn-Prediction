Project 1: Customer Churn Prediction

Repo: https://github.com/LV-Engineer/Churn-Prediction

# Business problem

* Who has the problem: the retention team of a telecom operator.
* Why it matters: every customer who leaves is lost revenue, while a retention offer costs money. Contacting everyone is too expensive, contacting nobody loses customers.
* Decision the model supports: which customers get a retention offer.
* Cost assumptions (simulated, not from real data):
  * loss if a customer leaves: 890 (about 12 months of the average monthly charge of churned customers, 74.4);
  * cost of one offer: 20;
  * share of at-risk customers saved by an offer: 30%.

  These numbers are only used to choose the decision threshold and to estimate the effect. They will be varied to show sensitivity.

# Data

* Source: IBM Telco Customer Churn (extended version), Kaggle: https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset. Details and license note: `data/README.md`.
* Size: 7043 rows x 33 columns in the raw file, 21 after cleaning.
* Target: `Churn Value` (1 = left), class balance: 26.5% churned.
* Key features: contract type, tenure, monthly charges, payment method, internet service, support services.
* Data issues: 11 blank `Total Charges` values (new customers, set to 0); leakage columns removed (`Churn Label`, `Churn Score`, `Churn Reason`); `Total Charges` and `CLTV` kept out of model input; class imbalance (26.5%).

# Tech stack

|  |  |
| --- | --- |
| Area | Tools |
| Language | Python 3.11+ |
| Data and EDA | pandas, NumPy, Matplotlib, Seaborn |
| Classical ML | scikit-learn (Pipeline, LogisticRegression, RandomForest, cross-validation, tuning), XGBoost |
| Neural network | PyTorch (MLP) |
| Interpretation | feature importance, SHAP (optional) |
| Environment | Jupyter Notebook, uv, pyproject.toml, uv.lock |
| Version control | Git, GitHub (README with the 5-part structure) |
| Statistics | A/B test design: hypothesis test, sample size (scipy / statsmodels) |

# Approach

* Baseline: logistic regression, compared with a dummy classifier (always predicts the class prior).
* Classical ML: Random Forest and XGBoost, tuned with `RandomizedSearchCV` (30 iterations) on the same cross-validation folds.
* Neural network: PyTorch MLP, hidden layers (64, 32), ReLU, dropout 0.3, Adam with weight decay, early stopping on a validation split of each fold's training part.
* Validation: stratified 80/20 train/test split (seed 42); 5-fold stratified cross-validation on train for all models; the test set is used once, at the end.
* Metric choice and why: ROC-AUC to compare models (does not depend on the threshold and is not distorted by the 26.5% class share); recall and precision to see the trade-off at a threshold; expected profit to make the decision. Accuracy is not used: always predicting "stayed" already gives about 73%.
* Threshold selection: chosen by expected profit on out-of-fold probabilities of train, using the simulated cost assumptions; break-even point is c / (p x V) = 20 / (0.3 x 890), about 0.075.
* Interpretation: logistic regression coefficients (log-odds and odds ratios, numeric features scaled) and permutation importance on the test set (drop in ROC-AUC when one original column is shuffled). SHAP was not used.
* A/B test design (retention offer): design only, no real experiment data.
  * Question: does the retention offer lower churn among the customers the model flags (probability above the threshold 0.05, about 71% of customers)?
  * Groups: flagged customers are randomly split 50/50 at customer level into treatment (receives the offer) and control (receives nothing).
  * Success metric: share of customers who churn during the observation period (one quarter, as in the dataset).
  * Hypothesis test: two-sided test of two proportions, significance level 0.05, power 0.8. H0: churn share is the same in both groups.
  * Effect sizes (simulated): baseline churn among flagged customers is about 36.9% (precision on the test set). Under the assumed 30% save rate it would fall to about 25.8% (11.1 percentage points). The break-even reduction is c / V = 20 / 890, about 2.25 percentage points.
  * Sample size per group (two-proportion test): about 272 to detect the assumed effect, about 1148 to detect half of it, about 7139 to detect the break-even effect.
  * Decision rule: roll the offer out only if the difference is statistically significant and the reduction in churn is at least the break-even 2.25 percentage points; a smaller significant effect does not cover the cost of the offer.

# Results

* Best model vs baseline: cross-validated ROC-AUC on train: dummy 0.500, logistic regression 0.858, MLP 0.857, tuned Random Forest 0.861, tuned XGBoost 0.865. The differences between the real models are smaller than the fold-to-fold spread (about 0.012), so no complex model is clearly better. Logistic regression is kept as the final model: simplest, explainable, equal quality. Test set: ROC-AUC 0.847.
* Key drivers of churn: five features carry almost all the signal (drop in test ROC-AUC when shuffled): `Tenure Months` (about 0.08), `Dependents` (0.04), `Contract` (0.03), `Internet Service` (0.03), `Monthly Charges` (0.02); the other features add 0.003 or less. Longer tenure, dependents and two-year contracts lower churn risk; month-to-month contracts and fiber optic raise it. These are associations in the data, not causes. Coefficients are effects given all other features and can look counter-intuitive (for example `Monthly Charges` is negative because the services priced into it are also in the model); the six "No internet service" columns duplicate `Internet Service = No` and share one coefficient.
* Business effect (simulated): with the assumptions above (loss 890, offer cost 20, 30% saved) and threshold 0.05, the model contacts 71% of customers (recall 0.987, precision 0.369). Expected profit per 1000 customers: contact nobody 0, contact everyone 50872, model 55730, about +9.5% over contacting everyone. The model matters more when the offer is expensive: in the sensitivity table the gain over the best simple strategy grows from about 8k (c=10, p=0.3) to about 143k (c=80, p=0.3) on the train set.
* Limitations: all money values are simulated from three assumed numbers, not from a real campaign; the true save rate can only be measured with an A/B test. The test set has 1409 customers, so the result is a single noisy estimate without a confidence interval. The class share and churn drivers come from a static dataset.
* A/B test design: the effect of the retention offer would be measured as the difference in churn share between the offered and the control group of flagged customers (see Approach). The 30% save rate used in the profit simulation is an assumption that only such a test can confirm. Detecting only the break-even effect would need about 7000 customers per group, more than the whole dataset, so a real test should be planned for a realistic effect size.

# Takeaway

* Which model won and why: [...]
* Next step: [e.g. deploy via FastAPI + Docker, monitor drift (Project 3)]