from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from churn.config import CAT_COLS, MODEL_NUM_COLS


def build_preprocessor() -> ColumnTransformer:
    return ColumnTransformer([
        ("num", StandardScaler(), MODEL_NUM_COLS),
        ("cat", OneHotEncoder(drop="if_binary", handle_unknown="ignore"), CAT_COLS)
    ])