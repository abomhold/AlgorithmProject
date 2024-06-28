import heapq
import timeit
import typing
from heapq import heappush, heappop

import graph

N: int = 5
node_array: list[graph.Point] = graph.generate_points(N)
heap: list[float] = []
table: dict[float, list[graph.Point]] = {}
p: list[int] = list(range(0, N + 1))


def swap(x: int, y: int) -> None:
    temp = node_array[x]
    node_array[x] = node_array[y]
    node_array[y] = temp


def solve() -> None:
    index: int = 1
    count: int = 0
    while index < N:
        p[index] -= 1
        j: int = (index % 2) * p[index]
        swap(j, index)
        count += 1
        distance = graph.path_distance(node_array)
        heappush(heap, distance)
        table[distance] = node_array
        index = 1
        while p[index] == 0:
            p[index] = index
            index += 1
    distance = heappop(heap)
    path = table[distance]
    print(path)
    print(distance)


if __name__ == '__main__':
    min_time: float = 10.0  # could be any > expected
    for i in range(1):
        start_time = timeit.default_timer()
        solve()
        end_time = timeit.default_timer()
        min_time = min(min_time, end_time - start_time)
    print(min_time)
