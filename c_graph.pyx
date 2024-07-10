import random
from dataclasses import dataclass

# Global
board_length = 100
cdef int calculations = 0

# Point data class
# @dataclass
cdef struct Point:
    int x_cord
    int y_cord

# Use distance formula on two point objects
cpdef double calculate_distance(Point point1, Point point2):
    global calculations
    calculations += 1
    return pow((pow(point1.x_cord - point2.x_cord, 2)
                + pow(point1.y_cord - point2.y_cord, 2)), 0.5)

# Iteratively sum the loop of points
cpdef double path_distance(list[Point] points):
    cdef double accumulator = 0.0
    cdef Point last_point = points[-1]
    cdef Point p
    cdef int i
    cdef int length = len(points)

    for i in range(length):
        p = points[i]
        accumulator += calculate_distance(last_point, p)
        last_point = p

    return accumulator

cpdef list[Point] generate_points(int node_count):
    cdef list[Point] points = []
    cdef int i = 0
    for i in range(node_count):
        new_point = Point(random.randint(0, board_length), random.randint(0, board_length))
        while new_point in points:
            new_point = Point(random.randint(0, board_length), random.randint(0, board_length))
        points.append(new_point)

    return points
