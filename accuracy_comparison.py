import multiprocessing
import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from src import chris as ch
from src import held_karp as hp
from src import nearest as nn

with open("data/paths.txt", "r") as f:
    PATHS = [eval(line) for line in f]

node_count = len(PATHS[0])
number_of_paths = len(PATHS)


def held_karp(index):
    return hp.solve(PATHS[index])


def christofides(index):
    return ch.solve(PATHS[index])


def nearest_neighbor(index):
    return nn.solve(PATHS[index])


def multi_proc_loop():
    with multiprocessing.Pool() as pool:
        chris_results = pool.map(christofides, range(number_of_paths))
        held_results = pool.map(held_karp, range(number_of_paths))
        nearest_results = pool.map(nearest_neighbor, range(number_of_paths))
    return chris_results, held_results, nearest_results


def run_accuracy_test():
    start_time = time.time()
    chris_results, held_results, nearest_results = multi_proc_loop()
    duration = time.time() - start_time
    with open("data/comparison.csv", "w") as f:
        f.write("id,chris_distance,held_distance,nn_dist,chris_path,held_path,nn_path,chris_diff,nn_diff\n")
        for solution in range(number_of_paths):
            f.write(f"{solution + 1},"  # id    
                    f"{chris_results[solution][0]},"  # chris_dist
                    f"{held_results[solution][0]},"  # held_dist
                    f"{nearest_results[solution][0]},"  # nn_dist
                    f"\"{chris_results[solution][1]}\","  # chris_path
                    f"\"{held_results[solution][1]}\","  # held_path
                    f"\"{nearest_results[solution][1]}\","  # nn_path
                    f"{chris_results[solution][0] - held_results[solution][0]},"  # chris_held_diff
                    f"{nearest_results[solution][0] - held_results[solution][0]} \n"  # nn_held_diff
                    )
        # Append runtime
        f.write(f"Duration {duration} seconds")


def plot_accuracy() -> None:
    data = pd.read_csv("data/comparison.csv")
    data = data.replace(np.inf, np.nan).replace(-np.inf, np.nan).dropna()
    x, y, z = np.array(data["held_distance"]), np.array(data["chris_distance"]), np.array(data["nn_dist"])
    fig, ax = plt.subplots()
    ax.boxplot([x, y, z],
               labels=["HeldKemp", "Chris", "Nearest"],
               vert=False,
               widths=0.3,
               showfliers=False
               )
    ax.set(
        xlabel="Shortest Path Length",
        title="Comparison of Held-Karp and Chris' Solutions",
    )
    plt.show()


if __name__ == "__main__":
    run_accuracy_test()
    plot_accuracy()