import os

import numpy as np
import pandas as pd

os.makedirs("data", exist_ok=True)

# Numpyデータ生成 (1000 x 20)
processed_data = np.random.rand(1000, 20)
np.save("data/processed_data.npy", processed_data)

# Pandasデータ生成
df = pd.DataFrame(
    {
        "id": range(1000),
        "feature1": np.random.randn(1000),
        "feature2": np.random.randn(1000),
        "target": np.random.randint(0, 2, size=1000),
    }
)
df.to_csv("data/cleaned_data.csv", index=False)

print("Data generated successfully.")
