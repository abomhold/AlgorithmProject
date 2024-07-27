from src.graph import generate_points, calculate_distance, Point

max_node_count: int = 11


def solve(input_list: list[Point]) -> tuple[float, list[Point], int]:
    in_node_count = len(input_list)
    in_node_array = input_list
    in_memo = {}
    distance, path, cost = solve_loop(0, 1, in_node_array, in_node_count, in_memo, 0)
    return distance, path, cost


def solve_loop(pos: int, mask: int, node_array: list[Point], node_count: int,
               memo: dict[tuple[int, int], tuple[float, list[Point]]], cost: int) -> tuple[float, list[Point], int]:
    # Check if all positions have been visited this recursive call
    if mask == (1 << node_count) - 1:
        cost += 1
        return calculate_distance(node_array[pos], node_array[0]), [node_array[0]], cost

    # Check if the current combination has been calculated before
    if (pos, mask) in memo:
        (best_distance, best_path) = memo[(pos, mask)]
        return best_distance, best_path, cost

    best_distance = float('inf')
    best_path = []

    for j in range(node_count):
        # if the index is not in the mask,...
        if not (mask & (1 << j)):
            current_distance, sub_path, cost = solve_loop(j, mask | (1 << j), node_array, node_count, memo, cost)
            cost += 1
            current_distance += calculate_distance(node_array[pos], node_array[j])

            if current_distance < best_distance:
                best_distance = current_distance
                best_path = [node_array[j]] + sub_path

    memo[(pos, mask)] = (best_distance, best_path)
    return best_distance, best_path, cost

# if __name__ == '__main__':
#     for i in range(4, max_node_count):
#         node_count = i
#         node_array = generate_points(node_count)
#         memo = {}
#         cost, path = solve(node_array)
#         print(f"{i},{cost},{graph.calculations},{path}")
