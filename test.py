import cython
import c_graph
# from c_graph import generate_points, calculations, path_distance
import graph
import timeit

node_count = 10000

start_time = timeit.default_timer()
points_list = c_graph.generate_points(node_count)
# print(f"Path: {points_list}")
# print(f"Cost: {c_graph.path_distance(points_list)}")
end_time = timeit.default_timer()

print(f"Took {end_time - start_time}")

start_time = timeit.default_timer()
points_list = graph.generate_points(node_count)
# print(f"Path: {points_list}")
# print(f"Cost: {graph.path_distance(points_list)}")
end_time = timeit.default_timer()

print(f"Took {end_time - start_time}")
