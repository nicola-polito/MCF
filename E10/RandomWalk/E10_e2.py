import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import argparse
import RandomWalk2D2 as rw2

# SCRIPT CHE SIMULA UN RANDOM WALK 2D



# PROCESSO NON DIREZIONATO


# Setting per processo non direzionato ------------
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


# Grafico delle posizioni Random Walk ------------
def rw_graph2(pstart, step, N, rw_sim):
    '''
    rw_graph(pstart, step, N, rw_sim): grafica un random walk 2D non direzionato

    parametri iniziali random walk
        pstart: posizione iniziale, 
        step  : passo
        N     : numero di passi
    
    rw_sim: array contenente le cooridinate del random walker ad ogni passo
    '''
    xx=np.arange(0, N*step, step )
    fig, ax=plt.subplots(3,1, figsize=(6,5), layout='constrained')
    #fig.subplots_adjust(hspace=0)
    fig.suptitle('Random Walk 2D, Distribuzione: '+r'$ p(\varphi)= \frac{1}{4} \sin \left( \frac{\varphi}{2} \right)$', color='grey', fontsize=14)

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


# Grafico delle posizioni di n random walk per N passi ------------
def rw_graph2(pstart, N, rw_sim, n_rws):
    '''
    rw_graph(pstart, N, rw_sim, n_rws): grafica un random walk 2D non direzionato
    
    parametri iniziali random walk
        pstart: posizione iniziale, 
        N     : numero di passi
    
    rw_sim: array contenente le cooridnate del random walker ad ogni passo
    d_text: distribuzione
    n_rws : numero di random walkers
    '''

    fig, ax=plt.subplots(figsize=(6,5), layout='constrained')

    plt.suptitle('{:5d} Random Walk per {:5d} passi, Distribuzione:'.format(n_rws ,N, d_text), color = 'grey')
    count=1
    mark=''
    ax.axhline(0, color='grey', linewidth=1)
    ax.axvline(0, color='grey', linewidth=1)
    for i in rw_sim:
        if(count==5):
            mark='end position'
        ax.plot(i[0], i[1], '--', label='rw{:d}'.format(count))
        ax.plot(i[0][-1], i[1][-1],'o', markersize=7,label=mark, color='black')
        count +=1
    ax.plot(pstart[0], pstart[1], 'o', markersize=7, label='start position', color='darkblue')
    ax.set_xlabel(r'$\Delta x$')
    ax.set_ylabel(r'$\Delta y$')
    ax.legend()



# PROCESSO DIREZIONATO


# Setting per processo direzionato ------------
def sel_n(s, c, x):
    '''
    sel_n(s, n, c): funzione che seleziona il numero di passi di un random walk in modo che la coordinata c < s*n
    s: passo
    x: limite per la coordinata c --> m(c)<s*x
    c: coordinata di riferimento

    restituisce un array contenente: la coordinata c di riferimento, il limite per la coordinata c
    '''
    return [c, s*x]

def lim_set():
    p0, n, passo=rw_set()
    #input variabile di direzionalità
    ctrl=False
    while(ctrl==False):
        try:
            sf=float(input('\n parametro di direzionalità: '))
            ctrl=True
        except: print('\n valore immesso non valido! deve essere un numero reale. Riprova: \n')
    
    control1=np.array([sf*passo,0])  

    #input coordinata di riferimento
    c=input(str('\n coordinata di riferimento (di default è x):'))
    print('\n coordinata selezionata: ', c)

    if(c=='y'): control1=np.array([0, sf*passo])

    #input limite per la coordinata c
    ctrl=False
    while(ctrl==False):
        try:
            lim=float(input('\n limite per la coordinata {:s}: '.format(c)))
            ctrl=True
        except: print('\n valore immesso non valido! deve essere un numero reale. Riprova: \n')
    
    return sel_n(passo, c, lim), control1


def rw_graph3(pstart, n_rws, dp, clim, rw_sim, d_text):
    '''
    rw_graph(pstart, N, rw_sim, n_rws): grafica un random walk 2D direzionato

    pstart: posizione iniziale
    n_rws : numero di random walkers
    clim  : posizione limite che arresta il processo  
    dp    : parametro di direzionalità
    rw_sim: array contenente le cooridnate del random walker ad ogni passo
    d_text: distribuzione
    '''

    #seleziono gli indici 0 per printare in base agli indici
    d1x=np.where(rw_sim[0]==0)[0]
    s1x=np.zeros(1)
    s1x=np.append(0,d1x[:-1])

    fig, ax=plt.subplots(figsize=(6,5), layout='constrained')

    plt.suptitle('5 Random Walker per $s_f = {:d}$ con processo arrestato quando $ \Delta x \geq s{:d}$'.format(dp, clim), color = 'grey')
    count=1
    mark=''
    ax.axhline(pstart[1], color='grey', linewidth=1)
    ax.axvline(pstart[0], color='grey', linewidth=1)
    ax.axvline(clim, color='gold', linestyle='--')
    for j,k in zip(s1x, d1x):
        if(count==n_rws):
            mark='end position'
    ax.plot(rw_sim[0][j:k], rw_sim[1][j:k], '--', label='rw{:d}'.format(count))
    ax.plot(rw_sim[0][j:k][-1], rw_sim[1][j:k][-1],'o', markersize=7,label=mark, color='black')
    count +=1
    ax.text(-85,30, 'Distribuzione: {:d}'.format(d_text))
    ax.plot(pstart[0], pstart[1], 'o', markersize=7, label='start position', color='darkblue')
    ax.set_xlabel(r'$\Delta x$')
    ax.set_ylabel(r'$\Delta y$')
    ax.legend()   


# Gestione script da riga di comando
def parse_arguments():
    parser=argparse.ArgumentParser(description='simulazione random walk 2d', 
                                   usage= 'python3 e10_e1.py  --opzione')
    parser.add_argument('-p2', '--p_as', action='store_true', help='distribuzione asimmetica')
    parser.add_argument('-rw_p1', '--p1_walk', action='store_true', help='simula 1 random walk 2D simmetrico non direzionato')
    parser.add_argument('-rw_p2','--p2_walk', action='store_true', help='simula 1 random walks 2D asimmetrico non direzionato')
    parser.add_argument('-rws_p1','--p1walkers', action='store_true', help='simula n random walks 2D simmetrici non direzionati')
    parser.add_argument('-rws_p2','--p2walkers', action='store_true', help='simula n random walks 2D asimmetrici non direzionati')
    parser.add_argument('-drws', '--p2DirWalkers', action='store_true', help='simula n random wlakers asimmetrici direzionati')

    return parser.parse_args()


# MAIN
def random_walk_sim():
    args=parse_arguments()
    xx=np.linspace(0, 2*np.pi, 1000)
    yy=np.arange(0,1,0.001)
    p_sim=rw2.p_sim(xx)
    p_as=rw2.p_as(xx)
    inv_as=rw2.invcum_p(yy)

    if args.p_as == True:
        rw2.xp(xx)
    
    if args.p1_walk == True:
        p0, passo, n = rw_set()
        sim_s1=rw2.rnd_walk2D(p0, passo, n, rw2.p_sim)
        rw_graph2(p0, passo, n, sim_s1)

    if args.p2_walk == True:
        print('')

    if args.p1walkers == True:
        print('')

    if args.p2walkers == True:
        print('')
    
    if args.p2DirWalkers == True:
        print('')
    
    plt.show(block = True)



if __name__=='__main__':

    random_walk_sim()
    




