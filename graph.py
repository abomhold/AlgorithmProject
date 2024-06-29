import math
import random
import matplotlib.pyplot as plt

# Consts
BOARD_SIZE: int = 100


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
        acc += distance(last_point, point)
        last_point = point

    return acc


def distance(point1: Point, point2: Point) -> float:
    return math.sqrt(math.pow(point1.x_cord - point2.x_cord, 2)
                     + math.pow(point1.y_cord - point2.y_cord, 2))


def generate_points(node_count: int) -> list[Point]:
    points: list[Point] = []

    for count in range(node_count):
        new_point: Point = Point(
            random.randint(0, BOARD_SIZE),
            random.randint(0, BOARD_SIZE))

        #Reroll for duplicates
        while new_point in points:
            new_point = Point(random.randint(0, BOARD_SIZE), random.randint(0, BOARD_SIZE))

        points.append(new_point)

    return points


def plot_points(points: list[Point]) -> None:
    for current_point in points:
        plt.scatter(current_point.x_cord, current_point.y_cord)

    plt.show()


if __name__ == '__main__':
    points_list = generate_points(7)
    print(points_list)
    print(path_distance(points_list))

    plot_points(points_list)
