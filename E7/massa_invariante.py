import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors 


########################################
#   CALCOLO DELLA MASSA INVARIANTE     #
########################################

# FUNZIONE MASSA INVARIANTE --------------------
def mc2(e,p1,p2):
    """Calcola la massa invariante di un decadimento a due corpi.

    Parametri:
    ---------
    e: list of float
        lista con valori dell'energia per ciascuna particella;
    p1,p2: list of float
        lista con valori della quantità di moto delle due particelle per ciascuna componente;

    Restituisce:
    -----------
    t3: float
        modulo del quadrimpulso di ciascuna coppia di prodotto di decadimento.
    """
    t3=0
    t1= (e[0] + e[1])**2
    t=np.empty(0)
    for j in range(3):
        t=np.append(t, (p1[j]+p2[j])**2)
    t2=np.sum(t)
    if((t1-t2)>0):
        t3=np.sqrt(t1-t2)
    else:
        t3=0
        print('Values Error!')
    return t3

# CALCOLO DISTRIBUZIONE MASSE INVARIANTI --------------------
def data_distr(data):
    #valori di energia e impulso dai dati
    E1=np.array(data.loc[:,['E1']], dtype=float)
    E2=np.array(data.loc[:,['E2']], dtype=float)
    E=np.array([E1, E2])

    P1 =np.array(data.loc[:,['px1','py1','pz1']], dtype=float)
    P2 =np.array(data.loc[:,['px2','py2','pz2']], dtype=float)

    #Calcolo distribuzione masse invarianti:
    d_m=np.empty(0)
    for j in range(P1.shape[0]):
        mass_inv=mc2(E[:,j], P1[j], P2[j])
        d_m=np.append(d_m, mass_inv)
    
    return d_m


########################################
# DISTRIBUZIONE DELLA MASSA INVARIANTE #
########################################

# ISTOGRAMMA DELLE MASSE INVARIANTI --------------------
def distr_hist(d_mass):
    fig, ax = plt.subplots(1,1, figsize=(6,4), layout='constrained', facecolor='lightgrey')
    nd, bins, p = ax.hist(d_mass, bins=125, color='blue', alpha=0.8)
    ax.set_facecolor('whitesmoke')
    ax.set_title('Distribuzione delle masse invarianti', fontsize=11)
    ax.set_ylabel('n.decadimenti '+r'$J/\psi \rightarrow \mu \mu $', fontsize=9)
    ax.set_xlabel(r'$mc^2$', fontsize=9)

    return nd, bins, p

#ISTOGRAMMA DELLE MASSE INVARIANTI CON INSERTO SUL PICCO
def distr_hist_peak(d_mass):
    fig, ax = plt.subplots(1,1, figsize=(6,4), layout='constrained', facecolor='lightgrey')
    ax.hist(d_mass, bins=125, color='blue', alpha=0.8)
    ax.set_facecolor('whitesmoke')
    ax.set_title('Distribuzione delle masse invarianti', fontsize=11)
    ax.set_ylabel('n.decadimenti '+r'$J/\psi \rightarrow \mu \mu $', fontsize=9)
    ax.set_xlabel(r'$mc^2$', fontsize=9)

    #inserto
    ins=ax.inset_axes([0.55, 0.5, 0.4, 0.5], facecolor='whitesmoke')
    ins.hist(d_mass, bins=125, color='blue', alpha=0.7)
    ins.set_xlim(2.8, 3.4)
    ins.tick_params(labelleft=False, labelsize=8)
    ins.set_xticks([2.8, 3.0, 3.2, 3.4])

    #freccia
    fc = colors.to_rgba('lightgrey')  # facecolor
    ec = colors.to_rgba('black')      # edgecolor

    # Imposta alpha solo per il facecolor
    fc = fc[:-1] + (0.5,)  # 0.5 = 50% trasparente
    ax.annotate("      ", xytext=(3.02, 260), xy=(3.6, 1400),
                bbox=dict(boxstyle="circle", facecolor=fc, edgecolor=ec, linewidth=1.0),
                arrowprops=dict(arrowstyle="-|>"))
