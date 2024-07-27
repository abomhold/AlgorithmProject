import multiprocessing
import pathlib
import time
from src import graph as graph
from src import held_karp as hp
from src import chris as ch

with open("data/paths.txt", "r") as f:
    PATHS = [eval(line) for line in f]

node_count = len(PATHS[0])
number_of_paths = len(PATHS)


def held_karp(index):
    return hp.solve(PATHS[index])

def christofides(index):
    return ch.solve(PATHS[index])

# def brute_force(path_array):
#     return bf.solve(path_array)

# def brute_force(_):


def multi_loop():
    with multiprocessing.Pool() as pool:
        results = pool.map(held_karp, range(number_of_paths))
    return results


if __name__ == "__main__":
    start_time = time.time()
    paths = multi_loop()
    duration = time.time() - start_time

    for path in paths:
        print(f"Path: {path[1]}, Distance: {path[0]}, Calculations: {path[2]}")

    print(f"Duration {duration} seconds")

# for path in PATHS:
#     print(f"Path: {path}")
#     result = hp.solve(path)
#     print(f"Path: {result[1]}, Distance: {result[0]}, Calculations: {result[2]}")
