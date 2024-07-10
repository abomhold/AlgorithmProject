import c_graph
from c_graph import generate_points, calculate_distance
import cython

cdef int max_node_count = 10
cdef int node_count
cdef list node_array = []
cdef dict[tuple, tuple] memo

cpdef tuple[float, list[Point]] solve(int pos, int mask):
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

cdef struct Point:
    int x_cord
    int y_cord
