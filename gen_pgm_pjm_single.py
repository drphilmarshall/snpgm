#!/usr/bin/env python

from matplotlib import rc
from daft import PGM, Node, Plate
rc("font", family="serif", size=12)
rc("text", usetex=True)


pgm = PGM([6, 4.2], origin=[0., 0.2], observed_style='inner')

# x_1 and c distributions on top line
# pgm.add_node(Node("hyperM", r"$M_0,\sigma_{\mathrm{int}}$", 3, 4, aspect=1.5))
# pgm.add_node(Node("hyperx1", r"$\bar{x_1},\sigma_{x_1}$", 4, 4, aspect=1.5))
# pgm.add_node(Node("hyperc", r"$\bar{c},\sigma_c$", 5, 4, aspect=1.5))

# Per-SN parameters:  top line in the plate
# pgm.add_node(Node("Mi", r"$M_i$", 3, 3))
pgm.add_node(Node("x1i", r"$x_{1,i}$", 4, 3))
pgm.add_node(Node("ci", r"$c_i$", 5, 3))

# Per-SN parameters: second line in the plate
pgm.add_node(Node("x0i", r"$x_{0,i}$", 3, 2))
pgm.add_node(Node("t0", r"$t_{0,i}$", 5, 2))

# Per-SN parameters: third line in the plate
pgm.add_node(Node("zi", r"$z_i$", 2, 1, observed=True))

# Observed photometry
pgm.add_node(Node("fij", r"$f_{i,j}$", 4, 1, observed=True))
pgm.add_node(Node("noise", r"$\sigma_{i,j}$", 5, 1, observed=True))


# Big Plate: SNe
pgm.add_plate(Plate([1.5, 0.5, 4, 3.],
                    label=r"SN $i = 1$",
                    shift=-0.1))

# Cosmological parameters
# pgm.add_node(Node("cosmology", r"$\Omega$", 1, 2))

# Nuisance parameters
# pgm.add_node(Node("nuisance", r"$\alpha, \beta$", 0.7, 3, aspect=1.5))

# Add in the edges.
# pgm.add_edge("hyperx1", "x1i")
# pgm.add_edge("hyperc", "ci")
# pgm.add_edge("hyperM", "Mi")

# pgm.add_edge("x1i", "x0i")
# pgm.add_edge("ci", "x0i")
# pgm.add_edge("Mi", "x0i")

# pgm.add_edge("cosmology", "x0i")
# pgm.add_edge("nuisance", "x0i")

# pgm.add_edge("zi", "x0i")

pgm.add_edge("x0i", "fij")
pgm.add_edge("x1i", "fij")
pgm.add_edge("ci", "fij")

pgm.add_edge("zi", "fij")
pgm.add_edge("t0", "fij")
pgm.add_edge("noise", "fij")

# Render and save.
pgm.render()
pgm.figure.savefig("snpgm_pjm_single.png", dpi=150)
