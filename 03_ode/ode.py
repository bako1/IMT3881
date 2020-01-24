import numpy as np
import matplotlib.pyplot as plt
def eksplisitt(N,T,a,y_0):

    delta_t = T/N
    y_verdier_eks = np.zeros(N + 1) 
    n_verdier = np.arange(N + 1)
    t_verdier = delta_t * n_verdier
    y_verdier_eks[0] = y_0
    for i in range(N):
        y_verdier_eks[i + 1] = delta_t*a*y_verdier_eks[i]+y_verdier_eks[i]
    plt.plot(t_verdier, y_verdier_eks)
    return y_verdier_eks

def crank_nicolson(N,T,a,y_0):

    delta_t = T/N
    y_verdier_crank = np.zeros(N + 1) 
    n_verdier = np.arange(N + 1)
    t_verdier = delta_t * n_verdier
    y_verdier_crank[0] = y_0
    for i in range(N):
        y_verdier_crank[i + 1] = y_verdier_crank[i]*((1+ a*delta_t*0.5)/(1-a*delta_t*0.5))
    plt.plot(t_verdier, y_verdier_crank)

    return y_verdier_crank



def implisitt(N,T,a,y_0):
    delta_t = T/N
    n_verdier = np.arange(N + 1)
    y_verdier_impl = np.zeros(N + 1)  
    y_verdier_impl[0] = y_0
    t_verdier = delta_t * n_verdier

    
    for i in range(N):
        y_verdier_impl[i + 1] = y_verdier_impl[i]/(1-a*delta_t)
    plt.plot(t_verdier, y_verdier_impl)
    return y_verdier_impl

#eksplisitt(2,2,1,1)
