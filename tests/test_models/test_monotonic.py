from src.models import SimpleModel


def test_model_monotonic_increase():
    model = SimpleModel()
    inputs = list(range(1, 101))
    outputs = [model.predict(i) for i in inputs]
    assert all(
        x <= y for x, y in zip(outputs, outputs[1:])
    ), "モデル出力が単調増加になっていません"
