
def utility(values, ncol, gamma):
    # values 就是消费序列
    # ncol 规定了消费序列的维度
    # gamma 是相对风险厌恶度
    import numpy as np
    if len(values[0]) == ncol:
        return values**(1 - gamma) / (1 - gamma)
    else:
        return "Dimension Error!"


if __name__ == "__main__":
    import numpy as ny
    value = [12.3, 23.6, 34.6, 45.6, 37.8, 40.5, 52.5, 55.6]
    value = ny.array([value])
    res = utility(value, 8, 10.0)
    print(res)
