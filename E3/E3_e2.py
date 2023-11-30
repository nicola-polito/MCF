"""
Esercizio 2
Creare un secondo script python che:

    1.legga il file (4LAC_DR2_sel.csv) e crei il DtaFrame pandas corrispondente;
    2.stampi il nome delle colonne del DataFrame;
    3.stampi un estratto del contenuto del DataFrame;
    4.produca un grafico dell'indice spettrale (PL_Index) in funzione del flusso (Flux1000);
suggerimento: usare pyplot.scatter;
    5.produca un grafico dell'indice spettrale (PL_Index) in funzione del flusso (Flux1000) con asse x logaritmico;
    6.produca un grafico dell'indice spettrale (PL_Index) in funzione del logaritmo in base 10 della variabile nu_syn;
    7.produca un grafico dell'indice spettrale (PL_Index) in funzione del logaritmo in base 10 della variabile nu_syn distinguendo le sorgenti di classe (CLASS) bll e fsrq con la corrispondente legenda (gli altri tipi di sorgente non vanno considerate nel grafico);
suggerimento: usare .loc per la serezione dei valori nel DataFrame;
suggerimento: usare l'opzione alpha per la trasparenza;
    8.produca un grafico analogo a quello del punto 7 ma che mostri anche l'incertezza sulla stima dell'indice spettrale (Unc_PL_Index);
suggerimento: usare pyplot.errorbar;
    9.produca l'istogramma sovrapposto dell'indice spettrale per le sorgenti di tipo bll e fsrq con la relativa legenda;
suggerimento: usare pyplot.hist definendo lo stesso numero di bin e lo stesso intervallo per l'asse x;
suggerimento: usare l'opzione alpha per la trasparenza;
    10.produca un grafico analogo al precedente per il logaritmo in base 10 del valore nu_syn.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_fromfile=pd.read_csv('/home/nicola_polito/get-mcf-data/dati/ex3_data/4LAC_DR2_sel.csv')
print(df_fromfile.head())
print(df_fromfile.columns)

#Grafico dell'indice spettrale(PL_Index) in funzione del flusso(Flux1000)
plt.scatter(df_fromfile['Flux1000'], df_fromfile['PL_Index'], color= 'royalblue', s= 20)
plt.ylabel('PL_Index', fontsize=10)
plt.xlabel('Flux_1000', fontsize=10)
plt.title('Spectral Index in function of Flux')
plt.show()

#Grafico dell'indice spettrale(PL_Index) in funzione del flusso(Flux1000) con asse x logaritmico
plt.scatter(df_fromfile['Flux1000'], df_fromfile['PL_Index'], color= 'limegreen', s= 20)
plt.ylabel('PL_Index', fontsize=10)
plt.xlabel('log(Flux_1000)', fontsize=10)
plt.xscale('log')
plt.title('Spectral Index in function of log(Flux)')
plt.show()

#Indice spettrale(PL_Index) in funzione di Log(nu_syn)

#Grafico1
plt.scatter(df_fromfile['nu_syn'], df_fromfile['PL_Index'], color= 'limegreen', s= 20)
plt.ylabel('PL_Index', fontsize=10)
plt.xlabel('Log(nu_syn) [Hz]', fontsize=10)
plt.xscale('log', base=10)
plt.title('Spectral Index in function of Log(nu_syn)')
plt.show()


#Grafico2 (bll e fsrq)
df_fsrq = df_fromfile.loc[(df_fromfile['CLASS'] == 'fsrq')]
df_bll = df_fromfile.loc[(df_fromfile['CLASS'] == 'bll')]
plt.scatter(df_fsrq['nu_syn'], df_fsrq['PL_Index'], color= 'darkslategray', s= 20, label='fsrq', alpha = 0.8)
plt.scatter(df_bll['nu_syn'], df_bll['PL_Index'], color= 'red', s= 20, label='bll', alpha= 0.3)
plt.ylabel('PL_Index', fontsize=10)
plt.xlabel('Log(nu_syn) [Hz]', fontsize=10)
plt.xscale('log', base=10)
plt.title('for fsrq and bll source class')
plt.suptitle('Spectral Index in function of Log(nu_syn)')
plt.legend()
plt.show()

#Grafico 3 (con incertezza sull'indice spettrale)
plt.errorbar(df_fsrq['nu_syn'], df_fsrq['PL_Index'], yerr=df_fsrq['Unc_PL_Index'], fmt='o', color= 'darkslategray', linewidth=1, capsize= 1, label='fsrq', alpha = 0.8)
plt.errorbar(df_bll['nu_syn'], df_bll['PL_Index'], yerr=df_bll['Unc_PL_Index'], fmt='o', color= 'red', linewidth=1, capsize= 1, label='bll', alpha= 0.3)
plt.ylabel('PL_Index', fontsize=10)
plt.xlabel('Log(nu_syn) [Hz]', fontsize=10)
plt.xscale('log', base=10)
plt.title('for fsrq and bll source class')
plt.suptitle('Spectral Index in function of Log(nu_syn)')
plt.legend()
plt.show()

print(df_fsrq['PL_Index'].size)
print(df_bll['PL_Index'].size)
print('\n')


#Istogramma dell'indice spettrale per le sorgenti di tipo fsrq e bll

#trovo il massimo valore per PL_Index 
def trova_extr(arr):
    val=[0,0]
    for i in arr:
        if(i>=val[0]):
            val[0]= i
        else:
            val[1]=i
    return val

maxPL_fsrq = trova_extr(df_fsrq['PL_Index'])[0]
minPL_fsrq = trova_extr(df_fsrq['PL_Index'])[1]
print('max fsrq:',maxPL_fsrq)
print('min fsrq:',minPL_fsrq)
print('\n')
maxPL_bll= trova_extr(df_bll['PL_Index'])[0]
minPL_bll= trova_extr(df_bll['PL_Index'])[1]
print('max bll:',maxPL_bll)
print('min bll:',minPL_bll)
print('\n')


n, bis, p = plt.hist(df_fsrq['PL_Index'], bins=50, range=(1.5, 3.5), color='darkslategray', alpha=0.8, label='fsrq source')
n, bis, p = plt.hist(df_bll['PL_Index'], bins=50, range=(1.5, 3.5), color='red', alpha=0.4, label='bll source')
plt.suptitle('PL_Index Instogram')
plt.title('for fsrq and bll source class')
plt.xlabel('PL_Index', fontsize=10)
plt.ylabel('Numbers of sources', fontsize=10)
plt.legend(fontsize=10)
plt.show()

#Istogramma di Log(nu_syn) per le sorgenti di tipo fsrq e bll

maxPL_fsrq = trova_extr(np.log10(df_fsrq['nu_syn']))[0]
minPL_fsrq = trova_extr(np.log10(df_fsrq['nu_syn']))[1]
print('max fsrq:',maxPL_fsrq)
print('min fsrq:',minPL_fsrq)
print('\n')
maxPL_bll= trova_extr(np.log10(df_bll['nu_syn']))[0]
minPL_bll= trova_extr(np.log10(df_bll['nu_syn']))[1]
print('max bll:',maxPL_bll)
print('min bll:',minPL_bll)


n, bis, p = plt.hist(np.log10(df_fsrq['nu_syn']), bins=50, range=(10, 22), color='darkslategray', alpha=0.8, label='fsrq source')
n, bis, p = plt.hist(np.log10(df_bll['nu_syn']), bins=50, range=(10, 22), color='red', alpha=0.4, label='bll source')
plt.suptitle('Log(nu_syn) Instogram')
plt.title('for fsrq and bll source class')
plt.xlabel('Log(nu_syn) [Hz]', fontsize=10)
plt.ylabel('Numbers of sources', fontsize=10)
plt.legend(fontsize=10)
plt.show()