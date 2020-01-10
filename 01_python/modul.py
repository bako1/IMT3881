import unittest
import numpy as np

def f(x):
#def dobbel(x):
    """
    Beregner og returnerer summen av cos og sin.

    

    Paramters
    ---------
    x : float / int
        

    Returns
    -------
    float / int
        Den summerte verdien.
    """
    return np.sin(x)+np.cos(x)


class test_modul(unittest.TestCase):

    def test_f(self):
        self.assertEqual(f(0), 1)
        self.assertAlmostEqual(f(1), 1.38177329068)
