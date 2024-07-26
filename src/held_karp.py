import graph
from graph import generate_points, Point, calculate_distance

max_node_count: int = 11

node_count: int
node_array: list[Point]
memo: dict[tuple[int, int], tuple[float, list[Point]]]


def solve(pos: int, mask: int) -> tuple[float, list[Point]]:
    # Check if all positions have been visited this recursive call
    if mask == (1 << node_count) - 1:
        return calculate_distance(node_array[pos], node_array[0]), [node_array[0]]

    # Check if the current combination has been calculated before
    if (pos, mask) in memo:
        return memo[(pos, mask)]

    best_distance = float('inf')
    best_path = []

    for j in range(node_count):
        # if the index is not in the mask,...
        if not (mask & (1 << j)):
            current_distance, sub_path = solve(j, mask | (1 << j))
            current_distance += calculate_distance(node_array[pos], node_array[j])

            if current_distance < best_distance:
                best_distance = current_distance
                best_path = [node_array[j]] + sub_path

    memo[(pos, mask)] = (best_distance, best_path)
    return memo[(pos, mask)]


if __name__ == '__main__':
    for i in range(4, max_node_count):
        node_count = i
        node_array = generate_points(node_count)
        memo = {}
        cost, path = solve(0, 1)
        print(f"{i},{cost},{graph.calculations},{path}")