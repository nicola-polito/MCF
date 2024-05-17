#Esercitazione 5 esercizio 1
'''
ESERCIZIO 0
Creare il file python somme.py in cui vanno definite due funzioni:
    - una funzione che restituisca la somma dei primi n numeri naturali, con n da passare tramite un argomento;
    - una funzione che restituisca la somma delle radici dei primi n numeri naturali, con n da passare tramite un argomento.
Creare uno script python che importi il modulo somme appena creato e ne utilizzi le funzioni.
Esaminare la cartella di lavoro.
''' 

import sys,os
import somma as sum

num= input('Immettere un numero:')
print('Il numero immesso è ',num, '\n')
nn=int(num)
b=sum.somma_primi_n(nn)
print('funzione somma:', b, '\n')
c=sum.somma_radici_n(nn)
print('funzione somma radici:', c, '\n')
d,e=sum.somma_prodotto(nn)
print('funzione somma-prodotto: ', d, e,'\n')
f1=sum.potenze_di_i(nn)
f2=sum.potenze_di_i(nn, alpha = 3)
print('funzione potenze di i: {:} -- {:}'.format(f1,f2))

'''
E' stata creata automaticamente nella stessa cartella in cui sono presenti gli script relativi, la cartella "_pycache_" .
La cartella “__pycache__” è una directory generata automaticamente da Python quando esegui uno script Python o importi un modulo.
La sua funzione principale è archiviare file bytecode (.pyc) che contengono codice Python compilato.
'''
