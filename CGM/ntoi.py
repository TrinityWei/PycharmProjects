

def NTOI(value, nrow, grid, n):
    import numpy as np
    aux = np.zeros([nrow, 1])

    for i in range(0, nrow):
        if value[i][0] >= grid[-1][0]:
            aux[i][0] = grid[-1][0]
        else:
            aux[i][0] = value[i][0]

    for i in range(0, nrow):
        if aux[i][0] <= grid[0][0]:
            aux[i][0] = grid[0][0]

    step = (grid[n - 1][0] - grid[0][0]) / (n - 1)
    ones = np.ones([nrow, 1])
    # res = (np.subtract(aux, np.multiply(grid[0][0], ones))) / step
    res = ((aux - grid[0][0] * ones) / step) + ones
    for k in range(0, nrow - 1):
        res[k][0] = int(round(res[k][0]))
    return res


if __name__ == "__main__":
    import numpy as np
    values = [1.56, 0.12, 1.34, 2.34, 0.02, 0.83, 5.89]
    values = np.array([values]).T
    nrow = 7
    grid = [0.23, 1.24, 3.45, 2.45, 5.23]
    grid = np.array([grid]).T
    n = 5
    y = NTOI(values, nrow, grid, n)
    print(y)
