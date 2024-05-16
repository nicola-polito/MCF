#Esercitazione 1 Esercizio 3

from datetime import datetime, timedelta

def calcola_giorni(year_date):
    #un anno bisestile è di 366 giorni invece di 365; ogni 4 anni si aggiunge un giorno in più (a febbraio)
    #1998 era bisestile? No, l'anno prima bisestile era 1996. 
    datenow=datetime.now()
    sum=0
    etc=2
    for i in range(abs(datenow.year - year_date), 0, -1):
        etc+=1
        if(etc==4):
            sum = sum + 366
            etc=0
        else:
            sum=sum+365
    return sum

def calcola_eta(dt):
    bd= input('Inserisci la data di nascita in fmt g-m-y h:m:s:')
    mydate= datetime.strptime(bd, "%d-%m-%Y %H:%M:%S")
    print('\n')
    print(mydate)
    datenow=datetime.now()
    time_diff= datenow-mydate
    print(datenow, '\n')
    until_days = calcola_giorni(mydate.year)
    print(time_diff.days)
    print(until_days)
    yr= datenow.year -mydate.year
    if (mydate.month > datenow.month) or ( datenow.month == mydate.month and datenow.day < mydate.day): # or correzione prof
        yr = yr - 1
        
    dt.update({'years':yr, 'days':(abs(until_days-time_diff.days)), 'seconds':time_diff.seconds})

eta={'years': 1, 'days':1, 'seconds': 1}
calcola_eta(eta)
print(eta, '\n')

print('My Age:')
for s in eta:
    print('{:<8}{:8d}'.format(s, eta[s]))