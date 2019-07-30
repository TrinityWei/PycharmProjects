import splint


def ev(cash, nrow, ncol, v, nco, prob, n, fy, eyp, grid, secondd, ret, ret_coef):
    # cash fci的结果
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
    import numpy as np
    ev_out = 0.0
    ones = np.ones([nrow, ncol])  # (4, 7)
    inc2 = np.empty([nrow, ncol])
    v1 = np.empty([nrow, ncol])
    aux = np.empty([nrow, ncol])

    for ind1 in range(1, n + 1):
        for ind2 in range(1, n + 1):
            inc = fy[ind1 - 1][0] * eyp[ind2 - 1][0] + ret_coef * ret
            inc2 = inc * ones + cash  # (4, 7)
            for i in range(0, nrow):
                for i1 in range(0, ncol):
                    if inc2[i][i1] >= grid[nco - 1][0]:
                        inc2[i][i1] = grid[nco - 1][0]

            for k in range(0, nrow):
                for k1 in range(0, ncol):
                    if inc2[k][k1] <= grid[0][0]:
                        inc2[k][k1] = grid[0][0]

            aux = splint.splint(grid, v, secondd, nco, inc2, nrow, ncol)
            v1 = prob[ind1 - 1][0] * prob[ind2 - 1][0] * aux
            ev_out = ev_out + v1
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
    cash = np.ones([nrow, ncol])
    n = 10
    nco = 8
    v = np.ones([nco, 1])
    prob = np.array([[1.33, 2.64, 3.35, 3.67, 4.87, 4.99, 5.34, 7.33, 6.34, 9.23]]).T
    fy = np.ones([n, 1])
    eyp = np.ones([n, 1])
    grid = np.ones([nco, 1])
    secondd = np.ones([nco, 1])
    ret = 0.87
    ret_coef = 0.0700855

    y = ev(cash, nrow, ncol, v, nco, prob, n, fy, eyp, grid, secondd, ret, ret_coef)
    print(y)

