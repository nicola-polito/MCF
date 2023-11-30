#Esercitazione 1 esercizio 4
'''
Creare uno script python che:
- Crei una lista con i nomi dei giorni della settimana;
- Crei una lista col nome dei giorni della settimana per tutto il mese di ottobre 2023;
- Crei un dizionario che metta in relazione il giorno del mese di ottobre 2023 con il giorno della settimana.
'''

week = ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi', 'Sabato', 'Domenica']
october_week=[]

t=0
s=0
while(t<31):
    el= week[s-1]
    october_week.append(el) 
    if(s==len(week)-1):
        s=0
    else:
        s=s+1
    t=t+1
print(october_week)
print(len(october_week))
print('\n')

g=range(1, 32)
october={}
for s, r in zip(g, october_week):
    october[s]=r

for l in october:
    print('{:d}{: >13}'.format(l, october[l]))
print('\n')
