import numpy as np

from src.data_processing import standardize


def test_standardize():
    data = np.random.rand(1000)
    transformed = standardize(data)
    assert abs(np.mean(transformed)) < 1e-7, "平均が0に近くありません"
    assert abs(np.std(transformed) - 1) < 1e-7, "標準偏差が1になっていません"
