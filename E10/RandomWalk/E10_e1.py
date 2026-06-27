import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import argparse
import RandomWalk2D as rw

# SCRIPT CHE SIMULA UN RANDOM WALK SIMMETRICO 2D

# Set random walk
def rw_set():
    '''
    rw_set(pstart, N, step): funzione che definisce i parametri di base di un random walk 2D

    pstart: posizione iniziale
    N     : numero di passi
    step  : passo del random walk
    '''

    x=0
    y=0
    N=0
    step=0
    pstart=np.zeros(2)

    # input posizione iniziale
    ctrl=False
    while(ctrl==False):
        try:
            x= float(input(' posizione iniziale x: '))
            y= float(input('\n posizione iniziale y: '))
            ctrl=True
        except:
            print('\n valore immesso non valido! deve essere una coppia di coordinate reali. Riprova: \n')
    pstart=np.array([x,y])

    #input numero di passi
    ctrl=False
    while(ctrl==False):
        try:
            N= int(input('\n numero di passi: '))
            if (N>0):
                ctrl=True
            else: print('\n valore immesso non valido! deve essere un numero naturale. Riprova: \n')
        except:
            print(' \n valore immesso non valido! deve essere un numero naturale. Riprova: \n')
    
    #input passo
    ctrl=False
    while(ctrl == False):
        try:
            step= float(input('\n passo: '))
            if(step >0):
                ctrl=True
            else: print('\n valore immesso non valido! deve essere un numero reale positivo. Riprova: \n')
        except:
            print('\n valore immesso non valido! deve essere un numero reale positivo. Riprova: \n')
        
        
    return pstart, step, N


# Grafico random walk
def rw_graph(pstart, step, N, rw_sim):
    '''
    rw_graph(pstart, step, N, rw_sim): grafica un random walk 2D

    parametri iniziali random walk
        pstart: posizione iniziale, 
        step  : passo
        N     : numero di passi
    
    rw_sim: array contenente le cooridinate del random walker ad ogni passo
    '''
    xx=np.arange(0, N*step, step )
    fig, ax=plt.subplots(3,1, figsize=(6,5), layout='constrained')
    #fig.subplots_adjust(hspace=0)
    fig.suptitle('Random Walk 2D', color='grey', fontsize=14)

    ax[0].plot(xx/step, rw_sim[0])
    ax[0].set_xlabel('passi')
    ax[0].set_ylabel(r'$\Delta x$')
    #ax[0].set_ylim(-25,25)
    ax[0].set_title(r'spostamento lungo $x$', loc='left', color='grey', fontsize=12)

    ax[1].plot(xx/step, rw_sim[1])
    ax[1].set_xlabel('passi')
    ax[1].set_ylabel(r'$\Delta y$')
    #ax[1].set_ylim(-25,25)
    ax[1].set_title(r'spostamento lungo $y$',  loc='left', color='grey', fontsize=12)

    ax[2].plot(rw_sim[0], rw_sim[1], linestyle='--')
    ax[2].plot(pstart[0], pstart[1], 'o', markersize=6, label='start position')
    ax[2].plot(rw_sim[0][-1], rw_sim[1][-1], 'o', markersize=6, label='end position')
    ax[2].set_xlabel(r'$\Delta x$')
    ax[2].set_ylabel(r'$\Delta y$')
    ax[2].legend()
    #ax[2].set_ylim(-25,25)


#Grafico random walkers
def rws_graph(pstart, N, rw_sim, n_rws):
    '''
    rw_graph(pstart, N, rw_sim, n_rws): grafica un random walk 2D
    
    parametri iniziali random walk
        pstart: posizione iniziale, 
        N     : numero di passi, 
    
    rw_sim: array contenente le cooridnate del random walker ad ogni passo
    n_rws : numero di random walkers
    '''

    fig2, ax=plt.subplots(figsize=(6,5), layout='constrained')

    plt.suptitle('{:5d} Random Walks per {:5d} passi '.format(n_rws, N), color = 'grey')
    count=1
    mark=''
    ax.axhline(pstart[1], color='grey', linewidth=1)
    ax.axvline(pstart[0], color='grey', linewidth=1)
    for i in rw_sim:
        if(count==n_rws):
            mark='end position'
        ax.plot(i[0], i[1], '--', label='rw{:d}'.format(count))
        ax.plot(i[0][-1], i[1][-1],'o', markersize=7,label=mark, color='black')
        count +=1
    ax.plot(pstart[0], pstart[1], 'o', markersize=7, label='start position', color='darkblue')
    ax.set_xlabel(r'$\Delta x$')
    ax.set_ylabel(r'$\Delta y$')
    ax.legend()


#Grafico random walkers distanza dal punto di partenza
def rws_dgraph(pstart, step, N, rw_sim, n_rws, d_rws):
    '''
    rw_dgraph(pstart, step, N, rw_sim, n_rws, d_rws): grafica un random walk 2D

    parametri iniziali random walk
        pstart: posizione iniziale,  
        step  : passo
        N     : numero di passi,
    
    rw_sim: array contenente le cooridnate del random walker ad ogni passo
    n_rws : numero di random walkers
    d_rws = rw.euclid_d: array contenente il quadrato della distanza dalla posizione iniziale
                         raggiunta da nwr random walkwers in funzione del numero di passi
    '''

    xx1=np.arange(0, N*step, step)
    xxl=np.array([xx1 for x in range(n_rws)])

    fig4, ax=plt.subplots(2,1, figsize=(7,7), layout='constrained')
    #fig.subplots_adjust(hspace=0)

    plt.suptitle('Quadrato della distanza dalla posizione di partenza in termini di numero di passi', color='grey')
    count=1
    mark=''
    ax[0].axhline(pstart[1], color='grey', linewidth=1)
    ax[0].axvline(pstart[0], color='grey', linewidth=1)
    for i in rw_sim:
        if(count==n_rws):
            mark='end position'
        ax[0].plot(i[0], i[1], '--', label='rw{:d}'.format(count))
        ax[0].plot(i[0][-1], i[1][-1],'o', markersize=7,label=mark, color='black')
        count +=1
    ax[0].plot(pstart[0], pstart[1], 'o', markersize=7, label='start position', color='darkblue')
    ax[0].set_xlabel(r'$\Delta x$')
    ax[0].set_ylabel(r'$\Delta y$')
    ax[0].legend()

    count=1
    for l,z in zip(xxl,d_rws):
        ax[1].plot(l, z, '-', label='rw{:d}'.format(count))
        ax[1].set_ylabel(r'$d^2$ passi')
        ax[1].set_xlabel('passi')
        count+=1
    ax[1].legend()


#Gestione script da riga di comando
def parse_arguments():
    parser=argparse.ArgumentParser(description='simulazione random walk 2d simmetrico', 
                                   usage= 'python3 e10_e1.py  --opzione')
    parser.add_argument('-rw', '--random_walk', action='store_true', help='simula 1 random walk 2D simmetrico')
    parser.add_argument('-rws','--walkers', action='store_true', help='simula n random walks 2D simmetrici')
    parser.add_argument('-drws','--distance_walkers', action='store_true', help='simula n random walks 2D simmetrici e grafica la distanza raggiunta dalla posizione di partenza')

    return parser.parse_args()

#MAIN
def random_walk_sim():
    args=parse_arguments()
    p0=np.zeros(2); passo=0; n=0; nn=0

    if args.random_walk == True:
        p0, passo, n=rw_set()
        rw1=rw.walk_2d(p0, passo, n)
        rw_graph(p0, passo, n, rw1)

    if args.walkers == True:
        p0, passo, n=rw_set()
        nn=int(input('\n numero di random walkers: '))
        while(nn<0):
            print('\n valore immesso non valido! deve essere un numero naturale. Riprova: \n')
            nn=int(input('\n numero di random walkers: '))
        rws1=rw.rnd_ws(p0 ,passo, n, nn)
        rws_graph(p0, n, rws1, nn)

    if args.distance_walkers == True:
        p0, passo, n=rw_set()
        nn= int(input('\n numero di random walkers: '))
        while(nn<0):
            print('\n valore immesso non valido! deve essere un numero naturale. Riprova: \n')
            nn= int(input('\n numero di random walkers: '))
        rws2=rw.rnd_ws(p0 ,passo, n, nn)
        d_rws2=rw.euclid_d(p0, n, rws2, nn)
        rws_dgraph(p0, passo, n, rws2, nn, d_rws2)

    plt.show(block=True)


if __name__=='__main__':
    random_walk_sim()

