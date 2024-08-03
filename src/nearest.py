from src.graph import Point, generate_points, create_distance_dict, path_distance, calculate_distance
from src import graph


def solve(node_array) -> tuple[float, list[Point]]:
    route = nearest_neighbor(node_array)
    distance = path_distance(route)
    return distance, route


def nearest_neighbor(node_array: list[Point]) -> list[Point]:
    distance_dict = create_distance_dict(node_array)
    route = [node_array.pop()]
    remaining: set[Point] = set(node for node in node_array)
    while remaining:
        current_city = route[-1]
        nearest_city = (
            min([(node, distance_dict[(current_city, node)]) for node in remaining], key=lambda x: x[1]))
        route.append(nearest_city[0])
        remaining.remove(nearest_city[0])
        route.append(route[0])
    return route


if __name__ == '__main__':
    for i in range(4, 14):
        graph.calculations = 0
        node_array = generate_points(i)
        dist, path = solve(node_array)
        print(f"{i},{dist},{graph.calculations},{path}")
