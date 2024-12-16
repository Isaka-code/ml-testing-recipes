import os

import numpy as np


def test_numpy_data_shape():
    data_path = "data/processed_data.npy"
    assert os.path.exists(data_path), f"{data_path} が存在しません。"
    data = np.load(data_path)
    assert data.shape == (1000, 20), "入力データのshapeが想定と異なります"


def test_numpy_data_no_nan():
    data = np.load("data/processed_data.npy")
    assert not np.isnan(data).any(), "NaNが含まれています"
