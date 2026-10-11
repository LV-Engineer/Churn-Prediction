Work Plan and Checklist

|  |  |  |  |
| --- | --- | --- | --- |
| **Step** | **Task** | **Done?** | **Notes** |
| 1 | Choose dataset, define business problem and cost assumptions | [x] | IBM Telco; cost assumptions are simulated |
| 2 | EDA: distributions, missing values, class balance, leakage check | [x] | `notebooks/01_eda.ipynb` |
| 3 | Preprocessing pipeline (scikit-learn Pipeline) | [x] | `src/churn/features.py` |
| 4 | Baseline: logistic regression | [x] | `notebooks/02_modeling.ipynb` |
| 5 | Random Forest and XGBoost, tuning, cross-validation | [x] | `notebooks/02_modeling.ipynb` |
| 6 | PyTorch MLP and comparison with classical models | [x] | `src/churn/models.py`; equal to logistic regression within noise |
| 7 | Threshold selection tied to business cost | [x] | `notebooks/03_threshold_business.ipynb`, threshold 0.05 |
| 8 | Interpretation (feature importance / SHAP) | [x] | `notebooks/04_interpretation.ipynb`; SHAP not used |
| 9 | Design the A/B test for the retention offer (groups, metric, sample size, hypothesis test) and describe it in the brief | [x] | `notebooks/05_ab_test_design.ipynb` |
| 10 | Clean notebook, README with the 5-part structure, requirements, seeds | [ ] |  |
| 11 | Push to GitHub, pin the repo, update CV, Djinni, DOU, LinkedIn | [ ] |  |