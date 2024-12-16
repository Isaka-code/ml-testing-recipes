import os

import numpy as np
import pytest

DATA_PATH = "data/processed_data.npy"


@pytest.mark.skipif(not os.path.exists(DATA_PATH), reason="data file not found")
def test_numpy_data_shape():
    data = np.load(DATA_PATH)
    assert data.shape == (1000, 20), "入力データのshapeが想定と異なります"


@pytest.mark.skipif(not os.path.exists(DATA_PATH), reason="data file not found")
def test_numpy_data_no_nan():
    data = np.load(DATA_PATH)
    assert not np.isnan(data).any(), "NaNが含まれています"
