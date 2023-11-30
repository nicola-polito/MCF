# Esercitazione1 Esercizio 1 
#Somma dei primi 100 numeri naturali

def calcola_somma():
    sum=0
    for i in range(101):
        sum= sum + i
    return sum

c = calcola_somma()
print('somma dei primi 100 numeri naturali: ',c)
