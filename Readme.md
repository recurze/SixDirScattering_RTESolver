## Problem

Solve simplied Radiative Transfer Equation (RTE) with 6 directions with scattering only.

$$
    \pdv{F_1}{x} = \sigma (\frac{1}{6} \Sigma F_i - F_1)
    -\pdv{F_2}{x} = \sigma (\frac{1}{6} \Sigma F_i - F_2)
    \pdv{F_3}{y} = \sigma (\frac{1}{6} \Sigma F_i - F_3)
    -\pdv{F_4}{y} = \sigma (\frac{1}{6} \Sigma F_i - F_4)
    \pdv{F_5}{z} = \sigma (\frac{1}{6} \Sigma F_i - F_5)
    -\pdv{F_6}{z} = \sigma (\frac{1}{6} \Sigma F_i - F_6)
$$

With boundary conditions

$$
    F_1(-1, y, z) = F_b(y, z)
    F_3(x, -1, z) = F_b(x, z)
    F_5(x, y, -1) = F_b(x, y)
    F_2(1, y, z) = 0
    F_4(x, 1, z) = 0
    F_6(x, y, 1) = 0
$$

(If any of the terms related to the physics is incorrect, please forgive me.)

## Methods

1. Fixed-point (FP) iteration with relaxation.
2. Symmetric Gauss-Seidel (SGS) method with SOR.
3. Multicolor Gauss-Seidel (MGS) (if you have a lot of time).

See report for description and results.
