from typing import Generator
import math
import matplotlib.pyplot as plt

dynamic: list[int] = [21, 85, 270, 786, 2179, 5827, 15124, 38264, 94705, 230017]
brute: list[int] = [21, 88, 445, 2676, 18739, 149920, 1349289, 13492900, 148421911, 1781062944]
x_values: list[int] = [x for x in range(4, 14)]
min_nodes: int = 4
max_nodes: int = 14


def generate_plot() -> None:
    fig, ax = plt.subplots()
    ax.plot(x_values, brute, '.', linestyle=':', color='red', label='naive')
    ax.plot(x_values, dynamic, '.', linestyle=':', color='blue', label='dynamic')

    ax.plot(x_values, [x for x in fact_class_gen(max_nodes)], linestyle=(0, (1, 10)), color='grey', label='Θ(n!)')
    ax.plot(x_values, [x for x in exp_class_gen(max_nodes)], linestyle=(0, (1, 10)), color='grey', label='Θ(2ⁿ)')
    ax.plot(x_values, [x for x in square_class_gen(max_nodes)], linestyle=(0, (1, 10)), color='grey', label='Θ(n²)')

    ax.legend(loc='upper left')
    ax.set_yscale('log', base=2)

    # ax.set_xlim(xm.in=3, xmax=14)

    ax.set(
        xlabel="number of cites",
        ylabel="number of distance calculations",
        title="Runtime Cost of Traveling Salesman Solutions",
        xmargin=.03,
        xticks=[4,5,6,7,8,9,10,11,12,13]
    )

    plt.show()


def exp_class_gen(limit: int) -> Generator[int, None, None]:
    for i in range(min_nodes, limit):
        yield 2 ** i


def fact_class_gen(limit: int) -> Generator[int, None, None]:
    for i in range(min_nodes, limit):
        yield math.factorial(i)


def square_class_gen(limit: int) -> Generator[int, None, None]:
    for i in range(min_nodes, limit):
        yield i ** 2


if __name__ == '__main__':
    generate_plot()

# import math
#
#

# max_nodes = 14
# dynamic: list[int] = [21, 85, 270,  786,  2179,   5827,   15124,    38264,     94705]
import math
from typing import Generator

import matplotlib.pyplot as plt

max_nodes: int = 13
min_nodes: int = 4
# brute: list[int] =   [21, 88, 445, 2676, 18739, 149920, 1349289, 13492900, 148421911]
# x_values: list[int] = [x for x in range(min_nodes, 15)]
#
#
# def generate_plot() -> None:
#     fig, ax = plt.subplots()
#     ax.plot(x_values, brute, '.', linestyle=':', color='red', label='naive')
#     ax.plot(x_values, dynamic, '.', linestyle=':', color='blue', label='dynamic')
#
#     ax.plot(x_values, [x for x in fact_class_gen(max_nodes)], linestyle=(0, (1, 10)), color='grey', label='Θ(n!)')
#     ax.plot(x_values, [x for x in exp_class_gen(max_nodes)], linestyle=(0, (1, 10)), color='grey', label='Θ(2ⁿ)')
#     ax.plot(x_values, [x for x in square_class_gen(max_nodes)], linestyle=(0, (1, 10)), color='grey', label='Θ(n²)')
#
#     ax.legend(loc='upper left')
#     ax.set_yscale('log', base=2)
#     ax.set(
#         xlabel="number of cites",
#         ylabel="number of distance calculations",
#         title="Runtime Cost of Traveling Salesman Solutions"
#     )
#
#     plt.show()
#
#

#
# if __name__ == '__main__':
#     generate_plot()
