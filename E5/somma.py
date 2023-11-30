import sys,os

def somma_primi_n(n):
    somma=0
    for i in range(n+1):
        somma=somma+i
    return somma

def somma_radici_n(n):
    somma1=0
    for i in range(n+1):
        somma1=somma1 + pow(i,0.5)
    return somma1

def somma_prodotto(n):
    sum=0
    prod=1
    for i in range(1, n+1):
        sum=sum+i
        prod=prod*i
    return sum, prod

def potenze_di_i(n, alpha=1):
    sum=0
    for i in range(0,n+1):
        term=pow(1j, alpha)
        sum= sum+term
    return sum
