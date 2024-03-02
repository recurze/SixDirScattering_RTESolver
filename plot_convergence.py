import generic_solver
import matplotlib.pyplot as plt

from method.fp import fp_iterator
from method.sgs import sgs_iterator
from typing import Optional


def plot_residuals(residuals: list[float], ax: plt.Axes, label: Optional[str] = None):
    ax.plot(residuals, label=label)
    ax.set_yscale("log")


def plot_residual_graphs(N: int = 100):
    ax = plt.gca()
    for omega, sigma in zip([1, 1, 1.05, 1.37], [0.1, 1, 10, 100]):
        residuals, _ = generic_solver.solve(generic_solver.get_init_density(N),
                                            sigma,
                                            sgs_iterator,
                                            omega=omega)
        plot_residuals(residuals, ax, label=f"sigma={sigma}")
    ax.set_ylim((10**-9, 10**4))

    plt.legend()
    plt.title("Convergence of SGS with relaxation")
    plt.xlabel("#iterations")
    plt.ylabel("residuals")
    plt.savefig("sgs_convergence.jpg")
    plt.cla()

    for relaxation, sigma in zip([0, 0, -3, -40], [0.1, 1, 10, 100]):
        residuals, _ = generic_solver.solve(generic_solver.get_init_density(N),
                                            sigma,
                                            fp_iterator,
                                            relaxation=relaxation)
        plot_residuals(residuals, ax, label=f"sigma={sigma}")

    ax.set_ylim((10**-9, 10**4))
    plt.legend()
    plt.title("Convergence of Fixed-point with relaxation")
    plt.xlabel("#iterations")
    plt.ylabel("residuals")
    plt.savefig("fp_convergence.jpg")
