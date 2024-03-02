import copy
import numpy as np


def fp_iterator(density: list[np.ndarray],
                sigma: float,
                relaxation: float = 0) -> list[np.ndarray]:

    A, B, C, D, E, F = copy.deepcopy(density)

    N = A.shape[0] - 2

    den = relaxation + 5*(sigma/6) + N/2
    s1, s2, s3 = (relaxation - (sigma/6))/den, (sigma/6)/den, (N/2)/den

    X = s1*A + s2*(A + B + C + D + E + F)
    for i in range(1, N + 1):
        A[i, :, :] = X[i, :, :] + s3*A[i - 1, :, :]

    # We use the new A computed in this iteration
    X = s1*B + s2*(A + B + C + D + E + F)
    for i in range(N, 0, -1):
        B[i, :, :] = X[i, :, :] + s3*B[i + 1, :, :]

    Y = s1*C + s2*(A + B + C + D + E + F)
    for j in range(1, N + 1):
        C[:, j, :] = Y[:, j, :] + s3*C[:, j - 1, :]

    Y = s1*D + s2*(A + B + C + D + E + F)
    for j in range(N, 0, -1):
        D[:, j, :] = Y[:, j, :] + s3*D[:, j + 1, :]

    Z = s1*E + s2*(A + B + C + D + E + F)
    for k in range(1, N + 1):
        E[:, :, k] = Z[:, :, k] + s3*E[:, :, k - 1]

    Z = s1*F + s2*(A + B + C + D + E + F)
    for k in range(N, 0, -1):
        F[:, :, k] = Z[:, :, k] + s3*F[:, :, k + 1]

    return [A, B, C, D, E, F]
