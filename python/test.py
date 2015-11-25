import matplotlib.pyplot as plt
import matplotlib.patches as pch
import mgsp
import itertools
import random

M = [i for i in itertools.product(range(11), range(11))];
M.remove((5, 5))
P = mgsp.separate(M, (4, 5))

def drawMap(M, P):
    x = [m[0] for m in M]
    y = [m[1] for m in M]

    plt.plot(x, y, 'o')
    plt.axis([min(x) - 1, max(x) + 1, max(y) + 1, min(y) - 1])
    axis = plt.gca()
    for R in P:
        x, y, w, h = R[0][0], R[1][0], R[0][1] - R[0][0] + 1, R[1][1] - R[1][0] + 1
        axis.add_patch(pch.Rectangle((x - 0.5, y - 0.5), w, h, facecolor="grey"))
    plt.show()

drawMap(M, P)
