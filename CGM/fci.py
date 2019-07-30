

def fci(sav, nrow, galfa, n, ret, rf):
    import numpy as np
    ones = np.ones([n, 1])
    capinc = np.empty([nrow, n])
    for ind1 in range(1, nrow + 1):
        rp = ret * galfa + rf * (ones - galfa)
        for ind2 in range(1, n + 1):
            capinc[ind1 - 1][ind2 - 1] = sav[ind1 - 1][0] * rp[ind2 - 1][0]
    return capinc


if __name__ == "__main__":
    import numpy as np
    n = 7
    nrow = 4
    ret = 0.87
    rf = 1.02
    sav = np.array([[0.23, 1.24, 3.45, 2.45]]).T
    galfa = np.array([[1.33, 2.64, 3.35, 3.67, 4.87, 4.99, 5.34]]).T
    y = fci(sav, nrow, galfa, n, ret, rf)
    print(y)


