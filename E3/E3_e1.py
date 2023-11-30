"""
Esercizio 1 
Creare uno script python che:
    1.legga il file (4FGL_J2202.7+4216_weekly_9_11_2023.csv) e crei il DataFrame pandas corrispondente;
    2.stampi il nome delle colonne del DataFrame;
    3.produca un grafico del flusso in funzione del Giorno Giuliano (Julian Date)
suggerimento: usare pyplot.plot;
    4.produca un grafico del flusso in funzione del Giorno Giuliano coi punti del grafico demarcati da un simbolo;
suggerimento: usare pyplot.plot con opzione 'o' o equivalente;
    5.produca un grafico del flusso in funzione del Giorno Giuliano con barre di errore e salvi il risultato in un file png e/o pdf;
suggerimento: usare pyplot.errorbar;
    6.produca un grafico simile al precedente con asse y logaritmico e salvi il risultato in un file png e/o pdf;
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df_fromfile=pd.read_csv('/home/nicola_polito/get-mcf-data/dati/ex3_data/4FGL_J2202.7+4216_weekly_9_11_2023.csv')
print(df_fromfile.head())
print(df_fromfile.columns)

#Grafico del flusso in funzione del giorno giuliano(asse non logaritmico)
plt.errorbar(df_fromfile['Julian Date'], df_fromfile['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], yerr=df_fromfile['Photon Flux Error(photons cm-2 s-1)'], fmt= 'o', linewidth=1, capsize=10**(-7), color= 'blue')
plt.title('Phothon Flux in function of Julian Date')
plt.xlabel('Julian Date', fontsize=12)
plt.ylabel('Phothon Flux', fontsize=12)
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
plt.show()

#Grafico del flusso in funzione del giorno giuliano(asse logaritmico)
plt.errorbar(df_fromfile['Julian Date'], df_fromfile['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], yerr=df_fromfile['Photon Flux Error(photons cm-2 s-1)'], fmt= 'o', linewidth=1, capsize=10**(-7), color= 'orange')
plt.title('Phothon Flux in function of Julian Date')
plt.xlabel('Julian Date', fontsize=12)
plt.ylabel('log(Phothon Flux)', fontsize=12)
plt.yscale('log')
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
plt.show()