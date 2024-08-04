import math
import random
from typing import Generator

# Global
board_length: int = 100
calculations: int = 0


# Point data class
class Point(tuple):
    x_cord: int
    y_cord: int

    def __new__(cls, x_cord: int, y_cord: int):
        return tuple.__new__(cls, (x_cord, y_cord))

    def __repr__(self) -> str:
        return f'({self[0]}, {self[1]})'


# Use distance formula on two point objects
# tag::calculate_distance[]
def calculate_distance(point1, point2) -> float:
    global calculations
    calculations += 1
    p1_x, p1_y = point1
    p2_x, p2_y = point2
    return math.sqrt(
        math.pow(p1_x - p2_x, 2) +
        math.pow(p1_y - p2_y, 2))


# end::calculate_distance[]


# Iteratively sum the loop of points
def path_distance(points: list[Point]) -> float:
    accumulator: float = 0.0
    last_point: Point = points[-1]

    for point in points:
        accumulator += calculate_distance(last_point, point)
        last_point = point

    return accumulator


# Create a matrix for the distance between all points
def create_distance_dict(points: list[Point]) -> dict[tuple[Point, Point], float]:
    dist = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist[(points[i], points[j])] = calculate_distance(points[i], points[j])
            dist[(points[j], points[i])] = dist[(points[i], points[j])]
    return dist


# Incermentally build paths from length 4 to limit
def path_generator(limit: int) -> Generator[list[Point], None, None]:
    for i in range(4, limit):
        yield generate_points(i)


def generate_points(node_count: int) -> list[Point]:
    points: list[Point] = []

    for _ in range(node_count):
        new_point: Point = Point(random.randint(0, board_length), random.randint(0, board_length))
        # Re-roll for duplicates
        # When is it better to re-roll vs calculate all and then pick randomly?
        while new_point in points:
            new_point = Point(random.randint(0, board_length), random.randint(0, board_length))
        points.append(new_point)

    return points


if __name__ == '__main__':
    points_list = generate_points(20)
    print(f"Path: {points_list}")
    print(f"Cost: {path_distance(points_list)}")
    print(f"Count: {calculations}")
    print(f"Matrix: {create_distance_dict(points_list)}")
