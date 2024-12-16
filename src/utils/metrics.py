def custom_metric(y_true, y_pred):
    correct = sum(t == p for t, p in zip(y_true, y_pred))
    return correct / len(y_true) if len(y_true) > 0 else 0.0
