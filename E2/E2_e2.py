3#Esercitazione 1 Esercizio 2
#Somma dei primi N numeri naturali

def calcola_somma_n():
    sum=0
    num = input('Inserire un numero:')
    controllo= num.find('.')
    print(type(controllo))
    while (controllo > 0):
        print('Valore non valido ! ')
        num=input('Riprova!:')
        controllo= num.find('.')
        
    N = int(num)
    if (N==0):
        sum=0
    elif(N==1):
        sum=1
    else:
        for i in range(N+1):
            sum = sum + i 
    print('La somma è: ', sum)    

calcola_somma_n()
        