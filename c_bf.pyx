import graph
from graph import generate_points, Point, calculate_distance
from c_graph import generate_points, Point, calculate_distance

max_node_count: int = 10
node_count: int
node_array: list[Point]
memo: dict[tuple[int, int], tuple[float, list[Point]]]


cpdef tuple[float, list] find_shortest_path(pos: int, mask: int) -> tuple[float, list[Point]]:
    # Check if all positions have been visited this recursive call
    if mask == (1 << node_count) - 1:
        return calculate_distance(node_array[pos], node_array[0]), [node_array[0]]

    best_distance = float('inf')
    best_path = []

    for j in range(node_count):
        # if the index is not in the mask,...
        if not (mask & (1 << j)):
            current_distance, sub_path = find_shortest_path(j, mask | (1 << j))  # the | flips the current bit
            current_distance += calculate_distance(node_array[pos], node_array[j])

            if current_distance < best_distance:
                best_distance = current_distance
                best_path = [node_array[j]] + sub_path

    return best_distance, best_path


if __name__ == '__main__':
    for i in range(4, max_node_count):
        node_count = i
        node_array = generate_points(node_count)
        memo = {}
        cost, path = find_shortest_path(0, 1)
        print(f"{i},{cost},{graph.calculations},{path}")
