import unittest
import numpy as np


def ett_trapes(f, a, b):
    """
    Numerisk integrasjon av funksjonen f med ett trapes (ESC 1.3.1)

    Parameters
    ----------
    f : function
        Funksjonen som skal integreres
    a : float
        Startverdi for integrasjonsintervallet
    b : float
        Sluttverdi for integrasjonsintervallet

    Returns
    -------
    float :
        Tilnærmet verdi for integralet
    """
    return 0.5 * (b - a) * (f(a) + f(b))


def to_trapeser(f, a, b):
    """
    Numerisk integrasjon av funksjonen f med to trapeser (ESC 1.3.2)

    Parameters
    ----------
    f : function
        Funksjonen som skal integreres
    a : float
        Startverdi for integrasjonsintervallet
    b : float
        Sluttverdi for integrasjonsintervallet

    Returns
    -------
    float :
        Tilnærmet verdi for integralet
    """
    c = .5 * (a + b)            # midtpunkt
    return 0.25 * (b - a) * (f(a) + 2 * f(c) + f(b))


def n_trapeser(f, a, b, n):
    """
    Numerisk integrasjon av funksjonen f med n trapeser (ESC 1.3.3)

    Parameters
    ----------
    f : function
        Funksjonen som skal integreres
    a : float
        Startverdi for integrasjonsintervallet
    b : float
        Sluttverdi for integrasjonsintervallet
    n : int
        Antall trapeser

    Returns
    -------
    float :
        Tilnærmet verdi for integralet
    """
    h = (b - a) / n
    x_punkter = np.linspace(a, b, n + 1)
    return h * (0.5 * f(x_punkter[0]) +
                0.5 * f(x_punkter[-1]) +
                f(x_punkter[1:-1]).sum())


# Tester

class test_integrasjon(unittest.TestCase):

    def test_ett_trapes(self):
        ett_t = ett_trapes(lambda x: x, 0, 1)
        self.assertAlmostEqual(ett_t, .5)

    def test_to_trapeser(self):
        to_t = to_trapeser(lambda x: x, 0, 1)
        self.assertAlmostEqual(to_t, .5)

    def test_n_trapeser(self):
        n_t = n_trapeser(lambda x: x, 0, 1, 50)
        self.assertAlmostEqual(n_t, .5)
