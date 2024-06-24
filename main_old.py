from heapq import heappush

import graph
from itertools import permutations

NODE_COUNT: int = 25


def sum_path(points: tuple[any, ...]) -> float:
    sum_: float = 0
    last_point: graph.Point = points[0]

    for point in points:
        sum_ += graph.distance(last_point, point)
        last_point = point

    sum_ += graph.distance(last_point, points[0])
    return sum_


if __name__ == '__main__':
    myMap: list[graph.Point] = graph.generate_points(NODE_COUNT)
    myPaths: permutations = permutations(myMap)
    mySortedPaths: list[float] = []
    myPathDict: dict[float, tuple[any, ...]] = {}

    for path in myPaths:
        # print(path)
        current_path_sum: float = sum_path(path)
        heappush(mySortedPaths, current_path_sum)
        myPathDict[current_path_sum] = path

    shortest_path: float = mySortedPaths[0]
    print(myPathDict[shortest_path])
    print(shortest_path)
