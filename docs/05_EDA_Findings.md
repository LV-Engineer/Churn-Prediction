# EDA Findings

Notebook: `notebooks/01_eda.ipynb`. All numbers below come from the notebook outputs. They are descriptive, not causal.

## Data quality

- Raw file: 7043 rows x 33 columns, one row per customer. After cleaning: 21 columns.
- No duplicate rows. No missing values after the `Total Charges` fix.
- Target `Churn Value`: 26.5% churned (class 1), 73.5% stayed. A model that always predicts "stayed" gets ~73% accuracy, so accuracy is not a useful metric.
- `Total Charges` was read as text. 11 rows contain a blank string; all 11 have `Tenure Months = 0` (new customers who have not paid yet). Replaced with 0.

## Columns removed

| Column(s) | Reason |
| --- | --- |
| `Count`, `Country`, `State` | constants (one unique value) |
| `Lat Long` | duplicate of `Latitude` + `Longitude` |
| `Zip Code`, `City`, `Latitude`, `Longitude` | high cardinality (1652 zip codes, 1-5 customers each), little statistical power. A hypothesis to re-check later |
| `Churn Label` | same information as the target |
| `Churn Score` | computed by IBM SPSS Modeler (another model's prediction), leakage |
| `Churn Reason` | known only for customers who already left, leakage |
| `CustomerID` | identifier, kept as the index |

## Excluded from model input (kept in the data)

- `CLTV`: an estimate from another model, so it is not used as a feature. Kept for the business cost calculation. Single-feature ROC-AUC is 0.419 (weak, no sign of leakage, but the formula is unknown).
- `Total Charges`: almost equal to `Tenure Months x Monthly Charges` (correlation 0.9996) and correlated 0.83 with tenure. To be re-checked with tree models (with and without it) and logged in the experiment log.

## Numeric features

| Feature | Stayed (mean / median) | Churned (mean / median) | Single-feature ROC-AUC |
| --- | --- | --- | --- |
| `Tenure Months` | 37.6 / 38.0 | 18.0 / 10.0 | 0.26 |
| `Monthly Charges` | 61.3 / 64.4 | 74.4 / 79.6 | 0.621 |
| `Total Charges` | 2550 / 1680 | 1532 / 704 | 0.35 |

- Churn is concentrated among new customers (first months) and customers with a higher monthly charge.
- Correlation with the target: `Tenure Months` -0.35, `Monthly Charges` 0.19, `Total Charges` -0.20.

## Categorical features

Churn rate per value (baseline 26.5%) and Cramér's V with the target:

| Feature | Churn rate by value | Cramér's V |
| --- | --- | --- |
| `Contract` | Month-to-month 42.7%, One year 11.3%, Two year 2.8% | 0.410 |
| `Online Security` | No 41.8%, Yes 14.6%, No internet 7.4% | 0.347 |
| `Tech Support` | No 41.6%, Yes 15.2%, No internet 7.4% | 0.343 |
| `Internet Service` | Fiber optic 41.9%, DSL 19.0%, No 7.4% | 0.322 |
| `Payment Method` | Electronic check 45.3%, others 15.2-19.1% | 0.303 |
| `Online Backup` | No 39.9%, Yes 21.5% | 0.292 |
| `Device Protection` | No 39.1%, Yes 22.5% | 0.282 |
| `Dependents` | No 32.6%, Yes 6.5% | 0.249 |
| `Streaming TV`, `Streaming Movies` | about 30% with, 33.5% without | 0.231 |
| `Paperless Billing` | Yes 33.6%, No 16.3% | 0.192 |
| `Senior Citizen` | Yes 41.7%, No 23.6% | 0.151 |
| `Partner` | No 33.0%, Yes 19.7% | 0.150 |
| `Multiple Lines` | 25.0-28.6% | 0.040 |
| `Phone Service` | No 24.9%, Yes 26.7% | 0.012 |
| `Gender` | Female 26.9%, Male 26.2% | 0.009 |

- Strongest signals: contract type, payment method, internet service, and the absence of Online Security / Tech Support.
- `Gender`, `Phone Service` and `Multiple Lines` carry almost no signal. They stay for now; feature importance and regularization will decide later.
- "No internet service" gives the same 7.4% churn in all six service columns, and "No phone service" in `Multiple Lines` repeats `Phone Service = No`. These values duplicate `Internet Service` / `Phone Service`. To decide at the encoding step.

## Open decisions

- Merge "No internet service" / "No phone service" into "No", or keep them separate (affects encoding).
- Encode `Contract` as ordered (Month-to-month < One year < Two year) or one-hot.
- Re-check geography and `Total Charges` with models.
- Business cost assumptions (project brief, step 1) are not defined yet.

## What this means for the business (hypothesis)

The highest-risk profile in the data is a new customer on a month-to-month contract with fiber optic, electronic check, and no Tech Support / Online Security. A retention offer would be tested on this group first. This is an observation from the data, not proof that these factors cause churn.
