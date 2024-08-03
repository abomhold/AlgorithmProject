import csv
from typing import Generator

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

diff_dict = {}

data = pd.read_csv("data/comparison.csv")
print(data)
data = data.replace(np.inf, np.nan).replace(-np.inf, np.nan).dropna()
# summary = data['distance_diff'].describe()
# print(summary)

x = np.array(data["held_distance"])
y = np.array(data["chris_distance"])
z = np.array(data["nn_dist"])
m, b = np.polyfit(x, y, 1)

## Box Plot
fig, ax = plt.subplots()

ax.boxplot([x, y, z],
           labels=["HK", "Chris", "NN"],
           vert=False,
           widths=0.3,
           showfliers=False
           )

ax.set(
    xlabel="Shortest Path Length",
    title="Comparison of Held-Karp and Chris' Solutions",
)

plt.show()
