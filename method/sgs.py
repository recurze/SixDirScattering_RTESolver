import copy
import numpy as np


def sgs_iterator(density: list[np.ndarray],
                 sigma: float,
                 omega: float = 1) -> list[np.ndarray]:

    A, B, C, D, E, F = copy.deepcopy(density)
    N = A.shape[0] - 2

    # We solve the system of linear equation by matrix inverse
    M = np.linalg.inv((N/2 + sigma) * np.eye(6) - sigma/6)
    M4_4 = np.delete(M[4, :], 4, axis=0)
    M5_5 = np.delete(M[5, :], 5, axis=0)

    # Left-Right, Front-Back, Top-Bottom pass
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # Typically, there'd be another loop but we get rid of the loop with the following optimization.
            X = (N/2) * np.vstack([
                A[i - 1, j, 1:N+1],
                B[i + 1, j, 1:N+1],
                C[i, j - 1, 1:N+1],
                D[i, j + 1, 1:N+1],
                E[i, j, 0:N],
                F[i, j, 2:N+2],
            ])

            # Compute E[k] = M4_4.dot(X)[k] + M[4, 4]E[k - 1]
            m44 = M[4, 4] * (N/2)
            Y = np.concatenate((
                [E[i, j, 0]],
                M4_4.dot(np.delete(X, 4, axis=0))
            ))
            E[i, j, 0:N+1] = m44**np.arange(N + 1) * (Y / (m44**np.arange(N + 1))).cumsum()

            X[4] = (N/2) * E[i, j, 0:N]

            # 0 < Omega < 2 for https://en.wikipedia.org/wiki/Successive_over-relaxation
            A[i, j, 1:N+1], B[i, j, 1:N+1], C[i, j, 1:N+1], D[i, j, 1:N+1], E[i, j, 1:N+1], F[i, j, 1:N+1] = \
                omega * M.dot(X) + (1 - omega) * np.array([
                    A[i, j, 1:N+1],
                    B[i, j, 1:N+1],
                    C[i, j, 1:N+1],
                    D[i, j, 1:N+1],
                    E[i, j, 1:N+1],
                    F[i, j, 1:N+1],
                ])

    # Right-Left, Back-Front, Bottom-Top pass
    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            X = (N/2) * np.vstack([
                A[i - 1, j, 1:N+1],
                B[i + 1, j, 1:N+1],
                C[i, j - 1, 1:N+1],
                D[i, j + 1, 1:N+1],
                E[i, j, 0:N],
                F[i, j, 2:N+2],
            ])

            m55 = M[5, 5] * (N/2)
            Y = np.concatenate((
                M5_5.dot(X[:-1, :]),
                [F[i, j, N+1]],
            ))
            F[i, j, 1:] = (Y * (m55**np.arange(N + 1)))[::-1].cumsum()[::-1] / m55**np.arange(N + 1)
            X[5] = (N/2) * F[i, j, 2:N+2]

            A[i, j, 1:N+1], B[i, j, 1:N+1], C[i, j, 1:N+1], D[i, j, 1:N+1], E[i, j, 1:N+1], F[i, j, 1:N+1] = \
                omega * M.dot(X) + (1 - omega) * np.array([
                    A[i, j, 1:N+1],
                    B[i, j, 1:N+1],
                    C[i, j, 1:N+1],
                    D[i, j, 1:N+1],
                    E[i, j, 1:N+1],
                    F[i, j, 1:N+1],
                ])

    return [A, B, C, D, E, F]
