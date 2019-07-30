import splint


def evr(cash, nrow, ncol, v, nro, nco, fy, grid, secondd):
    # cash fci的结果 维度(ncow, ncol)
    # v 维度(nro, nco)
    # nco
    # prob 维度(n, 1)
    # fy 维度(n, 1)
    # eyp 维度(n, 1)
    # grid 维度(nco, 1)
    # secondd 维度(nco, 1)
    # ret
    # ret_coef
    import numpy as np
    ones = np.ones([nrow, ncol])
    inc = fy * ones + cash
    for i in range(0, nrow):
        for i1 in range(0, ncol):
            if inc[i][i1] >= grid[nco - 1][0]:
                inc[i][i1] = grid[nco - 1][0]

    for k in range(0, nrow):
        for k1 in range(0, ncol):
            if inc[k][k1] <= grid[0][0]:
                inc[k][k1] = grid[0][0]

    prob_li = 0.0
    v = np.array([v[0][:]]).T
    aux = splint.splint(grid, v, secondd, nco, inc, nrow, ncol)
    ev_out = aux

    for d in range(0, nrow):
        for d1 in range(0, ncol):
            inc[d][d1] = 5.0

    aux = splint.splint(grid, v, secondd, nco, inc, nrow, ncol)
    ev_out = (1 - prob_li) * ev_out + prob_li * aux
    return ev_out


if __name__ == "__main__":
    import numpy as np
    # cash fci的结果 维度(nrow, n)
    # v utility的结果，维度(nco, 1)
    # nco
    # prob 维度(n, 1)
    # n
    # fy 维度(n, 1)
    # eyp 维度(n, 1)
    # grid 维度(nco, 1)
    # secondd 维度(nco, 1)
    # ret
    # ret_coef
    nrow = 4
    ncol = 7
    cash = np.random.rand(nrow, ncol)
    n = 10
    nco = nro = 8
    v = np.random.rand(nro, nco)
    prob = np.array([[1.33, 2.64, 3.35, 3.67, 4.87, 4.99, 5.34, 7.33, 6.34, 9.23]]).T
    fy = ret_y = 0.0
    eyp = np.random.rand(n, 1)
    grid = np.random.rand(nco, 1)
    secondd = np.random.rand(nco, 1)

    y = evr(cash, nrow, ncol, v, nro, nco, fy, grid, secondd)
    print(y)

