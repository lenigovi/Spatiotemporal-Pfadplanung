import matplotlib.pyplot as plt
import numpy as np

def multP(a, b):
    '''
    Multiplies two polynomials a and b into r
    FORMAT :
    P(x) = ax^n + ... + bx + c <=> P = [c,b,...,a]
    '''
    r = [0] * (len(a) + len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            r[i + j] += a[i] * b[j]
    while r[-1] == 0:
        r.pop()
    return r

def sumP(a, b):
    '''
    Sums two polynomials a and b into r
    FORMAT :
    P(x) = ax^n + ... + bx + c <=> P = [c,b,...,a]
    '''
    if len(b) > len(a):
        a, b = b, a
    r = a[:]
    for i in range(len(b)):
        r[i] += b[i]
    return r

def getPval(P, t):
    '''
    Gives the values of polynomial P at evaluation point t
    '''
    r = P[0]
    for i in range(1, len(P)):
        r += P[i] * (t ** i)
    return r

def interpolate(waypoints):
    '''
    Interpolates a polynomial trajectory for a perfect fit with flight inputs expected as follows:
    waypoints = [point,point,point,...] 
    with point = [time,x,y,z]

    polynomials are stored as such :
    P(x) = ax^n + ... + bx + c <=> P = [c,b,...,a]
    '''
    R = []
    n = len(waypoints)
    L = []
    for i in range(n):
        lagr = [0] * 2
        for j in range(n):
            if j == 0:
                if i == 0:
                    lagr[0] = 1
                    lagr[1] = 0
                else:
                    lagr[0] = -waypoints[0][0] / (waypoints[i][0] - waypoints[0][0])
                    lagr[1] = 1 / (waypoints[i][0] - waypoints[0][0])
            else:
                if j != i:
                    lagr = multP(lagr, [-waypoints[j][0] / (waypoints[i][0] - waypoints[j][0]), 1 / (waypoints[i][0] - waypoints[j][0])])
                else:
                    continue
        L += [lagr]
    for i in range(3):
        p = []
        for j in range(n):
            p = sumP(p, [waypoints[j][1 + i] * L[j][k] for k in range(n)])
        R += [p]
    return R

def plotInterp(W_list, R_list):
    '''
    Plots the interpolation points W_list with the interpolated curves R_list
    '''
    ax = plt.figure().add_subplot(projection='3d')
    colors = ['r', 'g', 'b']
    for idx, (W, R) in enumerate(zip(W_list, R_list)):
        tm = min([W[i][0] for i in range(len(W))])
        tM = max([W[i][0] for i in range(len(W))])
        ax.scatter([W[i][1] for i in range(len(W))], [W[i][2] for i in range(len(W))], [W[i][3] for i in range(len(W))], color=colors[idx])
        ax.plot([getPval(R[0], i) for i in np.linspace(tm, tM, 100)], [getPval(R[1], i) for i in np.linspace(tm, tM, 100)], [getPval(R[2], i) for i in np.linspace(tm, tM, 100)], color=colors[idx])
    plt.show()

# Waypoint Set
W1 = [[0, 0, -10, 0], [1, 1, -8, 0], [2, 3, -1, 0]]
W2 = [[0, -25, -5, 1], [1, -20, -3, 0.8], [2, -10, -2, 0.5]]
W3 = [[0, 5, 5, 0], [1, 3, 3, 0], [2, 2, 2, 0]]

R1 = interpolate(W1)
R2 = interpolate(W2)
R3 = interpolate(W3)

plotInterp([W1, W2, W3], [R1, R2, R3])
