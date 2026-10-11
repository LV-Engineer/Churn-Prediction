Project 1: Customer Churn Prediction

Repo: [GitHub link]

# Business problem

* Who has the problem: [e.g. telecom retention team]
* Why it matters: [cost of losing a customer vs cost of a retention offer]
* Decision the model supports: [who gets a retention offer]

# Data

* Source: [IBM Telco Customer Churn, link]
* Size: [rows x columns]
* Target: [Churn Yes/No], class balance: [%]
* Key features: [contract type, tenure, charges, ...]
* Data issues: [missing values, leakage risks, imbalance]

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