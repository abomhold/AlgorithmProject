import multiprocessing
import time

from src import chris as ch
from src import held_karp as hp

with open("data/paths.txt", "r") as f:
    PATHS = [eval(line) for line in f]

node_count = len(PATHS[0])
number_of_paths = len(PATHS)


def held_karp(index):
    return hp.solve(PATHS[index])


def christofides(index):
    return ch.solve(PATHS[index])


def multi_proc_loop():
    with multiprocessing.Pool() as pool:
        chris_results = pool.map(christofides, range(number_of_paths))
        held_results = pool.map(held_karp, range(number_of_paths))
    return chris_results, held_results


if __name__ == "__main__":
    start_time = time.time()
    result = multi_proc_loop()
    duration = time.time() - start_time

    with open("data/comparison.csv", "w") as f:
        f.write("id,chris_distance,held_distance,chris_path,held_path,distance_diff,node_diff \n")
        # Format as CSV
        for i in range(number_of_paths):
            f.write(f"{i + 1},"  # id    
                    f"{result[0][i][0]},"  # chris_dist
                    f"{result[1][i][0]},"  # held_dist 
                    f"\"{result[0][i][1]}\","  # chris_path
                    f"\"{result[1][i][1]}\","  # held_path
                    f"{abs(result[0][i][0] - result[1][i][0])},"
                    f"{abs(len(result[0][i][1]) - len(result[1][i][1]))} \n")
        # Append runtime
        # f.write(f"Duration {duration} seconds")
