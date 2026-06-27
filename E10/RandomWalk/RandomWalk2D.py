import numpy as np

# MODULO CHE IMPLEMENTA IL RANDOM WALK 2D


# Random Walk ---------------
def walk_2d(start, step, N):
    """
    funzione walk_2d(step, N) per generare una sequenza di random walk 2D
    
    start: posizione di partenza
    step : array contenente il modulo del vettore passo del random walk
    N    : numero di passi
    
    reuturn deltar: array con spostamento rispetto all'origine per i due assi
    """
 
    deltax=np.empty(0) #array con spostamento lungo asse x
    deltay=np.empty(0) #array con spostamento lungo asse y
    movex, movey=start[0], start[1]
    var_phi=np.random.uniform(low=0, high=2*np.pi, size=N)

    #implementazione random_walk
    for c in var_phi:
        x_step= step*np.cos(c)
        y_step= step*np.sin(c)
        movex= movex + x_step
        movey= movey + y_step
        deltax=np.append(deltax, movex)
        deltay=np.append(deltay, movey)

    return np.array([deltax,deltay])


#Random Walkers ---------------
def rnd_ws(start, step, N, nwr):
    '''
    rnd_ws(start, step,n,nrw): funzione che simula il moto di un certo numero di random walkers
    start : vettore posizione iniziale
    step  : passo random walk
    nwr   : numero di random walkers
    N     : numero di passi

    return rws: array di random walks,in cui ciascun elemento contiene lo spostamento lungo x e y 
    '''
    t=np.full(N,0)
    rws=np.array([np.array([t,t]) for x in range(nwr)])
    for i in range(nwr):
        rw= walk_2d(start,step, N)
        rws[i,0]=rw[0]
        rws[i,1]=rw[1]
    return rws


#Distanza dal punto di partenza ---------------
def euclid_d(p0, N, rwfunc, nrw):
    '''
    euclid(p0, rwfunc, N, nrw): funzione che calcola il quadrato della distanza 
                                raggiunta da nwr random walkwers in funzione del numero di passi
    p0    : posizione di partenza
    N     : numero di passi per ciascun random walker
    rwfunc: simulazione random walk attraverso rnw_ws
    nwr   : numero di random walkers

    '''
    t=np.full(N,0)
    de=np.array([t for x in range(nrw)])
    for i,j in zip(rwfunc, range(nrw)):
        sum=0
        d=(i[0]-p0[0])**2 + (i[1]-p0[1])**2
        sum=sum+d
        de[j]=sum
    return de
