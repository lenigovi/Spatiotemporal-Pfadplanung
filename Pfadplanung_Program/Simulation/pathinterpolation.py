import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def multP(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            r[i + j] += a[i] * b[j]
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r

def sumP(a, b):
    if len(b) > len(a):
        a, b = b, a
    r = a[:]
    for i in range(len(b)):
        r[i] += b[i]
    return r

def getPval(P, t):
    r = P[0]
    for i in range(1, len(P)):
        r += P[i] * (t ** i)
    return r

def interpolate(waypoints):
    R = []
    n = len(waypoints)
    L = []
    for i in range(n):
        lagr = [1]
        for j in range(n):
            if j != i:
                lagr = multP(lagr, [-waypoints[j][0] / (waypoints[i][0] - waypoints[j][0]), 1 / (waypoints[i][0] - waypoints[j][0])])
        L.append(lagr)
    for i in range(3):
        p = [0] * (len(L[0]) + 1)
        for j in range(n):
            term = [waypoints[j][1 + i] * coeff for coeff in L[j]]
            p = sumP(p, term)
        R.append(p)
    return R

def plotInterp(W_list, R_list, delay=1):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    colors = ['r', 'g', 'b', 'c']

    for idx, (W, R) in enumerate(zip(W_list, R_list)):
        tm = min([W[i][0] for i in range(len(W))])
        tM = max([W[i][0] for i in range(len(W))])
        ax.scatter([W[i][1] for i in range(len(W))], [W[i][2] for i in range(len(W))], [W[i][3] for i in range(len(W))], color=colors[idx])
        ax.plot([getPval(R[0], i) for i in np.linspace(tm, tM, 100)], 
                [getPval(R[1], i) for i in np.linspace(tm, tM, 100)], 
                [getPval(R[2], i) for i in np.linspace(tm, tM, 100)], color=colors[idx])

    points = [ax.plot([], [], [], marker='o', color=colors[idx])[0] for idx in range(len(W_list))]
    arrows = [ax.quiver([], [], [], [], [], [], color='black', arrow_length_ratio=0.1) for _ in range(len(W_list))]

    def init():
        for point, arrow in zip(points, arrows):
            point.set_data([], [])
            point.set_3d_properties([])
            arrow.set_segments([])
        return points + arrows

    def update(frame):
        for idx, (W, R, point, arrow) in enumerate(zip(W_list, R_list, points, arrows)):
            tm = min([W[i][0] for i in range(len(W))])
            tM = max([W[i][0] for i in range(len(W))])
            t = np.linspace(tm, tM, 100)[frame]
            if idx == 0:
                if t < delay:
                    x, y, z = W[0][1], W[0][2], W[0][3]
                else:
                    t = t - delay  # Apply delay
                    x = getPval(R[0], t)
                    y = getPval(R[1], t)
                    z = getPval(R[2], t)
            else:
                x = getPval(R[0], t)
                y = getPval(R[1], t)
                z = getPval(R[2], t)
            
            point.set_data(x, y)
            point.set_3d_properties(z)

            arrow.set_segments([[np.array([x, y, z]), np.array([x+1, y, z])],  # X direction
                                [np.array([x, y, z]), np.array([x, y+1, z])],  # Y direction
                                [np.array([x, y, z]), np.array([x, y, z+1])]]) # Z direction
        return points + arrows

    ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
    plt.show()

# Adjust the waypoints and introduce a delay for R1
W1 = [[1, -25, -10, 0], [2, -15, -8, 0], [3, -10, -1, 0], [4, 0, -1, 0], [5, 10, 0, 0]]
W2 = [[0, -25, 20, 0], [1, -10, 10, 0], [2, -5, -2, 0], [3, 0, -1, 0], [4, 5, -2, 0]]
W3 = [[0, 25, 20, 0], [1, 3, 10, 0], [2, 2, 2, 0], [3, 3, -1, 0], [4, 4, 0, 0]]
W4 = [[1, -25, -10, 0], [2, -15, -8, 0], [3, -10, -1, 0], [4, 0, -1, 0], [5, 10, 0, 0]]

R1 = interpolate(W1)
R2 = interpolate(W2)
R3 = interpolate(W3)
R4 = interpolate(W4)

plotInterp([W1, W2, W3, W4], [R1, R2, R3, R4], delay=2)
