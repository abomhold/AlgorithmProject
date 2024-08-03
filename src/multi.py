import multiprocessing
import time

from src import chris as ch
from src import held_karp as hp
from src import nearest as nn

with open("../data/paths.txt", "r") as f:
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


if __name__ == "__main__":
    start_time = time.time()
    result = multi_proc_loop()
    duration = time.time() - start_time

    with open("../data/comparison.csv", "w") as f:
        f.write("id,chris_distance,held_distance,nn_dist,chris_path,held_path,nn_path,chris_diff,nn_diff\n")
        # Format as CSV
        for i in range(number_of_paths):
            f.write(f"{i + 1},"  # id    
                    f"{result[0][i][0]},"  # chris_dist
                    f"{result[1][i][0]},"  # held_dist
                    f"{result[2][i][0]},"  # nn_dist
                    f"\"{result[0][i][1]}\","  # chris_path
                    f"\"{result[1][i][1]}\","  # held_path
                    f"\"{result[2][i][1]}\","  # nn_path
                    f"{result[0][i][0] - result[1][i][0]},"  # chris_held_diff
                    f"{result[2][i][0] - result[1][i][0]} \n"  # nn_held_diff
                    )
        # Append runtime
        f.write(f"Duration {duration} seconds")
