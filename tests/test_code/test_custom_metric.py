from src.utils.metrics import custom_metric


def test_custom_metric():
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 0, 0]
    score = custom_metric(y_true, y_pred)
    expected_score = 0.75
    assert score == expected_score, f"メトリクス値が想定外です: {score}"
