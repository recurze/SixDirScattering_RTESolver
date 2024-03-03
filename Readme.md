## Problem

Solve simplied Radiative Transfer Equation (RTE) with 6 directions with scattering only.

```math
\begin{align*}
    \pdv{F_1}{x} &= \sigma (\frac{1}{6} \Sigma F_i - F_1) \\[1em]
    -\pdv{F_2}{x} &= \sigma (\frac{1}{6} \Sigma F_i - F_2) \\[1em]
    \pdv{F_3}{y} &= \sigma (\frac{1}{6} \Sigma F_i - F_3) \\[1em]
    -\pdv{F_4}{y} &= \sigma (\frac{1}{6} \Sigma F_i - F_4) \\[1em]
    \pdv{F_5}{z} &= \sigma (\frac{1}{6} \Sigma F_i - F_5) \\[1em]
    -\pdv{F_6}{z} &= \sigma (\frac{1}{6} \Sigma F_i - F_6)
\end{align*}
```

With boundary conditions

```math
\begin{align*}
    \pdv{F_1}{x} &= \sigma (\frac{1}{6} \Sigma F_i - F_1) \\[1em]
    -\pdv{F_2}{x} &= \sigma (\frac{1}{6} \Sigma F_i - F_2) \\[1em]
    \pdv{F_3}{y} &= \sigma (\frac{1}{6} \Sigma F_i - F_3) \\[1em]
    -\pdv{F_4}{y} &= \sigma (\frac{1}{6} \Sigma F_i - F_4) \\[1em]
    \pdv{F_5}{z} &= \sigma (\frac{1}{6} \Sigma F_i - F_5) \\[1em]
    -\pdv{F_6}{z} &= \sigma (\frac{1}{6} \Sigma F_i - F_6)
\end{align*}
```

(If any of the terms related to the physics is incorrect, please forgive me.)

## Methods

1. Fixed-point (FP) iteration with relaxation.
2. Symmetric Gauss-Seidel (SGS) method with SOR.
3. Multicolor Gauss-Seidel (MGS) (if you have a lot of time).

See report for description and results.
