"""
Reference: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.06-Python-ODE-Solvers.html
"""
from matplotlib.pyplot import plot, xlabel, ylabel, legend, show
from numpy import linspace, ndarray
from scipy.integrate import solve_ivp

P: ndarray
"""Population points"""

K: float = 1e6
"""Capacity"""

r: float = 1
"""Growth rate"""


def dPdt(_t: float, P: float):
    """dP/dt at given `P` and `_t`"""
    return r * P * (1 - P / K)


def main(P_0s=[0, 1, 1e3, 1e6], t=[0, 20]):
    """
    Plot logistic growth curve
    given initial population(s) `P_0s`
    and time span (`[start_time, end_time]`) `t`
    """
    # Solve initial value problem
    P = solve_ivp(dPdt, t, P_0s, t_eval=linspace(t[0], t[1]))

    # Plot results
    for y, P_0 in zip(P.y, P_0s):
        plot(P.t, y, label=f"P_0 = {P_0}")
    xlabel("t")
    ylabel("P(t)")
    legend()
    show()


if __name__ == "__main__":
    main()
