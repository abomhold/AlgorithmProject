import multiprocessing
import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from src import chris as ch
from src import held_karp as hp
from src import nearest as nn
from src.graph import Point

with open("../data/acc_test_paths.txt", "r") as f:
    PATHS = [eval(line) for line in f]

node_count = len(PATHS[0])
number_of_paths = len(PATHS)


def held_karp(index: int) -> tuple[float, list[Point]]:
    return hp.solve(PATHS[index])


def christofides(index: int) -> tuple[float, list[Point]]:
    return ch.solve(PATHS[index])


def christofides_nx(index: int) -> tuple[float, list[Point]]:
    return ch.solve_nx(PATHS[index])


def nearest_neighbor(index: int) -> tuple[float, list[Point]]:
    return nn.solve(PATHS[index])


def multi_proc_loop():
    with multiprocessing.Pool() as pool:
        chris_results = pool.map(christofides, range(number_of_paths))
        held_results = pool.map(held_karp, range(number_of_paths))
        nearest_results = pool.map(nearest_neighbor, range(number_of_paths))
        christofides_nx_results = pool.map(christofides_nx, range(number_of_paths))
    return chris_results, held_results, nearest_results, christofides_nx_results


def run_accuracy_test():
    start_time = time.time()
    chris_results, held_results, nearest_results, chris_nx_results = multi_proc_loop()
    duration = time.time() - start_time
    with open("../data/accuracy_comparison.csv", "w") as f:
        f.write("id,ch_dist,ch_nx_dist,hk_dist,nn_dist\n")

        for solution in range(number_of_paths):
            f.write(f"{solution + 1},"  # id    
                    f"{chris_results[solution][0]},"  # chris_dist
                    f"{chris_nx_results[solution][0]},"  # chris_nx_dist
                    f"{held_results[solution][0]},"  # held_dist
                    f"{nearest_results[solution][0]}\n"  # nn_dist
                    )
        print(f"Duration {duration} seconds")


def plot_accuracy() -> None:
    data = pd.read_csv("../data/accuracy_comparison.csv")
    print(data.columns)
    d = np.array(data["hk_dist"])
    c = np.array(data["ch_nx_dist"])
    b = np.array(data["ch_dist"])
    a = np.array(data["nn_dist"])
    # print(a, b, c, d)
    fig, ax = plt.subplots()
    ax.boxplot([a, b, c, d],
               tick_labels=["NearestNeighbor", "Chrisofides", "Chrisofides_nx", "HeldKarp"],
               vert=False,
               widths=0.3,
               showfliers=False
               )
    ax.set(
        xlabel="Shortest Path Length",
        title="Comparison of Held-Karp and Chris' Solutions (n = 1000 runs)",

    )
    fig.set_size_inches(12, 8)
    plt.grid(True)
    plt.savefig('data/accuracy_comparison_plot.png')
    plt.show()
    plt.close()


if __name__ == "__main__":
    # run_accuracy_test()
    plot_accuracy()
