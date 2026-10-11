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
| Environment | Jupyter Notebook, venv, requirements.txt |
| Version control | Git, GitHub (README with the 5-part structure) |
| Statistics | A/B test design: hypothesis test, sample size (scipy / statsmodels) |

# Approach

* Baseline: [logistic regression]
* Classical ML: [Random Forest, XGBoost, tuning, cross-validation]
* Neural network: [PyTorch MLP: architecture, regularization, early stopping]
* Validation: [stratified split / CV, fixed seed]
* Metric choice and why: [ROC-AUC, recall at threshold]
* Threshold selection: [tied to business cost]
* Interpretation: [feature importance / SHAP]
* A/B test design (retention offer): [control vs treatment groups, success metric, sample size / power, hypothesis test, decision rule]. Design only, no real experiment data

# Results

* Best model vs baseline: [metric values]
* Business effect (simulated): [e.g. customers saved per 1000 contacted, assumptions stated]
* Limitations: [what the simulation does not prove]
* A/B test design: [how the effect of the retention offer would be measured; assumptions]

# Takeaway

* Which model won and why: [...]
* Next step: [e.g. deploy via FastAPI + Docker, monitor drift (Project 3)]