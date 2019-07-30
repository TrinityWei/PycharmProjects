

def splint(xa, ya, y2a, n, x, nrow, ncol):
    import numpy as np
    klo = 1
    khi = n
    for indr in range(1, nrow + 1):
        for indc in range(1, ncol + 1):
            klo = 1
            khi = n
            while khi - klo > 1:
                k = (khi+klo)/2
                k = int(round(k))
                if xa[k - 1][0] > x[indr - 1][indc - 1]:
                    khi = k
                else:
                    klo = k

            h = xa[khi - 1][0] - xa[klo - 1][0]
            a = (xa[khi - 1][0] - x[indr - 1][indc - 1]) / h
            b = (x[indr - 1][indc - 1] - xa[klo - 1][0]) / h
            y = np.empty([nrow, ncol])
            y[indr - 1][indc - 1] = a * ya[klo - 1][0] + b * ya[khi - 1][0] + \
                                    ((a**3 - a) * y2a[klo - 1][0] + (b**3-b) * y2a[khi - 1][0]) * (h**2) / 6.0
    return y


if __name__ == "__main__":
    import numpy as np
    n = 5
    nrow = 4
    ncol = 3
    x = np.ones([4, 3])
    xa = [0.23, 1.24, 3.45, 2.45, 5.23]
    xa = np.array([xa]).T
    ya = [1.33, 2.64, 3.35, 3.67, 4.87]
    ya = np.array([ya]).T
    y2a = [1.13, 2.14, 2.45, 4.05, 5.45]
    y2a = np.array([y2a]).T
    y = splint(xa, ya, y2a, n, x, nrow, ncol)

