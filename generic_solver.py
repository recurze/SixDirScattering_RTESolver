from typing import Callable
import numpy as np


def get_init_density(N: int = 100) -> list[np.ndarray]:
    A, B, C, D, E, F = [np.zeros((N + 2, N + 2, N + 2)) for i in range(6)]

    l, r = int(0.4 * N), int(0.6 * N) + 1
    A[0, l:r, l:r] = 1
    C[l:r, 0, l:r] = 1
    E[l:r, l:r, 0] = 1

    return [A, B, C, D, E, F]


def solve(density: list[np.ndarray],
          sigma: float,
          next_estimator: Callable,
          threshold: float = 1e-6,
          maxiter: int = 1000,
          verbose: bool = False,
          **kwargs) -> tuple[list[float], list[np.ndarray]]:
    print("Method parameters (omega/relaxation):", kwargs.get("omega", kwargs.get("relaxation", {})))

    residuals = []
    for i in range(maxiter):
        density_new = next_estimator(density, sigma, **kwargs)

        residual, density = compute_residual(density_new, sigma), density_new
        residuals.append(residual)

        if verbose:
            print(f"it={i} residual={residual:.8f}")

        if residual < threshold:
            print(f"{next_estimator.__name__} for sigma={sigma} completed {i} iterations: residual={residual:.8f}")
            break
    else:
        print(f"{next_estimator.__name__} for sigma={sigma} completed {maxiter} iterations: residual={residual:.8f}")

    return residuals, density


def compute_residual(density: list[np.ndarray], sigma: float) -> float:
    N = density[0].shape[0] - 2

    mean = sum(density)/6
    A, B, C, D, E, F = density

    resA = (N/2) * (A[1:-1, 1:-1, 1:-1] - A[:-2, 1:-1, 1:-1]) - sigma * (mean - A)[1:-1, 1:-1, 1:-1]
    resC = (N/2) * (C[1:-1, 1:-1, 1:-1] - C[1:-1, :-2, 1:-1]) - sigma * (mean - C)[1:-1, 1:-1, 1:-1]
    resE = (N/2) * (E[1:-1, 1:-1, 1:-1] - E[1:-1, 1:-1, :-2]) - sigma * (mean - E)[1:-1, 1:-1, 1:-1]

    resB = (N/2) * (B[1:-1, 1:-1, 1:-1] - B[2:, 1:-1, 1:-1]) - sigma * (mean - B)[1:-1, 1:-1, 1:-1]
    resD = (N/2) * (D[1:-1, 1:-1, 1:-1] - D[1:-1, 2:, 1:-1]) - sigma * (mean - D)[1:-1, 1:-1, 1:-1]
    resF = (N/2) * (F[1:-1, 1:-1, 1:-1] - F[1:-1, 1:-1, 2:]) - sigma * (mean - F)[1:-1, 1:-1, 1:-1]

    return sum(np.linalg.norm(res)**2 for res in [resA, resB, resC, resD, resE, resF]) ** 0.5
