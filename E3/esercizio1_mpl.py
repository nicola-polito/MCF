"""
Esercizio 1 matplotlib
    - Recuperare le temperature massime e minime per le località: Perugia, Palermo, Padova;
    - Creare un  data frame per ogni città con le temperature minima, massima e media per l'ultima settimana;
    - Mostrare i dati in una tabella per località;
    - Produrre un grafico di temperatura minima, massima e media in funzione del giorno per ogni città:
        . le tre temperature devono comparire nello stesso grafico ed essere accompagnate da una legenda;
        . assegnare un errore di un grado alle temperature minima e massima.
    - Produrre un grafico con le tre località insieme per temperature minime, massime e medie in funzione del giorno:
        .un grafico per tipo di temperatura con le città distinte da una legenda;
        .assegnare errore di un grado alle temperature massima e minima.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PARTE 1: creare dataframe per pgni località
#funzioni
def costruisci_tab(g, m, M, med):
    data = pd.DataFrame(columns = ['Data','Minima(°C)', 'Massima(°C)', 'Media(°C)'])
    data['Data'] = g
    data['Minima(°C)']= m
    data['Massima(°C)']= M
    data['Media(°C)']= med
    return data

def calcola_medie(minimi, massimi):
    medie= np.array(np.empty(0), dtype=int)
    for i in range(0, len(minimi)):
        term = int((minimi[i]+massimi[i])/2)
        medie = np.append(medie, term)
    return medie

#città
cityes= np.array(['Perugia', 'Palermo', 'Padova'])
date= np.array(['Sab 21', 'Dom 22', 'Lun 23', 'Mar 24', 'Mer 25', 'Gio 26', 'Ven 27'])

#Perugia (dati 3Bmeteo)
minimi_u = np.array([15, 14, 10, 13, 16, 15, 17])
massimi_u = np.array([22, 21, 21, 23, 20, 22, 22])
medie_u= calcola_medie(minimi_u, massimi_u)
u_data = costruisci_tab(date, minimi_u, massimi_u,medie_u)

#Palermo
minimi_s= np.array([21, 18, 18, 17, 22, 19, 21])
massimi_s = np.array([28, 27, 26, 29, 26, 26, 28])
medie_s= calcola_medie(minimi_s, massimi_s)
s_data = costruisci_tab(date, minimi_s, massimi_s,medie_s)

#Padova
minimi_v = np.array([15, 13, 13, 14, 13, 13, 15])
massimi_v = np.array([23, 22, 22, 18, 19, 18, 21])
medie_v= calcola_medie(minimi_v, massimi_v)
v_data = costruisci_tab(date, minimi_v, massimi_v,medie_v)

data_frame= np.array([u_data, s_data, v_data])
print('Perugia \n')
print(u_data)
print('\n')
print('Palermo \n')
print(s_data)
print('\n')
print('Padova \n')
print(v_data)

#PARTE 2: 1° grafico

"""
#Perugia
fig, ax = plt.subplots(1, 3, figsize=(15, 4)) 
plt.suptitle('Temperature nell ultima settimana Perugia')
ax[0].plot(u_data['Data'], u_data['Minima(°C)'], 'o-', color = 'limegreen')
ax[1].plot(u_data['Data'], u_data['Massima(°C)'], 'o-', color = 'blue')
ax[2].plot(u_data['Data'], u_data['Media(°C)'], 'o-', color = 'red')

ax[0].set_title('Minime', fontsize=13, color= 'limegreen')
ax[1].set_title('Massime', fontsize=13, color= 'blue')
ax[2].set_title('Medie', fontsize=13, color= 'red')

for i in range(0, 3):
    ax[i].set_xlabel('giorno')
    ax[i].set_ylabel('°C')
    ax[i].tick_params(axis='x', labelsize=6)
    ax[i].tick_params(axis='y', labelsize=12)
    ax[i].set_xlim(-1, 7)
    ax[i].set_ylim(5, 32)
    ax[i].grid(True)
plt.show()

#Palermo
fig, ax = plt.subplots(1, 3, figsize=(15, 4)) 
plt.suptitle('Temperature nell ultima settimana Palermo')
ax[0].plot(s_data['Data'], s_data['Minima(°C)'], 'o-', color = 'limegreen')
ax[1].plot(s_data['Data'], s_data['Massima(°C)'], 'o-', color = 'blue')
ax[2].plot(s_data['Data'], s_data['Media(°C)'], 'o-', color = 'red')

ax[0].set_title('Minime', fontsize=13, color= 'limegreen')
ax[1].set_title('Massime', fontsize=13, color= 'blue')
ax[2].set_title('Medie', fontsize=13, color= 'red')

for i in range(0, 3):
    ax[i].set_xlabel('giorno')
    ax[i].set_ylabel('°C')
    ax[i].tick_params(axis='x', labelsize=6)
    ax[i].tick_params(axis='y', labelsize=12)
    ax[i].set_xlim(-1, 7)
    ax[i].set_ylim(5, 32)
    ax[i].grid(True)
plt.show()

#Padova
fig, ax = plt.subplots(1, 3, figsize=(15, 4)) 
plt.suptitle('Temperature nell ultima settimana Padova')
ax[0].plot(v_data['Data'], v_data['Minima(°C)'], 'o-', color = 'limegreen')
ax[1].plot(v_data['Data'], v_data['Massima(°C)'], 'o-', color = 'blue')
ax[2].plot(v_data['Data'], v_data['Media(°C)'], 'o-', color = 'red')

ax[0].set_title('Minime', fontsize=13, color= 'limegreen')
ax[1].set_title('Massime', fontsize=13, color= 'blue')
ax[2].set_title('Medie', fontsize=13, color= 'red')

for i in range(0, 3):
    ax[i].set_xlabel('giorno')
    ax[i].set_ylabel('°C')
    ax[i].tick_params(axis='x', labelsize=6)
    ax[i].tick_params(axis='y', labelsize=12)
    ax[i].set_xlim(-1, 7)
    ax[i].set_ylim(5, 32)
    ax[i].grid(True)
plt.show()
"""

#versione con errorbar
#Perugia
fig, ax = plt.subplots(1, 3, figsize=(15, 4)) 
plt.suptitle('Temperature ultima settimana Perugia')
ax[0].errorbar(u_data['Data'], u_data['Minima(°C)'], yerr=1 , fmt='o-', color = 'limegreen')
ax[1].errorbar(u_data['Data'], u_data['Massima(°C)'], yerr=1, fmt='o-', color = 'blue')
ax[2].errorbar(u_data['Data'], u_data['Media(°C)'], yerr=1, fmt='o-', color = 'red')

ax[0].set_title('Minime', fontsize=13, color= 'limegreen')
ax[1].set_title('Massime', fontsize=13, color= 'blue')
ax[2].set_title('Medie', fontsize=13, color= 'red')

for i in range(0, 3):
    ax[i].set_xlabel('giorno')
    ax[i].set_ylabel('°C')
    ax[i].tick_params(axis='x', labelsize=6)
    ax[i].tick_params(axis='y', labelsize=12)
    ax[i].set_xlim(-1, 7)
    ax[i].set_ylim(5, 32)
    ax[i].grid(True)
plt.show()

#Palermo
fig, ax = plt.subplots(1, 3, figsize=(15, 4)) 
plt.suptitle('Temperature ultima settimana Palermo')
ax[0].errorbar(s_data['Data'], s_data['Minima(°C)'], yerr=1, fmt='o-', color = 'limegreen')
ax[1].errorbar(s_data['Data'], s_data['Massima(°C)'], yerr=1, fmt='o-', color = 'blue')
ax[2].errorbar(s_data['Data'], s_data['Media(°C)'], yerr=1, fmt='o-', color = 'red')

ax[0].set_title('Minime', fontsize=13, color= 'limegreen')
ax[1].set_title('Massime', fontsize=13, color= 'blue')
ax[2].set_title('Medie', fontsize=13, color= 'red')

for i in range(0, 3):
    ax[i].set_xlabel('giorno')
    ax[i].set_ylabel('°C')
    ax[i].tick_params(axis='x', labelsize=6)
    ax[i].tick_params(axis='y', labelsize=12)
    ax[i].set_xlim(-1, 7)
    ax[i].set_ylim(5, 32)
    ax[i].grid(True)
plt.show()

#Padova
fig, ax = plt.subplots(1, 3, figsize=(15, 4)) 
plt.suptitle('Temperature ultima settimana Padova')
ax[0].errorbar(v_data['Data'], v_data['Minima(°C)'], yerr=1, fmt='o-', color = 'limegreen')
ax[1].errorbar(v_data['Data'], v_data['Massima(°C)'], yerr=1, fmt='o-', color = 'blue')
ax[2].errorbar(v_data['Data'], v_data['Media(°C)'], yerr=1, fmt='o-', color = 'red')

ax[0].set_title('Minime', fontsize=13, color= 'limegreen')
ax[1].set_title('Massime', fontsize=13, color= 'blue')
ax[2].set_title('Medie', fontsize=13, color= 'red')

for i in range(0, 3):
    ax[i].set_xlabel('giorno')
    ax[i].set_ylabel('°C')
    ax[i].tick_params(axis='x', labelsize=6)
    ax[i].tick_params(axis='y', labelsize=12)
    ax[i].set_xlim(-1, 7)
    ax[i].set_ylim(5, 32)
    ax[i].grid(True)
plt.show()


#PARTE 3: 2° grafico

#Minime
fig, ax = plt.subplots( figsize=(10, 5) )
plt.title('Minime ultima settimana')
plt.errorbar(u_data['Data'], u_data['Minima(°C)'], yerr=1, fmt='o-', color = 'limegreen', label='Perugia')
plt.errorbar(s_data['Data'], s_data['Minima(°C)'], yerr=1, fmt='o-', color = 'blue', label = 'Palermo')
plt.errorbar(v_data['Data'], v_data['Minima(°C)'], yerr=1, fmt='o-', color = 'red', label= 'Padova')
plt.xlabel('giorno')
plt.ylabel('°C')
plt.xticks(fontsize= 10)
plt.yticks(fontsize=10)
plt.legend(fontsize= 12)
plt.show()

#Massime
fig, ax = plt.subplots( figsize=(10, 5) )
plt.title('Massime ultima settimana')
plt.errorbar(u_data['Data'], u_data['Massima(°C)'], yerr=1, fmt='o-', color = 'limegreen', label='Perugia')
plt.errorbar(s_data['Data'], s_data['Massima(°C)'], yerr=1, fmt='o-', color = 'blue', label = 'Palermo')
plt.errorbar(v_data['Data'], v_data['Massima(°C)'], yerr=1, fmt='o-', color = 'red', label= 'Padova')
plt.xlabel('giorno')
plt.ylabel('°C')
plt.xticks(fontsize= 10)
plt.yticks(fontsize=10)
plt.legend(fontsize= 12)
plt.show()

#Medie
fig, ax = plt.subplots( figsize=(10, 5) )
plt.title('Medie ultima settimana')
plt.errorbar(u_data['Data'], u_data['Media(°C)'], yerr=1, fmt='o-', color = 'limegreen', label='Perugia')
plt.errorbar(s_data['Data'], s_data['Media(°C)'], yerr=1, fmt='o-', color = 'blue', label = 'Palermo')
plt.errorbar(v_data['Data'], v_data['Media(°C)'], yerr=1, fmt='o-', color = 'red', label= 'Padova')
plt.xlabel('giorno')
plt.ylabel('°C')
plt.xticks(fontsize= 10)
plt.yticks(fontsize=10)
plt.legend(fontsize= 12)
plt.show()






