import matplotlib.pyplot as plt
import numpy as np
from matplotlib.scale import LogScale

from graph import Point


def plot_points(points: list[tuple[int, int]]) -> None:
    fig, ax = plt.subplots()
    # ax.set_yscal;e

    ax.set_yscale('log', base=2)
    # ax.set_xscale('log', base=2)
    # ax.set_ylim(ymin=0,ymax=40000000)
    ax.set_xlim(xmin=3, xmax=20)

    for current_point in points:
        plt.stem(current_point[0], current_point[1], linefmt='grey', markerfmt='D', bottom=1.1)
        # plt.stem(,current_point[0])
    plt.show()


# for testing
data = [(4, 21), (5, 85), (6, 270), (7, 786), (8, 2179), (9, 5827), (10, 15124), (11, 38264), (12, 94705), (13, 230017),
        (14, 549674), (15, 1295342), (16, 3015887), (17, 6948303), (18, 15861488), (19, 35915828)]

if __name__ == '__main__':
    plot_points(data)

# fig, ax = plt.subplots()
#
# dt = 0.01
# t = np.arange(dt, 20.0, dt)
#
# ax.semilogx(t, np.exp(-t / 5.0))
# ax.grid()
#
# plt.show()
