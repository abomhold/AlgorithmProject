import heapq
import timeit
from typing import Any, List
from heapq import heappush, heappop, heapify
from graph import Point, path_distance
import graph

N: int = 5
node_array: list[graph.Point] = graph.generate_points(N)

def permutations(arr: list[Any]) -> list[list]:
    if len(arr) < 2:
        return [arr]
    perm_list = []
    for i in arr:
        remaining_elements = [x for x in arr if x != i]
        for perm in permutations(remaining_elements):
            perm_list.append([i] + perm)
    return perm_list


def solve() -> tuple[list, float]:
    perms = permutations(node_array)
    perm_dist: list[Any] = []
    perm_dict = {}
    for perm in perms:
        distance = path_distance(perm)
        heappush(perm_dist, distance)
        perm_dict[distance] = perm
    best = heappop(perm_dist)
    return perm_dict[best], best


if __name__ == '__main__':
    min_time: float = 10.0  # could be any > expected
    for i in range(1):
        start_time = timeit.default_timer()
        shortest = solve()
        print(shortest)
        end_time = timeit.default_timer()
        min_time = min(min_time, end_time - start_time)
    print(min_time)

# def solve() -> None:
#     index: int = 1
#     count: int = 0
#     while index < N:
#         p[index] -= 1
#         j: int = (index % 2) * p[index]
#         swap(j, index)
#         count += 1
#         distance = graph.path_distance(node_array)
#         heappush(heap, distance)
#         table[distance] = node_array
#         index = 1
#         while p[index] == 0:
#             p[index] = index
#             index += 1
#     distance = heappop(heap)
#     path = table[distance]
#     print(path)
#     print(distance)
# def quick_perm(arr: list[Point], perm_dist, perm_dict) -> list[list[Point]]:
#     if len(arr) < 2:
#         return [arr]
#     perm_list = []
#     for i in arr:
#         remaining_elements = [x for x in arr if x != i]
#         permutes = quick_perm(remaining_elements, perm_dist, perm_dict)
#         for perm in permutes:
#             distance = path_distance([i] + perm)
#             heappush(perm_dist, distance)
#             perm_dict[distance] = [i] + perm
#             perm_list.append([i] + perm)
#             # perm_list.append([i] + perm)
#     return perm_list
