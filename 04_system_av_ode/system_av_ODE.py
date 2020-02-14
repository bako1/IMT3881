{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import unittest\n",
    "\n",
    "\n",
    "def eksplisitt(f, n, t0, t_end,x0, y0,z0):\n",
    "    \"\"\"\n",
    "    Løs ode-en med eksplisitt metode.\n",
    "\n",
    "    Løser y' = f(y) for y(t) fra t0 til t_end i n steg med y(t0) = y0.\n",
    "\n",
    "    Paramters\n",
    "    ---------\n",
    "    f : func\n",
    "        Funksjonen som beskriver differensialligningen\n",
    "    n : int\n",
    "        Antall steg\n",
    "    t0 : float\n",
    "        Starttidspunkt\n",
    "    t_end: float\n",
    "        Sluttidspunkt\n",
    "    y0 : float\n",
    "        Initialverdi\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    array:\n",
    "        Beregnede verdier for y(t)\n",
    "    \"\"\"\n",
    "    delta_t = (t_end - t0) / n\n",
    "    x_verdier = np.zeros(n + 1)\n",
    "    y_verdier = np.zeros(n + 1)  # allocate the space\n",
    "    z_verdier = np.zeros(n + 1)\n",
    "\n",
    "    x_verdier[0] = x0\n",
    "    y_verdier[0] = y0\n",
    "    z_verdier[0] = z0\n",
    "\n",
    "\n",
    "    for i in range(n):\n",
    "        x_verdier[i + 1] = x_verdier[i] + delta_t * f(x_verdier[i])\n",
    "        y_verdier[i + 1] = y_verdier[i] + delta_t * f(y_verdier[i])\n",
    "        z_verdier[i + 1] = z_verdier[i] + delta_t * f(z_verdier[i])\n",
    "    denderiverte=np.f(x_verdier,y_verdier,z_verdier),g(x_verdier,y_verdier,z_verdier)\n",
    "    return denderiverte\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
