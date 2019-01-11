import unittest


def dobbel(x):
    """
    Beregner og returnerer den dobbelte verdien.

    Det er ikke mye å si om dette, men om man skulle ha lyst,
    kan man skrive en lengre utlegning om temaet dobling her.

    Paramters
    ---------
    x : float / int
        Tallet som skal dobles.

    Returns
    -------
    float / int
        Den doblede verdien.
    """
    return 2 * x


class test_modul(unittest.TestCase):

    def test_dobbel(self):
        self.assertEqual(dobbel(3), 6)
        self.assertAlmostEqual(dobbel(7.4), 14.8)
