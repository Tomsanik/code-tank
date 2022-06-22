import numpy as np


def Ex(a: list):    # mean value of arrays (vectors nad matrices)
    if not a:
        return None
    A = np.zeros(a[0].shape)
    for i in a:
        A += i
    return A / len(a)


def deviation(a: list):  # deviaton sqrt(var) of list of vectors
    if not a:
        return None
    ex = Ex(a)
    a = [i - ex for i in a]
    pfpf = [np.outer(i, i) for i in a]
    var = Ex(pfpf)  # matrix, E[(X-EX)(X-EX).T]
    dev = np.sqrt(np.array([var[i][i] for i in range(len(var))]))  # diagonal has vars
    dev = np.divide(dev, np.absolute(ex)) * 100
    return dev
