#Esercitazione 1 Esercizio 3

from datetime import datetime, timedelta

def calcola_giorni(year_date):
    #un anno bisestile è di 366 giorni invece di 365; ogni 4 anni si aggiunge un giorno in più (a febbraio)
    #1998 era bisestile? No, l'anno prima bisestile era 1996. 
    datenow=datetime.now()
    sum=0
    etc=2
    for i in range(abs(datenow.year - year_date), 0, -1):
        etc=etc+1
        if(etc==4):
            sum = sum + 366
            etc=0
        else:
            sum=sum+365
    return sum

def calcola_eta(dt):
    bd=''
    print('Inserisci la data di nascita in fmt g-m-y h:m:s:')
    birthday=input(bd)
    mydate= datetime.strptime(birthday, "%d-%m-%Y %H:%M:%S")
    print('\n')
    print(mydate)
    datenow=datetime.now()
    time_diff= datenow-mydate
    print(datenow, '\n')
    until_days = calcola_giorni(mydate.year)
    last_days= calcola_giorni(2024)
    print(last_days)
    print(time_diff.days)
    print(until_days)
    yr= datenow.year -mydate.year
    if (mydate.month > datenow.month):
        yr = yr - 1
        
    dt.update({'years':yr, 'days':(last_days-(until_days-time_diff.days)) , 'seconds':time_diff.seconds})

eta={'years': 1, 'days':1, 'seconds': 1}
calcola_eta(eta)
print(eta, '\n')

print('My Age:')
for s in eta:
    print('{:<8}{:8d}'.format(s, eta[s]))