import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

diff_dict = {}

data = pd.read_csv("data/comparison.csv")
print(data.columns)
data = data.replace(np.inf, np.nan).replace(-np.inf, np.nan).dropna()

for index, row in data.iterrows():
    print(True if row['chris_distance'] > row['nn_dist'] else False)
