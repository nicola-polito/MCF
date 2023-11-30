"""
Esercizio 1.
    Creare un DataFrame con le seguenti temperature dell'ultima settimana:
        - minima
        - massima
        - media tra massima e minima
    Mostrare i dati in una tabella
    Calcolare media e deviazione standard delle due serie di dati e mostrarle
"""

import pandas as pd
import numpy as np

# PARTE 1
temp_data = pd.DataFrame(columns = ['Data','Minima(°C)', 'Massima(°C)', 'Media(°C)'])
date= np.array(['Sab 21', 'Dom 22', 'Lun 23', 'Mar 24', 'Mer 25', 'Gio 26', 'Ven 27'])
minimi = np.array([15, 14, 10, 13, 16, 15, 17])
massimi = np.array([22, 21, 21, 23, 20, 22, 22])
medie= np.array(np.empty(0), dtype=int)

for i in range(0, len(minimi)):
    term = int((minimi[i]+massimi[i])/2)
    medie = np.append(medie, term)

temp_data['Data'] = date
temp_data['Minima(°C)']= minimi
temp_data['Massima(°C)']= massimi
temp_data['Media(°C)']= medie

print(temp_data)
print('\n')

#PARTE 2

media_min = np.mean(temp_data['Minima(°C)'])
media_max = np.mean(temp_data['Massima(°C)'])

def sd(arr, m):
    sum2=0
    for i in range(0, len(arr)):
        sum2 = sum2 + np.power(arr[i]- m, 2)
    var= sum2/(len(arr)-1)
    d = var**(0.5)
    return d

sd_min = sd(temp_data['Minima(°C)'], media_min)
sd_max = sd(temp_data['Massima(°C)'], media_max)

print('Massime: (', int(round(media_max,0)),'+-', int(round(sd_max,0)) ,') °C')
print('\n')
print('Minime: (', int(round(media_min,0)) ,'+-', int(round(sd_min,0)) ,') °C')