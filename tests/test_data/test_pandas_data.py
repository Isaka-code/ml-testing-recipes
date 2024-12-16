import os

import pandas as pd
import pytest

CSV_PATH = "data/cleaned_data.csv"


@pytest.mark.skipif(not os.path.exists(CSV_PATH), reason="data file not found")
def test_pandas_data_columns():
    df = pd.read_csv(CSV_PATH)
    expected_cols = ["id", "feature1", "feature2", "target"]
    assert list(df.columns) == expected_cols, "列名が想定と異なります"


@pytest.mark.skipif(not os.path.exists(CSV_PATH), reason="data file not found")
def test_pandas_no_nulls():
    df = pd.read_csv(CSV_PATH)
    assert not df.isnull().values.any(), "欠損値が存在します"
