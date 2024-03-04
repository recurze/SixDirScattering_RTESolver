import matplotlib.pyplot as plt
import numpy as np


def plot_heatmap(data: np.ndarray,
                 ax: plt.Axes,
                 xlabel: str = 'x',
                 ylabel: str = 'y'):
    N = data.shape[0]
    X, Y = np.meshgrid(np.linspace(-1, 1, N), np.linspace(-1, 1, N))
    pcm = ax.pcolormesh(X, Y, data, cmap="inferno", clim=(0, 1))
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    return pcm


def visualize_2d(density: list[np.ndarray], plane: float, sigma: float):
    N = density[0].shape[0] - 2
    idx = int(((1 + plane)*N + 1)/2)

    fig = plt.figure(figsize=(9, 8), constrained_layout=True)
    subfig = fig.subfigures(nrows=3, ncols=1)

    data = density[0]
    axes = subfig[0].subplots(nrows=1, ncols=3)
    pcm = plot_heatmap(data[idx, :, :], axes[0], xlabel='y', ylabel='z')
    pcm = plot_heatmap(data[:, idx, :], axes[1], xlabel='x', ylabel='z')
    pcm = plot_heatmap(data[:, :, idx], axes[2], xlabel='x', ylabel='y')
    fig.colorbar(pcm, ax=axes.ravel().tolist())
    subfig[0].suptitle(f"A on x={plane}, y={plane} and z={plane} for sigma={sigma}")

    data = density[1]
    axes = subfig[1].subplots(nrows=1, ncols=3)
    pcm = plot_heatmap(data[idx, :, :], axes[0], xlabel='y', ylabel='z')
    pcm = plot_heatmap(data[:, idx, :], axes[1], xlabel='x', ylabel='z')
    pcm = plot_heatmap(data[:, :, idx], axes[2], xlabel='x', ylabel='y')
    fig.colorbar(pcm, ax=axes.ravel().tolist())
    subfig[1].suptitle(f"B on x={plane}, y={plane} and z={plane} for sigma={sigma}")

    data = sum(density)
    axes = subfig[2].subplots(nrows=1, ncols=3)
    pcm = plot_heatmap(data[idx, :, :], axes[0], xlabel='y', ylabel='z')
    pcm = plot_heatmap(data[:, idx, :], axes[1], xlabel='x', ylabel='z')
    pcm = plot_heatmap(data[:, :, idx], axes[2], xlabel='x', ylabel='y')
    fig.colorbar(pcm, ax=axes.ravel().tolist())
    subfig[2].suptitle(f"Total intensity on x={plane}, y={plane} and z={plane} for sigma={sigma}")


def visualize_3d(data: np.ndarray, plane: float, title: str):
    N = data.shape[0]

    x = np.linspace(-1, 1, N)
    y = np.linspace(-1, 1, N)
    z = np.linspace(-1, 1, N)

    X, Y, Z = np.meshgrid(x, y, z)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    maskx = (plane - 1.5/N < X) & (X < plane + 1.5/N)
    masky = (plane - 1.5/N < Y) & (Y < plane + 1.5/N)
    maskz = (plane - 1.5/N < Z) & (Z < plane + 1.5/N)
    mask = maskx | masky | maskz

    scatter = ax.scatter(X[mask], Y[mask], Z[mask], c=data[mask])
    fig.colorbar(scatter, ax=ax)

    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
