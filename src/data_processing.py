import numpy as np


def convert_data(input_data):
    # 単純にlistに変換
    return list(input_data)


def standardize(data):
    data = np.array(data, dtype=float)
    mean = np.mean(data)
    std = np.std(data)
    return (data - mean) / (std if std != 0 else 1.0)
