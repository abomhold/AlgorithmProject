import itertools
import timeit
from heapq import heappush, heappop

from graph import calculate_distance, generate_points, Point

N: int = 5
node_array: list[Point] = generate_points(N)


def permutations(arr: list[Point]) -> list[list[Point]]:
    if len(arr) < 2:
        return [arr]
    perm_list = []
    for j in arr:
        remaining_elements = [x for x in arr if x != j]
        for perm in permutations(remaining_elements):
            perm_list.append([j] + perm)
    return perm_list

def solve(arr: list[Point]) -> tuple[list[Point], float]:
    perm_dist = []
    perm_dict = {}
    for perm in itertools.permutations(arr):
        cost = calculate_distance(list(perm))
        heappush(perm_dist, cost)
        perm_dict[cost] = list(perm)
    best = heappop(perm_dist)
    return perm_dict[best], best

# def solve(arr: list[Point]) -> tuple[list[Point], float]:
#     perms = permutations(arr)
#     perm_dist: list[float] = []
#     perm_dict = {}
#     for perm in perms:
#         distance = path_distance(perm)
#         heappush(perm_dist, distance)
#         perm_dict[distance] = perm
#     best = heappop(perm_dist)
#     return perm_dict[best], best


if __name__ == '__main__':
    min_time: float = float('inf')
    for i in range(1):
        start_time = timeit.default_timer()
        shortest = solve(node_array)
        print(shortest)
        end_time = timeit.default_timer()
        min_time = min(min_time, end_time - start_time)
    print(min_time)
