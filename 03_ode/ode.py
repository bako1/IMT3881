import numpy as np
import unittest


def eksplisitt(f, n, t0, t_end, y0):
    """
    Løs ode-en med eksplisitt metode.

    Løser y' = f(y) for y(t) fra t0 til t_end i n steg med y(t0) = y0.

    Paramters
    ---------
    f : func
        Funksjonen som beskriver differensialligningen
    n : int
        Antall steg
    t0 : float
        Starttidspunkt
    t_end: float
        Sluttidspunkt
    y0 : float
        Initialverdi

    Returns
    -------
    array:
        Beregnede verdier for y(t)
    """
    delta_t = (t_end - t0) / n
    y_verdier = np.zeros(n + 1)  # allocate the space
    y_verdier[0] = y0
    for i in range(n):
        y_verdier[i + 1] = y_verdier[i] + delta_t * f(y_verdier[i])
    return y_verdier


def heun(f, n, t0, t_end, y0):
    """
    Løs ode-en med Heuns metodel

    Løser y' = f(y) for y(t) fra t0 til t_end i n steg med y(t0) = y0.

    Paramters
    ---------
    f : func
        Funksjonen som beskriver differensialligningen
    n : int
        Antall steg
    t0 : float
        Starttidspunkt
    t_end: float
        Sluttidspunkt
    y0 : float
        Initialverdi

    Returns
    -------
    array:
        Beregnede verdier for y(t)
    """
    delta_t = (t_end - t0) / n
    y_verdier = np.zeros(n + 1)  # allocate the space
    y_verdier[0] = y0
    for i in range(n):
        y_verdier[i + 1] = y_verdier[i] + \
                          .5 * delta_t * (f(y_verdier[i]) +
                                     f(y_verdier[i] +
                                       delta_t * f(y_verdier[i])))
    return y_verdier


# Tester

class test_ode(unittest.TestCase):

    def test_eksplisitt(self):
        y = eksplisitt(lambda x: x, 1, 0, 1, 1)
        self.assertAlmostEqual(y[-1], 2)

    def test_heun(self):
        y = heun(lambda x: x, 1, 0, 1, 1)
        self.assertAlmostEqual(y[-1], 2.5)
