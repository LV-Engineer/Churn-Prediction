from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW_PATH = ROOT / "data" / "raw" / "Telco_customer_churn.csv"

SEED = 42
TARGET = "Churn Value"
DROP_COLS = ["Count", "Country", "State", "City", "Lat Long", "Churn Label", "Churn Score", "Churn Reason", "Zip Code", "Latitude", "Longitude"]
CAT_COLS = [
    "Gender", "Senior Citizen", "Partner", "Dependents",
    "Phone Service", "Multiple Lines", "Internet Service",
    "Online Security", "Online Backup", "Device Protection",
    "Tech Support", "Streaming TV", "Streaming Movies",
    "Contract", "Paperless Billing", "Payment Method",
]

NOT_FEATURES = ["CLTV", "Total Charges"]