import numpy as np
import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from tqdm import tqdm

import mwpc_implementation as rivelatore


#################################
#          ESPERIMENTO          #
#################################

class esperimento():

    def __init__(self, cp):
        self.coppie_ei=np.empty(0)
        self.ei_rilevate=np.empty(0)
        self.riv_gen=np.empty(0)
        self.t_deriva=np.empty(0)
        self.tmin_deriva=np.empty(0)
        self.tmean_deriva=np.empty(0)

        self.set="SET 1"
        self.params=('su', 'sf', 'nr', 'tc')
        self.v1= np.array([1e-5, 10e-5, 1e7, 1e-12]) #1e-7
        self.v2= np.array([1e-4, 5e-5, 1e4, 1e-12]) #5e-5

        self.cam=cp

    def setting(self):
        print('SET 1: \n----- \n')
        for l,k in zip(self.params, self.v1):
            print(l, '=', k, '\n')
        print('SET 2: \n----- \n')
        for l,k in zip(self.params, self.v2):
            print(l, '=', k, '\n')
        while(True):
            select=input(' Select setting:')
            if(select == 'SET 1'):
                break
            if(select == 'SET 2'):
                self.set="SET 2"
                break
        
    def sim(self, n):
        for l, k in zip (range(n), tqdm(range(n), desc=" Simulazione in corso...")):
            SIM=rivelatore.mwpc_diffusion(self.cam)
            SIM.setting2(self.set)
            SIM.diff_process(self.cam)
            self.coppie_ei=np.append(self.coppie_ei, SIM.nei_pair)
            self.ei_rilevate=np.append(self.ei_rilevate, SIM.nei_riv)
            if(SIM.nei_td.size > 0):
                self.t_deriva=np.append(self.t_deriva, SIM.nei_td[-1])
            if(SIM.nei_td.size > 0):
                self.tmin_deriva=np.append(self.tmin_deriva, np.min(SIM.nei_td[-1]))
            if(SIM.nei_td.size > 0):
                self.tmean_deriva=np.append(self.tmean_deriva, np.mean(SIM.nei_td[-1]))
            if(self.coppie_ei[-1] > 0):
                self.riv_gen=np.append(self.riv_gen, (self.ei_rilevate[-1]/self.coppie_ei[-1]))

# Calcolo Efficienza di Rivelazione
def efficienza_mwpc(e):
    ''' 
    Funzione che calcola l'efficienza del rivelatore a gas

    Restituisce:
    ------------
    eff_e : efficienza di rivelazione di un elettrone
    eff_p : efficienza di rivelazione di una particella carica al nanosecondo
    '''

    eff_e=np.nanmean(e.riv_gen)
    eff_p=np.empty(0)
    for i in range(len(e.riv_gen)):
        if(e.t_deriva[i]>0):
            eff_p=np.append(eff_p, e.riv_gen[i]/(e.t_deriva[i]*1e9)) #particelle al nanosecondo

    return eff_e, np.mean(eff_p)



#################################
#         DISTRIBUZIONI         #
#################################

#DISTRIBUZIONE PARTICELLE
def particles_distr(e, efficienza_media, N):

    e_label=str(np.round(efficienza_media, 3)*100)
    xx1=np.linspace(0, 501, 500)
    mosaic_layout=[["A", "B"],
                   ["A", "B"],
                   ["C", "C"]]
    fig, ax=plt.subplot_mosaic(mosaic_layout, figsize= (7, 6), layout='constrained', facecolor='lightgrey')
    fig.suptitle(' Eventi per {:d} simulazioni'.format(N), color='black', fontsize=13)

    ax["A"].set_title('Distribuzione delle coppie elettroni-ioni generate', loc='left', color='black', fontsize=10)
    ax["A"].hist(e.coppie_ei, bins=12, color= 'skyblue', alpha=0.9)
    ax["A"].set_xlabel('coppie e-i', fontsize=9)
    ax["A"].set_ylabel('numero occorrenze', fontsize=9)

    ax["B"].set_title('Distribuzione delle cariche rilevate', loc='left', color='black', fontsize=10)
    ax["B"].hist(e.ei_rilevate, bins=10, color='steelblue', alpha=0.8)
    ax["B"].set_xlabel('cariche rivelate', fontsize=9)
    ax["B"].set_ylabel('numero occorrenze', fontsize=9)

    ax["C"].set_title('Coppie Generate/Cariche Rivelate', color='black', fontsize=10)
    ax["C"].scatter(xx1, (e.ei_rilevate/e.coppie_ei), s=45, marker='o', edgecolor='steelblue', color='skyblue', alpha=0.8)
    ax["C"].set_xlabel('coppie generate/cariche rivelate', fontsize=8)
    ax["C"].set_ylabel('numero occorrenze', fontsize=9)
    ax["C"].axhline(1, color='darkred', linewidth=2)
    ax["C"].axhline(efficienza_media, color='red', linewidth=1.5, label='efficienza media= '+e_label+" %")
    ax["C"].set_ylim(-1, 2)
    ax["C"].legend()

    for axs in fig.get_axes():
        axs.set_facecolor('whitesmoke')
        axs.tick_params(axis='both', labelsize=8)

    return fig


#DISTRIBUZIONI TEMPI DI DERIVA
def time_distr(e):
    conv=1e9
    fig= plt.figure(figsize=(6, 7), facecolor='lightgrey', layout='constrained')
    gs = fig.add_gridspec(3,1, hspace=0.1, wspace=0)
    ax1,ax2, ax3= gs.subplots()
    fig.suptitle('Distribuzione dei Tempi di Deriva', fontsize=13)

    ax1.set_title('Distribuzione dei tempi di deriva degli elettroni', color='black', fontsize=11)
    ax1.hist(conv*e.t_deriva, bins=12, color= 'darkseagreen', alpha=0.9)
    ax1.set_xlabel('tempi di deriva (ns)', fontsize=9)
    ax1.set_ylabel('numero occorrenze', fontsize=9)

    ax2.set_title('Distribuzione del tempo di deriva minimo per evento', color='black', fontsize=11)
    ax2.hist(conv*e.tmin_deriva, bins=12, color='darkseagreen', alpha=0.9)
    ax2.set_xlabel('tempi minimi per evento (ns)', fontsize=9)
    ax2.set_ylabel('numero occorrenze', fontsize=9)

    ax3.set_title('Distribuzione del tempo di deriva medio per evento', color='black', fontsize=11)
    ax3.hist(conv*e.tmean_deriva, bins=10, color='darkseagreen', alpha=0.9)
    ax3.set_xlabel('tempi medi per evento (ns)', fontsize=9)
    ax3.set_ylabel('numero occorrenze', fontsize=9)

    for axs in fig.get_axes():
        axs.set_facecolor('whitesmoke')
        axs.tick_params(axis='both', labelsize=8)

    return fig