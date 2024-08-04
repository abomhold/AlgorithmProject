import multiprocessing
import time
from typing import Generator
import math
import matplotlib.pyplot as plt
import src.chris as ch
import src.held_karp as hp
import src.nearest as nn
from src import graph
from src.graph import Point, generate_points
import numpy as np
import pandas as pd

brute: list[int] = [21, 88, 445, 2676, 18739, 149920, 1349289, 13492900, 148421911, 1781062944]
x_values: list[int] = [x for x in range(4, 14)]
min_nodes: int = 4
max_nodes: int = 14
num_runs: int = 50


def generate_plot() -> None:
    data = pd.read_csv("../data/runtime_comparison.csv")
    data = data.replace(np.inf, np.nan).replace(-np.inf, np.nan).dropna()

    fig, ax = plt.subplots()

    plt.plot(x_values, brute, label='Brute Force', marker='o')
    plt.plot(data['nodes'], data['hd_calc'], label='Held-Karp', marker='o')
    plt.plot(data['nodes'], data['ch_calc'], label='Christofides', marker='s')
    plt.plot(data['nodes'], data['nn_calc'], label='Nearest Neighbor', marker='^')
    plt.plot(data['nodes'], data['nodes'] ** 2, label='n²', color='grey', linestyle='--')
    plt.plot(data['nodes'], data['nodes'] ** 3, label='n³', color='grey', linestyle=':')
    plt.plot(data['nodes'], 2 ** data['nodes'], label='2ⁿ', color='grey', linestyle='-.')

    fig.set_size_inches(12, 8)
    plt.legend()
    plt.grid(True)
    plt.yscale('log', base=2)

    ax.set(
        xlabel='Number of Nodes',
        ylabel='Number of Calculations',
        title='Number of Calculations vs. Number of Nodes (n = 100 runs)',
        xmargin=.03,
        xticks=[x for x in range(min_nodes, max_nodes)]

    )
    plt.savefig('data/runtime_comparison_plot.png')
    plt.show()
    plt.close()


def held_karp(path) -> tuple[float, list[Point]]:
    return hp.solve(path)


def christofides(path) -> tuple[float, list[Point]]:
    return ch.solve(path)


def nearest_neighbor(path) -> tuple[float, list[Point]]:
    return nn.solve(path)


def path_generator(limit: int) -> Generator[list[Point], None, None]:
    for i in range(4, limit):
        yield generate_points(i)


def run_algorithm(func, path):
    start_time = time.perf_counter()
    graph.calculations = 0
    (distance, _) = func(path.copy())
    duration = time.perf_counter() - start_time
    return graph.calculations, duration


def runtime_comparison() -> None:
    results = []

    for num_nodes in range(min_nodes, max_nodes):
        for func in [held_karp, christofides, nearest_neighbor]:
            worst_calculations = 0
            total_duration = 0

            for _ in range(num_runs):
                path = generate_points(num_nodes)
                calculations, duration = run_algorithm(func, path)
                worst_calculations = max(worst_calculations, calculations)
                total_duration += duration

            avg_duration = total_duration / num_runs
            results.append((num_nodes, func.__name__, worst_calculations, avg_duration))

    with open("../data/runtime_comparison.csv", "w") as f:
        f.write("nodes,hd_calc,hd_duration,ch_calc,ch_duration,nn_calc,nn_duration\n")
        # Write results to csv and convert algorithm name to multi-column format
        for (nodes, algorithm, worst_calculations, avg_duration) in results:
            if algorithm == 'held_karp':
                f.write(f"{nodes},")
                f.write(f"{worst_calculations},{avg_duration},")
            elif algorithm == 'christofides':
                f.write(f"{worst_calculations},{avg_duration},")
            elif algorithm == 'nearest_neighbor':
                f.write(f"{worst_calculations},{avg_duration}\n")


if __name__ == '__main__':
    # runtime_comparison()
    generate_plot()
