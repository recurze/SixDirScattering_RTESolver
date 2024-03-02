import copy
import numpy as np


def mgs_iterator(density: list[np.ndarray],
                 sigma: float,
                 colors: list[list[tuple[int, int, int]]],
                 omega: float = 1) -> list[np.ndarray]:

    A, B, C, D, E, F = copy.deepcopy(density)
    N = A.shape[0] - 2

    M = np.linalg.inv((N/2 + sigma) * np.eye(6) - sigma/6)

    for ci, cj, ck in [zip(*c) for c in colors]:
        # The following indices belong to a different color by design
        X = (N/2) * np.vstack([
            A[[i - 1 for i in ci], cj, ck],
            B[[i + 1 for i in ci], cj, ck],
            C[ci, [j - 1 for j in cj], ck],
            D[ci, [j + 1 for j in cj], ck],
            E[ci, cj, [k - 1 for k in ck]],
            F[ci, cj, [k + 1 for k in ck]],
        ])
        A[ci, cj, ck], B[ci, cj, ck], C[ci, cj, ck], D[ci, cj, ck], E[ci, cj, ck], F[ci, cj, ck] = \
            omega * (M.dot(X)) + (1 - omega) * np.vstack([
                A[ci, cj, ck],
                B[ci, cj, ck],
                C[ci, cj, ck],
                D[ci, cj, ck],
                E[ci, cj, ck],
                F[ci, cj, ck],
            ])

    return [A, B, C, D, E, F]
