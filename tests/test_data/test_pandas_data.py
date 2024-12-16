import os

import pandas as pd


def test_pandas_data_columns():
    data_path = "data/cleaned_data.csv"
    assert os.path.exists(data_path), f"{data_path} が存在しません。"
    df = pd.read_csv(data_path)
    expected_cols = ["id", "feature1", "feature2", "target"]
    assert list(df.columns) == expected_cols, "列名が想定と異なります"


def test_pandas_no_nulls():
    df = pd.read_csv("data/cleaned_data.csv")
    assert not df.isnull().values.any(), "欠損値が存在します"
