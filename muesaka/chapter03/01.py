import numpy as np


def linear_convolution(x, h):
    N = len(x)
    z = np.zeros(2 * N - 2)

    for n in range(2 * N - 2):
        for k in range(N):
            if (n - k >= 0) and (n - k <= N - 1):
                z[n] += x[k] * h[n - k]
    return z
