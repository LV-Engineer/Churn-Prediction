import numpy as np

def expected_profit(y_true, proba, threshold, *, value, cost, save_rate):
    contact = proba >= threshold
    tp = (contact & (y_true == 1)).sum()
    return tp * save_rate * value - contact.sum() * cost