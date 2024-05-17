#Esercitazione 5 esercizio 2

#Dati
#python3 get_data.py --year 2023 --exn 5 --outdir percorso/cartella/esercitazione

import sys, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import reco 

#FUNCTIONS and TOOLS
def Delta_ht(list):
    delta=np.empty(0)
    for i in range(1, len(list)):
        term= (list[i] - list[i-1])
        delta= np.append(delta, term)
    return delta

def Delta1_ht(hits):
    delta=np.empty(0)
    for i in range(1,len(hits)):
        term=hits[i]-hits[i-1]
        delta = np.append(delta, term)
    return delta

def dati_to_events(datas):
    eventi=np.empty(0)
    for i in range(1, datas.shape[0]):
        m=int(datas['mod_id'][i])
        d=int(datas['det_id'][i])
        h=int(datas['hit_time'][i])
        term= reco.Hit(m,d,h)
        eventi=np.append(eventi,term)
    return eventi

def all_reco(a1, a2): #a1 e a2 sono già ordinati temporalmente.
    delta= np.empty(0)
    s=0
    z=0
    while(s < len(a1) and z < len(a2)):
        min=a1[s]
        if (a1[s] < a2[z]):
            min=a2[z]
            z=z+1
        else: s=s+1
        delta=np.append(delta, min)
    if(s < len(a1)):
        for i in range(s, len(a1)):
            delta= np.append(delta, a1[i])
    elif(z < len(a1)):
        for i in range(z, len(a2)):
            delta= np.append(delta, a2[i])
    return delta

#PASSO 1
M0_events=pd.read_csv('/home/nicola_polito/get-mcf-data/dati/ex5_data/hit_times_M0.csv')
M1_events=pd.read_csv('/home/nicola_polito/get-mcf-data/dati/ex5_data/hit_times_M1.csv')
M2_events=pd.read_csv('/home/nicola_polito/get-mcf-data/dati/ex5_data/hit_times_M2.csv')
M3_events=pd.read_csv('/home/nicola_polito/get-mcf-data/dati/ex5_data/hit_times_M3.csv')


print(M0_events.head())
print(M0_events.columns)

# Hist Hit-Time
fig1 = plt.figure()
gs = fig1.add_gridspec(2,2, hspace=0.2, wspace=0)
(ax1,ax2), (ax3, ax4) = gs.subplots()
plt.suptitle(' Hit_time hitogram for different detectors ', fontsize=13, color = 'red')

#M0
M0_log_events= np.log10(M0_events['hit_time'])
n, bis, p = ax1.hist(M0_log_events, bins=40, range=(5,9.5), color='darkslategray')
ax1.set_title('M0', color='navy', fontsize=10)
ax1.set_ylabel('events', fontsize=8)
ax1.set_xlabel('Log(hit_time) (ns)', fontsize=8)
ax1.tick_params(axis='x', size=5)
ax1.tick_params(axis='y',size=5)

#M1
M1_log_events= np.log10(M1_events['hit_time'])
n, bis, p = ax2.hist(M1_log_events, bins=40, range=(5,9.5), color='c')
ax2.set_title('M1', color='navy', fontsize=10)
ax2.set_ylabel('events', fontsize=8)
ax2.set_xlabel('Log(hit_time) (ns)', fontsize=8)

#M2
M2_log_events= np.log10(M2_events['hit_time'])
n, bis, p = ax3.hist(M2_log_events, bins=40, range=(5,9.5), color='slategray')
ax3.set_title('M2', color='navy', fontsize=10)
ax3.set_ylabel('events', fontsize=8)
ax3.set_xlabel('Log(hit_time) (ns)', fontsize=8)
ax3.tick_params(axis='x', size=5)
ax3.tick_params(axis='y',size=5)

#M3
M3_log_events= np.log10(M3_events['hit_time'])
n, bis, p = ax4.hist(M3_log_events, bins=40, range=(5,9.5), color='aquamarine')
ax4.set_title('M3', color='navy', fontsize=10)
ax4.set_ylabel('events', fontsize=8)
ax4.set_xlabel('Log(hit_time) (ns)', fontsize=8)

for ax in fig1.get_axes():
    ax.label_outer()

plt.show()

#Hist Delta Hit Time
fig2 = plt.figure()
gs = fig2.add_gridspec(2,2, hspace=0.2, wspace=0)
(ax1,ax2), (ax3, ax4) = gs.subplots()
plt.suptitle('$\Delta$ Hit_time histogram for different detectors ', fontsize=13, color = 'red')

#M0
delta_M0=Delta_ht(M0_events['hit_time'])
dM0_log_events=np.log10(delta_M0)
n, bis, p = ax1.hist(dM0_log_events, bins=30, range=(-0.5, 7.5), color='darkslategray')
ax1.set_title('M0', color='navy', fontsize=10)
ax1.set_ylabel('events', fontsize=8)
ax1.set_xlabel('$Log(\Delta$ hit_time) (ns)', fontsize=8)
ax1.tick_params(axis='x', size=5)
ax1.tick_params(axis='y',size=5)

#M2
delta_M1=Delta_ht(M1_events['hit_time'])
dM1_log_events=np.log10(delta_M1)
dM1_log_events=np.log10(Delta_ht(M1_events['hit_time']))
n, bis, p = ax2.hist(dM1_log_events, bins=30, range=(-0.5, 7.5), color='c')
ax2.set_title('M1', color='navy', fontsize=10)
ax2.set_ylabel('events', fontsize=8)
ax2.set_xlabel('$Log(\Delta$ hit_time) (ns)', fontsize=8)

#M2
delta_M2=Delta_ht(M2_events['hit_time'])
dM2_log_events=np.log10(delta_M2)
dM2_log_events=np.log10(Delta_ht(M2_events['hit_time']))
n, bis, p = ax3.hist(dM2_log_events, bins=30, range=(-0.5, 7.5), color='slategray')
ax3.set_title('M2', color='navy', fontsize=10)
ax3.set_ylabel('events', fontsize=8)
ax3.set_xlabel('$Log(\Delta$ hit_time) (ns)', fontsize=8)
ax3.tick_params(axis='x', size=5)
ax3.tick_params(axis='y',size=5)

#M3
delta_M3=Delta_ht(M3_events['hit_time'])
dM3_log_events=np.log10(delta_M3)
dM3_log_events=np.log10(Delta_ht(M3_events['hit_time']))
n, bis, p = ax4.hist(dM3_log_events, bins=30, range=(-0.5, 7.5), color='aquamarine')
ax4.set_title('M3', color='navy', fontsize=10)
ax4.set_ylabel('events', fontsize=8)
ax4.set_xlabel('$Log(\Delta $hit_time) (ns)', fontsize=8)

for ax in fig2.get_axes():
    ax.label_outer()

plt.show()

fig1.savefig('E5/hit_time hist.png')
fig2.savefig('E5/delta_hit_time hist.png')

'''
INTERPRETAZIONE DEI GRAFICI:
Gli istogrammi degli hit times per i 4 differenti moduli mostrano che ci sono molti eventi di hit verso la fine dell'acquisizione(in particolare intorno ai 0.7 s) 
 e pochi all'inizio della stessa e ciò è vero per tutti e 4 i moduli.
Gli istogrammi della differenza tra due hit time successivi mostrano che vi sono degli eventi che hanno uno delta_hit molto piccolo (eventi molto vicini tra di loro), 
mentre quasi tutti gli altri presentano una differenza temporale molto più significativa. In particolare, quasi nessun evento ha una distanza temporale dal successivo compresa tra 40 e 5600 ns 
e, poichè gli hit appartenenti ad uno stesso evento saranno presumibilmente raggruppati nel tempo, mentre hit relativi ad eventi diversi avranno una separazione temporale maggiore,
ciò distingue tra un evento di interesse e un evento di non interesse.
Complessivamente si può evincere che si hanno eventi di interesse verso la fine dell'acquisizione registrati da tutti e 4 i moduli.
'''

#PASSO 3
#reco.Hit arrays
print(type(M0_events))

array_M0_events= dati_to_events(M0_events) 
array_M1_events= dati_to_events(M1_events)
array_M2_events= dati_to_events(M2_events)
array_M3_events= dati_to_events(M3_events)

print(type(array_M0_events[3])) #array di reco.Hit
print(type(array_M0_events[3].id_module)) #ora sono int

print('\n')
print(array_M0_events[0], '\n')

#all_reco.Hit
arr1=all_reco(array_M0_events, array_M1_events)
print(len(arr1)) # dovrebbe essere 20384
arr2=all_reco(arr1, array_M2_events)
print(len(arr2)) # dovrebbe essere 30577
all_ord_events=all_reco(arr2, array_M3_events)
print(len(all_ord_events)) #dovrebbe essere 40730


#Istogramma dei delta_t tra RECO.HIT consecutivi
delta_all= Delta1_ht(all_ord_events)
print(len(delta_all)) #dovrebbe essere 40729
delta_all_log= np.log10(delta_all)

n, bis, p = plt.hist(delta_all_log, bins=35, range=(-0.5, 7.5), color='darkslategray', label='all_events')
plt.suptitle('Hinstogram of $\Delta_t$ for all hits', color='red')
plt.xlabel('$Log(\Delta$ hit_time)', fontsize=10)
plt.ylabel('Events', fontsize=10)
plt.legend(fontsize=10)
plt.show()
plt.savefig('E5/delta_t for all hits.png')

#Come stabilire la finestra temporale da applicare ai $\Delta t$ che permetta di raggruppare gli *Hit* dello stesso evento ma separi quelli apparteneti ad eventi differenti?