import unittest
import numpy as np


def rektangel(f, a, b, n, pos='venstre'):
    """
    Numerisk integrasjon av funksjonen f med midt punkt metode)

    Parameters
    ----------
    f : function
        Funksjonen som skal integreres
    a : float
        Startverdi for integrasjonsintervallet
    b : float
        Sluttverdi for integrasjonsintervallet
    n: antall rektangel
    pos: hvilket punkt integreringen går på
         

    Returns
    -------
    float :
        Tilnærmet verdi for integralet
    """
    h=(b-a)/n
    if pos=='venstre':
        start=a
    elif pos=='midt':
        start=a+h/2.0
    else:
        start=a+h
    resultat=0
    for i in range(n):
        resultat+=f((start)+ i*h)
    resultat *= h
    return resultat


def f_feilanalyse(x):
   
    
    """
bregner og returnerersvaret 
    Parameters
    ----------
    f : x float/int
    

    Returns
    -------
    float :
        Tilnærmet verdi for bregnet svar
    """
    return (1 + x) * np.exp(x)





# Tester

class test_integrasjon(unittest.TestCase):

    def test_rektangel(self):
        v_f_verdi=(1+1.5*np.exp(0.5))*0.5 #integrert vhm venstre punkt
        m_f_verdi=0.5*(1.25*np.exp(0.25) + 1.75*np.exp(0.75)) #integrert vhm midt punkt
        h_f_verdi=0.5*(1.5*np.exp(0.5)+2*np.e) #integrert vhm høyre punkt
        
        test_venstre=rektangel(f_feilanalyse, 0, 1, 2, pos='venstre')
        self.assertAlmostEqual(test_venstre,v_f_verdi )
        test_midt=rektangel(f_feilanalyse,0,1,2, pos='midt')
        self.assertAlmostEqual(test_midt,m_f_verdi)
        test_høyre=rektangel(f_feilanalyse, 0, 1, 2, pos='høyre')
        self.assertAlmostEqual(test_høyre, h_f_verdi)

