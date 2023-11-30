#Esercitazione 5 esercizio 1
'''
Modificare il file somme.py aggiungendo:
    -una funzione che restituisca la somma e il prodotto dei primi n numeri naturali, con n da passare tramite un argomento;
    -una funzione che restituisca (func) con n da passare tramite un argomento e alpha da passare tramite keyword (kwargs), con valore di default pari a 1.
Modificare lo script python che importa il modulo somme in modo da utilizzare le funzioni appena create.
'''

import sys,os
import somma as sum

a=5
b, c =sum.somma_prodotto(a)
print('funzione somma_prodotto n:', b, c)
print('\n')
d= sum.potenze_di_i(a)
print('funzione potenze di i:', d)
e=sum.potenze_di_i(a, alpha=3)
print('\n')
print('funzione potenze di i:', e)