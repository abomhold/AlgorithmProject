from typing import Generator
import math
import matplotlib.pyplot as plt

brute: list[int] = [21, 88, 445, 2676, 18739, 149920, 1349289, 13492900, 148421911, 1781062944]
dynamic: list[int] = [21, 64, 185, 516, 1393, 3648, 9297, 23140, 56441, 135312]
chris: list[int] = [32, 53, 84, 142, 184, 272, 391, 502, 680, 792]
nearest: list[int] = [19, 29, 41, 55, 71, 89, 109, 131, 155, 181]
x_values: list[int] = [x for x in range(4, 14)]
min_nodes: int = 4
max_nodes: int = 14


def generate_plot() -> None:
    fig, ax = plt.subplots()
    ax.plot(x_values, brute, 'x', linestyle=':', color='red', label='naive')
    ax.plot(x_values, dynamic, 'x', linestyle=':', color='blue', label='dynamic')
    ax.plot(x_values, chris, 'x', linestyle=':', color='green', label='chris')
    ax.plot(x_values, nearest, 'x', linestyle=':', color='purple', label='nearest')

    ax.plot(x_values, [x for x in fact_class_gen(max_nodes)], linestyle=(0, (1, 10)), color='black', label='Θ(n!)')
    ax.plot(x_values, [x for x in exp_class_gen(max_nodes)], linestyle=(0, (1, 10)), color='black', label='Θ(2ⁿ)')
    ax.plot(x_values, [x for x in square_class_gen(max_nodes)], linestyle=(0, (1, 10)), color='black', label='Θ(n²)')

    ax.legend(loc='upper left')
    ax.set_yscale('log', base=2)

    ax.set(
        xlabel="number of cites",
        ylabel="number of distance calculations",
        title="Runtime Cost of Traveling Salesman Solutions",
        xmargin=.03,
        xticks=[x for x in range(min_nodes, max_nodes)]
    )

    plt.show()


def exp_class_gen(limit: int) -> Generator[int, None, None]:
    for i in range(min_nodes, limit):
        yield 2 ** i


def fact_class_gen(limit: int) -> Generator[int, None, None]:
    for i in range(min_nodes, limit):
        yield math.factorial(i)


def quad_class_gen(limit: int) -> Generator[int, None, None]:
    for i in range(min_nodes, limit):
        yield i ** 4


def tri_class_gen(limit: int) -> Generator[int, None, None]:
    for i in range(min_nodes, limit):
        yield i ** 3


def square_class_gen(limit: int) -> Generator[int, None, None]:
    for i in range(min_nodes, limit):
        yield i ** 2


if __name__ == '__main__':
    generate_plot()
