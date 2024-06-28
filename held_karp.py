import timeit
from heapq import heappush, heappop

from graph import path_distance, generate_points, Point

N: int = 5
node_array: list[Point] = generate_points(N)
memo = {}

def solve(pos, mask):



if __name__ == '__main__':
    min_time: float = float('inf')
    for i in range(1):
        start_time = timeit.default_timer()
        shortest = solve(node_array)
        print(shortest)
        end_time = timeit.default_timer()
        min_time = min(min_time, end_time - start_time)
    print(min_time)


# def held_karp(arr, pos, mask, memo):
#     # Check if all nodes have been visited
#     if mask == 2 ** len(arr) - 1:
#         return distance(arr[pos], arr[0])
#
#     if memo.__contains__((pos, mask)):
#         return memo[(pos, mask)]
#
#     ans = float('inf')
#
#     for i in range(1, len(arr)):
#         if (mask >> i) == 0:
#             ans = min(ans, held_karp(arr, i, (mask | 1 << i), memo) + distance(arr[pos], arr[i]))
#     memo[(pos, mask)] = ans
#     return ans
# # # Algorithm tsp({c1, c2, . . . cn}, d).
# # # Input: Set of cities {c1, c2, . . . , cn} and for each pair of cities ci, c j the distance d(ci, c j ).
# # # Output: The minimum length of a tour.
# # # for i = 2 to n do
# # # OPT [ci, ci] = d(c1, ci)
# # # for j = 2 to n − 1 do
# # # forall S ⊆ {2, 3, . . . , n} with |S| = j do
# # # OPT [S, ci] = min{OPT [S \ {ci}, ck] + d(ck, ci) : ck ∈ S \ {ci}}
# # # return min{OPT [{c2, c3, . . . , cn}, ci] + d(ci, c1) : i ∈ {2, 3, . . . , n}}
# def distance(x, y):
#     return 0
#
#
# def held_karp(arr):
#     opt = []
#     for i in range(1, len(arr)):
#         opt[i][i] = distance(arr[0], arr[i])
#
#     for j in range(1, len(arr)-1):
#
#
# # import graph
# #
# # N: int = 5
# # node_array: list[graph.Point] = graph.generate_points(N)
# # heap: list[float] = []
# # table: dict[float, list[graph.Point]] = {}
# # p: list[int] = list(range(0, N + 1))
# #
# #
# # # Algorithm tsp({c1, c2, . . . cn}, d).
# # # Input: Set of cities {c1, c2, . . . , cn} and for each pair of cities ci, c j the distance d(ci, c j ).
# # # Output: The minimum length of a tour.
# # # for i = 2 to n do
# # # OPT [ci, ci] = d(c1, ci)
# # # for j = 2 to n − 1 do
# # # forall S ⊆ {2, 3, . . . , n} with |S| = j do
# # # OPT [S, ci] = min{OPT [S \ {ci}, ck] + d(ck, ci) : ck ∈ S \ {ci}}
# # # return min{OPT [{c2, c3, . . . , cn}, ci] + d(ci, c1) : i ∈ {2, 3, . . . , n}}
# #
# #
# # # Set up ajacnecy matrix
# # def adjacency(array: list[graph.Point]) -> list[list[float]]:
# #     new_array: list[list[float]] = []
# #     for i in range(2, len(array)):
# #         new_array[i][i] = graph.distance(array[1], array[i])
# #
# #     for j in range(2, len(array) - 1):
# #
# #
#
# # def adjacency(array: list[graph.Point]) -> list[list[float]]:
# #     adjacency_matrix: list[list[graph.Point]] = []
# #     for i in range(len(array)):
# #         for j in range(len(array)):
# #             adjacency_matrix[i][j] = graph.distance(array[i], array[j])
# #
# #     return adjacency_matrix
# #
# def permutations(arr: list[Point]) -> list[list[Point]]:
#     if len(arr) < 2:
#         return [arr]
#     perm_list = []
#     for j in arr:
#         remaining_elements = [x for x in arr if x != j]
#         if memo.__contains__(remaining_elements):
#             return memo[remaining_elements]
#
#
#
#
#
#         for perm in permutations(remaining_elements):
#             perm_list.append([j] + perm)
#     return perm_list
#
#
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
