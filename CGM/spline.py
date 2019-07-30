

def spline(x, y, n, gram):
    import numpy as np

    y2 = np.empty([n, 1], dtype=float)
    u = np.empty([1, 1], dtype=float)
    yp1 = (x[0][0]) ** (-gram)

    y2[0][0] = -0.5

    u[0][0] = (3.0 / (x[1][0] - x[0][0])) * ((y[1][0] - y[0][0]) / (x[1][0] - x[0][0]) - yp1)
    for i in range(2, n):
        print(i)
        sig = (x[i - 1][0] - x[i - 2][0]) / (x[i][0] - x[i - 2][0])
        p = sig * y2[i - 2][0] + 2.0
        y2[i - 1][0] = (sig - 1.0) / p
        last = (6.0 * ((y[i] - y[i - 1]) / (x[i] - x[i - 1]) - (y[i - 1] - y[i - 2]) / (x[i - 1] - x[i - 2])) / (
                x[i][0] - x[i - 2][0]) - sig * u[i - 2][0]) / p
        u = np.append(u, last)
        u = np.array([u]).T

    y2[-1][0] = 0.0

    for k in range(n - 1, 0, -1):
        print(k)
        y2[k - 1][0] = y2[k - 1][0] * y2[k][0] + u[k - 1][0]
    return y2


if __name__ == "__main__":
    import numpy as np
    x1 = [1.2, 2.8, 3.4, 4.9, 5.2, 6.4, 7.2, 8.1, 9.5, 10.7]
    y1 = [23.0, 54.0, 65.0, 76.0, 34.0, 45.0, 56.0, 67.0, 90.0, 189.0]
    x1 = np.array([x1]).T
    y1 = np.array([y1]).T
    y3 = spline(x1, y1, 10, 10)




# def spline_1(x, y, gram):
#     y2 = [1, 1, 1, 1, 1]
#     u = [1, 1, 1, 1, 1]
#     yp1 = x[0]**(-gram)
#     y2[0] = -0.5
#     u[0] = (3.0/(x[1] - x[0])) * (y[1] - y[0]) / (x[2] - x[1] - yp1)
#     for i in range(1, len(x) - 1):
#         sig = (x[i] - x[i-1]) / (x[i+1] - x[i-1])
#         p = sig * y2[i-1] + 2.0
#         y2[i] = (sig - 1.0) / p
#         u[i] = (6.0 * ((y[i+1] - y[i]) / (x[i+1] - x[i]) - (y[i] - y[i-1]) / (x[i] - x[i-1])) / (x[i+1] - x[i-1]) - sig * u[i-1]) / p
#     y2[-1] = 0.0
#     for k in range(1, len(x), -1):
#         y2[k] = y2[k] * y2[k+1] + u[k]
#     return y2
#
#
# import numpy as np
# n = 10
# x = [1.2, 2.8, 3.4, 4.9, 5.2, 6.4, 7.2, 8.1, 9.5, 10.7]
# y = [23, 54, 65, 76, 34, 45, 56, 67, 90, 89]
#
# x = np.array([x]).T
# y = np.array([y]).T
#
# y2 = np.empty([n, 1], dtype=float)
# u = np.empty([1, 1], dtype=float)
# gram = -10
# yp1 = x[0][0] ** (-gram)
#
# y2[0][0] = -0.5
#
# u[0][0] = (3.0/(x[1][0] - x[0][0])) * (y[1][0] - y[0][0]) / (x[1][0] - x[0][0] - yp1)
#
# for i in range(2, n):
#     print(i)
#     sig = (x[i - 1][0] - x[i - 2][0]) / (x[i][0] - x[i - 2][0])
#     p = sig * y2[i - 2][0] + 2.0
#     y2[i - 1][0] = (sig - 1.0) / p
#     last = (6.0 * ((y[i] - y[i - 1]) / (x[i] - x[i - 1]) - (y[i - 1] - y[i - 2]) / (x[i - 1] - x[i - 2])) / (
#                 x[i] - x[i - 2]) - sig * u[i - 2]) / p
#     u = np.append(u, last)
# u = np.array([u]).T
#
# y2[-1][0] = 0.0
#
# for k in range(n - 1, 0, -1):
#     print(k)
#     y2[k - 1][0] = y2[k - 1][0] * y2[k][0] + u[k - 1][0]
