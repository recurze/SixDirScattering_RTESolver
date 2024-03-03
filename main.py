import argparse
import generic_solver

from method.fp import fp_iterator
from method.mgs import mgs_iterator
from method.sgs import sgs_iterator


def rgb(N: int) -> list[list[tuple[int, int, int]]]:
    r = [(i, j, k) for i in range(1, N + 1) for j in range(1, N + 1) for k in range(1, N + 1) if (i + j + k) % 3 == 0]
    g = [(i, j, k) for i in range(1, N + 1) for j in range(1, N + 1) for k in range(1, N + 1) if (i + j + k) % 3 == 1]
    b = [(i, j, k) for i in range(1, N + 1) for j in range(1, N + 1) for k in range(1, N + 1) if (i + j + k) % 3 == 2]
    return [r, g, b]


if __name__ == "__main__":
    iterator = {
        "sgs": sgs_iterator,
        "fp": fp_iterator,
        "mgs": mgs_iterator,
    }

    parser = argparse.ArgumentParser()
    parser.add_argument('sigma', type=float)
    parser.add_argument('--method', required=True,
                        choices=iterator.keys())
    parser.add_argument('--relax-param', type=float)
    parser.add_argument('--num-grid-points', type=int, default=100)
    parser.add_argument('--max-iter', type=int, default=1000)
    parser.add_argument('--threshold', type=float, default=1e-6)
    parser.add_argument('--plot', action="store_true")
    parser.add_argument('-v', '--verbose', action="store_true")
    args = parser.parse_args()

    relax_param_name = {
        "sgs": "omega",
        "fp": "relaxation",
        "mgs": "omega",
    }

    recommended_parameters = {
        "sgs": {
            0.1: 1,
            1: 1,
            10: 1.05,
            100: 1.37,
        },
        "fp": {
            0.1: 0,
            1: 0,
            10: -3,
            100: -40,
        },
    }

    relax = args.relax_param or recommended_parameters.get(args.method, {}).get(args.sigma)
    param = {relax_param_name[args.method]: relax} if relax is not None else {}

    if args.method == "mgs":
        param["colors"] = rgb(args.num_grid_points)

    init_density = generic_solver.get_init_density(args.num_grid_points)
    residuals, density = generic_solver.solve(density=init_density,
                                              sigma=args.sigma,
                                              next_estimator=iterator[args.method],
                                              maxiter=args.max_iter,
                                              threshold=args.threshold,
                                              verbose=args.verbose,
                                              **param)

    if args.plot:
        import matplotlib.pyplot as plt
        from visualize import visualize_2d, visualize_3d

        visualize_2d(density, 0, args.sigma)
        fname_2d = f"2d_{args.method}_{args.sigma}.jpg"
        plt.savefig(fname_2d)
        visualize_3d(sum(density), 0, f"Total intensity on x=0, y=0 and z=0 for sigma={args.sigma}")
        fname_3d = f"3d_{args.method}_{args.sigma}.svg"
        plt.savefig(fname_3d)
        print(f"Plots saved to {fname_2d} and {fname_3d}")
