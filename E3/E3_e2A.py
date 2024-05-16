"""
Esercizio 2A(opzionale)

Creare uno script python che combini il grafico del punto 2.7 assieme
agli istogrammi dei punti 2.9 e 2.10 in un'unica immagine come in figura e salvi il risultato in un file png e in un file pdf.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#any function
def trova_extr(arr):
    val=[0,0]
    for i in arr:
        if(i>=val[0]):
            val[0]= i
        else:
            val[1]=i
    return val

#file data
df_fromfile=pd.read_csv('/home/nicola_polito/get-mcf-data/dati/ex3_data/4LAC_DR2_sel.csv')

#array for graphs
df_fsrq = df_fromfile.loc[(df_fromfile['CLASS'] == 'fsrq')]
df_bll = df_fromfile.loc[(df_fromfile['CLASS'] == 'bll')]

maxPL_fsrq = trova_extr(df_fsrq['PL_Index'])[0]
minPL_fsrq = trova_extr(df_fsrq['PL_Index'])[1]

maxPL_bll= trova_extr(df_bll['PL_Index'])[0]
minPL_bll= trova_extr(df_bll['PL_Index'])[1]

maxPL_fsrq = trova_extr(np.log10(df_fsrq['nu_syn']))[0]
minPL_fsrq = trova_extr(np.log10(df_fsrq['nu_syn']))[1]

maxPL_bll= trova_extr(np.log10(df_bll['nu_syn']))[0]
minPL_bll= trova_extr(np.log10(df_bll['nu_syn']))[1]



#Graphs
fig = plt.figure()
gs = fig.add_gridspec(2,2, hspace=0, wspace=0)
(ax1,ax2), (ax3, ax4) = gs.subplots()

plt.suptitle('fsrq and bll source', color='red')

ax3.scatter(df_fsrq['nu_syn'], df_fsrq['PL_Index'], color= 'darkslategray', s= 20, label='fsrq', alpha = 0.8)
ax3.scatter(df_bll['nu_syn'], df_bll['PL_Index'], color= 'red', s= 20, label='bll', alpha= 0.3)
ax3.set_xscale('log', base=10)
ax3.set_ylabel('PL_Index', fontsize=6)
ax3.set_xlabel('Log(nu_syn) [Hz]', fontsize=6)
ax3.legend(fontsize=8)

n, bis, p = ax1.hist(df_fsrq['PL_Index'], bins=50, range=(1.5, 3.5), color='darkslategray', alpha=0.8, label='fsrq source')
n, bis, p = ax1.hist(df_bll['PL_Index'], bins=50, range=(1.5, 3.5), color='red', alpha=0.4, label='bll source')
ax1.set_xlabel('PL_Index', fontsize=6)
ax1.set_ylabel('Number of sources', fontsize=6)
ax1.legend(fontsize=8)

n, bis, p = ax4.hist(np.log10(df_fsrq['nu_syn']), bins=50, range=(10, 22), orientation='horizontal', color='darkslategray', alpha=0.8, label='fsrq source')
n, bis, p = ax4.hist(np.log10(df_bll['nu_syn']), bins=50, range=(10, 22), orientation='horizontal', color='red', alpha=0.4, label='bll source')
ax4.set_ylabel('Log(nu_syn) [Hz]', fontsize=6)
ax4.set_xlabel('Number of sources', fontsize=6)
ax4.legend(fontsize=8)

for ax in fig.get_axes():
    ax.label_outer()

# Rimuovo assi per riqyadro non necessario
ax2.axis('off') #--> questo non sapevo come farlo, aggiunto opo averlo visto dalle soluzioni
plt.savefig('Blazars_4LAC_PL_index-SynPeak.png')
plt.show()