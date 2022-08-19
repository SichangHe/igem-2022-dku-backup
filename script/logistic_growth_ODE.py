"""
Reference: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.06-Python-ODE-Solvers.html
"""
from numpy import linspace, ndarray
from scipy.integrate import solve_ivp
from matplotlib import pyplot


P: ndarray
"""Population points"""

K: float = 1000_000
"""Capacity"""

r: float = 1
"""Growth rate"""


def dPdt(_t: float, P: float):
    """dP/dt at given `P` and `_t`"""
    return r * P * (1 - P / K)


def main(P_0=[100], t=[0, 20]):
    """
    Plot logistic growth curve
    given initial population `P_0`
    and time points `t`
    """
    # Solve initial value problem
    P = solve_ivp(dPdt, t, P_0, t_eval=linspace(t[0], t[1]))

    # Plot results
    pyplot.plot(P.t, P.y[0])
    pyplot.xlabel("t")
    pyplot.ylabel("P(t)")
    pyplot.show()


if __name__ == "__main__":
    main()
