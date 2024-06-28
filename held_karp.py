# import graph
#
# N: int = 5
# node_array: list[graph.Point] = graph.generate_points(N)
# heap: list[float] = []
# table: dict[float, list[graph.Point]] = {}
# p: list[int] = list(range(0, N + 1))
#
#
# # Algorithm tsp({c1, c2, . . . cn}, d).
# # Input: Set of cities {c1, c2, . . . , cn} and for each pair of cities ci, c j the distance d(ci, c j ).
# # Output: The minimum length of a tour.
# # for i = 2 to n do
# # OPT [ci, ci] = d(c1, ci)
# # for j = 2 to n − 1 do
# # forall S ⊆ {2, 3, . . . , n} with |S| = j do
# # OPT [S, ci] = min{OPT [S \ {ci}, ck] + d(ck, ci) : ck ∈ S \ {ci}}
# # return min{OPT [{c2, c3, . . . , cn}, ci] + d(ci, c1) : i ∈ {2, 3, . . . , n}}
#
#
# # Set up ajacnecy matrix
# def adjacency(array: list[graph.Point]) -> list[list[float]]:
#     new_array: list[list[float]] = []
#     for i in range(2, len(array)):
#         new_array[i][i] = graph.distance(array[1], array[i])
#
#     for j in range(2, len(array) - 1):
#
#

# def adjacency(array: list[graph.Point]) -> list[list[float]]:
#     adjacency_matrix: list[list[graph.Point]] = []
#     for i in range(len(array)):
#         for j in range(len(array)):
#             adjacency_matrix[i][j] = graph.distance(array[i], array[j])
#
#     return adjacency_matrix
#
