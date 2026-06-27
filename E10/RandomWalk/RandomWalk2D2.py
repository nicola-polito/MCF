import numpy as np
import matplotlib.pyplot as plt

# MODULO CHE IMPLEMENTA IL RANDOM WALK 2D SECONDO UNA CERTA DISTRIBUZIONE DI PROBABILITA
 

# DISTRIBUZIONI

#distribuzione di probabilità SIMMETRICA (uniforme) ------------
def p_sim(phi):
    N=len(phi)
    return np.random.uniform(low=0, high=2*np.pi, size=N)

#Distribuzione di probabilità ASIMMETRICA ------------
def p_as(phi):
    return np.sin(phi/2)/4

#funzione cumulativa
def cum_p(phi):
    return 1/2*(1-np.cos(phi/2))

#inversa cumulativa
def invcum_p(y):
    return 2*np.arccos(1-2*y)

#Generazione delle Occorrenze della Distribuzione
def xp(xx):
    yc=np.random.random(int(1e4))
    xc=invcum_p(yc)

    #verifico i valori trovati confrontando la distribuzione con l'istogramma delle occorrenze

    fig, ax = plt.subplots()
    ax.plot(xx, 850*p_as(xx), label='distribuzione asimmetrica*850', color='black')
    ax.hist(xc, bins=80, range=(0,2*np.pi), color='darkcyan', alpha=0.8, label='occorrenze')
    ax.set_xlabel(r'$\varphi$', )
    ax.set_ylabel('occorrenze distribuzione')
    ax.legend(frameon=False, labelcolor='white')



#IMPLEMENTAZIONE DEL RANDOM WALK 2D attraverso la distribuzione data


# Processo non direzionato

def rnd_walk2D(start, step, n, distr):
    '''
    rnd_walk2D(start, step, n, nrwn, distr): funzione che simula un random walk 2D secondo una certa ditribuzione

    start  : posizione di partenza
    step   : passo random walk (modulo del vettore)
    n      : numero di passi
    distr  : inversa della cumulativa della distribuzione di probabilità che regola il random walk

    reuturn np.array([deltax, deltay]): array con spostamento rispetto alla posizione di partenza per i due assi
    '''

    deltax=np.empty(0) #array con spostamento lungo asse x
    deltay=np.empty(0) #array con spostamento lungo asse y
    movex, movey=start[0], start[1]

    #calcolo valori distribuiti secondo la distribuzione indicata attraverso il metodo dell'inversa della cumulativa
    yc=np.random.random(n)
    var_phi=distr(yc)

    #implementazione del random-walk
    for c in var_phi:
        x_step= step*np.cos(c)
        y_step= step*np.sin(c)
        movex= movex + x_step
        movey= movey + y_step
        deltax=np.append(deltax, movex)
        deltay=np.append(deltay, movey)

    return np.array([deltax,deltay])

def rnd_ws(start, step, n, nwr, distr):
    '''
    rnd_ws(start, step,n,nrw): funzione che simula il moto di un certo numero di random walkers
    start  : vettore posizione iniziale
    step   : passo random walk
    nwr    : numero di random walkers
    n      : numero di passi
    distr  : inversa della cumulativa dellaa distribuzione di probabilità che regola il random walk

    return rws: array di random walks, in cui ciascun elemento contiene lo spostamento lungo x e y 
    '''
    t=np.full(n,0)
    rws=np.array([np.array([t,t]) for x in range(nwr)])
    for i in range(nwr):
        rw= rnd_walk2D(start ,step, n, distr)
        rws[i,0]=rw[0]
        rws[i,1]=rw[1]
    return rws


#Processo direzionato

def rnd_walk2D2(start, step, finish, distr, control):
    '''
    rnd_walk2D(start, step, n, nrwn, distr): funzione che simula un random walk 2D secondo una certa ditribuzione

    start  : posizione di partenza
    step   : passo random walk (modulo del vettore)
    finish : legge che seleziona il numero di passi
    distr  : inversa della cumulativa della distribuzione di probabilità che regola il random walk
    control: variabile che direziona il fenomeno artificialmente

    reuturn deltar: array con spostamento rispetto alla posizione di partenza per i due assi
    '''

    deltax=np.empty(0)
    deltay=np.empty(0) #array con spostamento lungo i due assi
    movex, movey=start[0], start[1]

    x_ref= np.array([movex, start[0], control[0]])
    y_ref=np.array([movey, start[1], control[1]])
    rif_c={'x':x_ref, 'y': y_ref}
    
    #seleziono la coordinata 
    c='x'
    if(type(finish[0])==str):
        if(finish[0] =='y'): 
            c='y'
    else:
        print('Selezionare una coordinata valida!')
        return 0
    
    c_rif=rif_c[c]

    #implementazione del random-walk
    while(np.abs(c_rif[0])<=np.abs(finish[1]-c_rif[1])):
        # estraggo l'occorrenza xc secondo la distribuzione
        yc=np.random.random()
        xc=distr(yc)
        x_step= step*np.cos(xc) + control[0]
        y_step= step*np.sin(xc) + control[1]
        st=np.array([x_step, y_step])
        rif_c['x'][0]= rif_c['x'][0] + st[0]
        rif_c['y'][0]= rif_c['y'][0] + st[1]
        deltax=np.append(deltax, rif_c['x'][0])
        deltay=np.append(deltay, rif_c['y'][0])

    return deltax, deltay

def rnd_ws2(start, step, finish, nwr, distr, control):
    '''
    rnd_ws(start, step, finish, nrw, disrt, control): funzione che simula il moto di un cetro numero di random walkers

    start  : vettore posizione iniziale
    step   : passo random walk
    finish : legge che seleziona il numero di passi
    nwr    : numero di random walkers
    distr  : inversa della cumulativa della distribuzione di probabilità che regola il random walk
    control: variabile che direziona il fenomeno artificialmente

    return t1,t2 : array di random walks,in cui ciascun elemento contiene lo spostamento lungo x e y (divisi dallo 0)
    '''
    t1=np.empty(0)
    t2=np.empty(0)
    for i in range(nwr): 
        rw= rnd_walk2D(start,step, finish, distr, control)
        t1=np.append(t1, rw[0])
        t1=np.append(t1,0)
        t2=np.append(t2, rw[1])
        t2=np.append(t2, 0)
    return t1,t2
