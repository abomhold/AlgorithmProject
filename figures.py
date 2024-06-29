import matplotlib.pyplot as plt
import numpy as np
from matplotlib.scale import LogScale
from graph import Point

dynamic = [21, 85, 270, 786, 2179, 5827, 15124, 38264, 94705]
brute = [21, 88, 445, 2676, 18739, 149920, 1349289, 13492900, 148421911]
x_values = [x for x in range(4, 13)]

if __name__ == '__main__':
    fig, ax = plt.subplots()
    for index in range(len(x_values)):
        plt.plot(x_values[index], dynamic[index], '1', color='blue')

    for index in range(len(x_values)):
        plt.plot(x_values[index], brute[index], '2', color='red')

    ax.set_yscale('log', base=2)
    plt.show()

# plt.step(current_point[0], current_point[1], label='pre (default)')
# fig, ax = plt.subplots()
#
# dt = 0.01
# t = np.arange(dt, 20.0, dt)
#
# ax.semilogx(t, np.exp(-t / 5.0))
# ax.grid()
#
# plt.show()

# # for testing
# # x_values = [x for x in range(4, 20)]
# # dynamic = [21, 85, 270, 786, 2179, 5827, 15124, 38264, 94705, 230017, 549674, 1295342, 3015887, 6948303, 15861488,
# #            35915828]
# #
# dynamic = [(4, 21), (5, 85), (6, 270), (7, 786), (8, 2179), (9, 5827), (10, 15124), (11, 38264), (12, 94705),
#            (13, 230017), (14, 549674), (15, 1295342), (16, 3015887), (17, 6948303), (18, 15861488), (19, 35915828)]
# #
# brute = [(4, 21), (5, 88), (6, 445), (7, 2676), (8, 18739), (9, 149920), (10, 1349289), (11, 13492900), (12, 148421911)]

# def plot_points(points: list[tuple[int, int]]) -> None:
#     fig, ax = plt.subplots()
#     # ax.set_yscal;e
#     # ax.set_yscale('log', base=2)
#     # ax.set_xscale('log', base=2)
#     # ax.set_ylim(ymin=0,ymax=40000000)
#
#     # ax.set_xlim(xmin=3, xmax=20)
#
#     for current_point in points:
#         plt.step(current_point[0], current_point[1], label='pre (default)')
#         plt.plot(current_point[0], current_point[1], 'o--', color='blue')
#         # plt.stem(current_point[0], current_point[1], linefmt='grey', markerfmt='D', bottom=1.1)
#         # plt.stem(,current_point[0])
#         # plt.stairs(current_point[0], current_point[1])
