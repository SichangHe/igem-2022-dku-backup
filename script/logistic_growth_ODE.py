from numpy import linspace, ndarray
from scipy.integrate import odeint
from matplotlib import pyplot


P: ndarray
"""Population points"""

K: float = 1000_000
"""Capacity"""

r: float = 1
"""Growth rate"""


def dPdt(P: float, _t: float):
    """dP/dt at given `P` and `_t`"""
    return r * P * (1 - P / K)


def main(P_0=100, t=linspace(0, 20)):
    """
    Plot logistic growth curve
    given initial population `P_0`
    and time points `t`
    """
    # Solve ODE
    P: ndarray = odeint(dPdt, P_0, t)

    # Plot results
    pyplot.plot(t, P)
    pyplot.xlabel("t")
    pyplot.ylabel("P(t)")
    pyplot.show()


if __name__ == "__main__":
    main()
