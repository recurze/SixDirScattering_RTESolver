## Problem

Solve simplied Radiative Transfer Equation (RTE) with 6 directions with scattering only.

```math
\begin{align*}
    \frac{\partial F_1}{\partial x} &= \sigma (\frac{1}{6} \Sigma F_i - F_1) \\[1em]
    -\frac{\partial F_2}{\partial x} &= \sigma (\frac{1}{6} \Sigma F_i - F_2) \\[1em]
    \frac{\partial F_3}{\partial y} &= \sigma (\frac{1}{6} \Sigma F_i - F_3) \\[1em]
    -\frac{\partial F_4}{\partial y} &= \sigma (\frac{1}{6} \Sigma F_i - F_4) \\[1em]
    \frac{\partial F_5}{\partial z} &= \sigma (\frac{1}{6} \Sigma F_i - F_5) \\[1em]
    -\frac{\partial F_6}{\partial z} &= \sigma (\frac{1}{6} \Sigma F_i - F_6)
\end{align*}
```

With boundary conditions

```math
\begin{align*}
    F_1(-1, y, z) &= F_b(y, z) \\
    F_3(x, -1, z) &= F_b(x, z) \\
    F_5(x, y, -1) &= F_b(x, y) \\
    F_2(1, y, z) &= 0 \\
    F_4(x, 1, z) &= 0 \\
    F_6(x, y, 1) &= 0
\end{align*}
```

(If any of the terms related to the physics is incorrect, please forgive me.)

## Methods

1. Fixed-point (FP) iteration with relaxation.
2. Symmetric Gauss-Seidel (SGS) method with SOR.
3. Multicolor Gauss-Seidel (MGS) (if you have a lot of time).

See report for description and results.
