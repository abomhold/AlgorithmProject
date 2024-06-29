import math
import random
import matplotlib.pyplot as plt

# Global
board_length: int = 100
calculations: int = 0


class Point:
    x_cord: int
    y_cord: int

    def __init__(self, x_cord: int, y_cord: int):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def __repr__(self) -> str:
        return f'({self.x_cord}, {self.y_cord})'


def path_distance(points: list[Point]) -> float:
    acc: float = 0.0
    last_point: Point = points[-1]

    for point in points:
        acc += calculate_distance(last_point, point)
        last_point = point

    return acc


def calculate_distance(point1: Point, point2: Point) -> float:
    global calculations
    calculations += 1
    return math.sqrt(math.pow(point1.x_cord - point2.x_cord, 2)
                     + math.pow(point1.y_cord - point2.y_cord, 2))


def generate_points(node_count: int) -> list[Point]:
    points: list[Point] = []

    for _ in range(node_count):
        new_point: Point = Point(
            random.randint(0, board_length),
            random.randint(0, board_length))

        #Reroll for duplicates

        # When is it better to reroll vs calculate all and then pick randomly?

        while new_point in points:
            new_point = Point(random.randint(0, board_length), random.randint(0, board_length))

        points.append(new_point)

    return points


def plot_points(points: list[Point]) -> None:
    for current_point in points:
        plt.scatter(current_point.x_cord, current_point.y_cord)

    plt.show()


if __name__ == '__main__':
    points_list = generate_points(7)
    print(f"Optimal cost: {path_distance(points_list)}")
    print(f"Optimal path: {points_list}")
    print(f"Count: {calculations}")
