import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
from scipy import integrate
import argparse

# Setting del Potenziale-------------------------------------------------
def set_V(m,c):
    control=True
    while(control):
        m=input('massa: ')
        try: 
            float(m)
            control=False
        except: print('valore non valido. Riprova. \n')
    m=float(m)
    control=True
    while(control):
        c=input('costante di potenziale:')
        try:
            float(c)
            control=False
        except: print('valore non valido. Riprova \n')
    c=float(c)
    return m,c

#Potenziali  -------------------------------------------------------
def V1(x,k):
    return k*x**2
def V2(x,k):
    return k*x**4
def V3(x,k):
    return k*x**6 
def V4(x,k):
    return k*abs(x)**(3/2)

#Periodo al variare della posizione iniziale per ogni potenziale  -------------------------------------------------------
def T(V,m,c,x_val,dx):
    y=np.empty(0) 
    s=np.empty(0) 
    t1= np.sqrt(8*m)
    arr1= np.array([x for x in x_val if x>=0])
    for j in arr1:
        arr2=np.arange(0,j,dx) #intervallo di integrazione
        #print(arr2)
        for l in arr2:
            t2=(np.sqrt(V(j,c)-V(l,c)))**(-1)
            #print(t2)
            y= np.append(y,t2)
        t3=integrate.simpson(y,arr2)
        y=np.empty(0)
        t4=t1*t3
        s=np.append(s,t4)
    return s

#Grafico dei potenziali  -------------------------------------------------------
def allv_plot(x_val,c):
    fig, (ax1,ax2) = plt.subplots(2,2, figsize=(8,6), layout='constrained')
    ax1[0].plot(x_val, V1(x_val,c), color='darkblue')
    ax1[0].axvline(color='k', linewidth=0.5)
    ax1[0].plot(4., V1(4.,c), 'o', markersize=10, color='r')
    ax1[0].set_ylabel(r'$V_1(x)$', fontsize=9)
    ax1[0].set_title(r"$v_1(x)=kx^2$", fontsize=12)

    ax2[0].plot(x_val, V3(x_val,c), color='darkblue')
    ax2[0].axvline(color='k', linewidth=0.5)
    ax2[0].plot(4.2, V3(4.2,c), 'o', markersize=10, color='r')
    ax2[0].set_xlabel('x', fontsize=9)
    ax2[0].set_ylabel(r'$V_3(x)$', fontsize=9)
    ax2[0].set_title(r"$v_3(x)=kx^6$", fontsize=12)

    ax1[1].plot(x_val, V2(x_val,c), color='darkblue')
    ax1[1].axvline(color='k', linewidth=0.5)
    ax1[1].plot(4., V2(4.,c), 'o', markersize=10, color='r')
    ax1[1].set_ylabel(r'$V_2(x)$', fontsize=9)
    ax1[1].set_title(r"$v_2(x)=kx^4$", fontsize=12)

    ax2[1].plot(x_val, V4(x_val,c), color='darkblue')
    ax2[1].axvline(color='k', linewidth=0.5)
    ax2[1].plot(3.5, V4(3.5,c), 'o', markersize=10, color='r')
    ax2[1].set_xlabel('x', fontsize=9)
    ax2[1].set_ylabel(r'$V_4(x)$', fontsize=9)
    ax2[1].set_title(r"$v_4(x)=k|x|^{3/2}$", fontsize=12)

    plt.show()

#Grafici dei potenziali separati  -------------------------------------------------------
def v1_plot(x_val,c):
    fig, ax= plt.subplots(1,1, figsize=(6,4), layout='constrained')
    ax.plot(x_val, V1(x_val,c), color='darkblue')
    ax.axvline(color='k', linewidth=0.5)
    ax.plot(4., V1(4.,c), 'o', markersize=10, color='r')
    ax.set_xlabel('x', fontsize=10)
    ax.set_ylabel(r'$V_1(x)$', fontsize=10)
    ax.set_title(r"$v_1(x)=kx^2$", fontsize=12)

    plt.show()

def v2_plot(x_val,c):
    fig, ax= plt.subplots(1,1, figsize=(6,4), layout='constrained')
    ax.plot(x_val, V2(x_val,c), color='darkblue')
    ax.axvline(color='k', linewidth=0.5)
    ax.plot(4., V2(4.,c), 'o', markersize=10, color='r')
    ax.set_xlabel('x', fontsize=10)
    ax.set_ylabel(r'$V_2(x)$', fontsize=10)
    ax.set_title(r"$v_2(x)=kx^4$", fontsize=12)

    plt.show()

def v3_plot(x_val, c):
    fig, ax= plt.subplots(1,1, figsize=(6,4), layout='constrained')
    ax.plot(x_val, V3(x_val,c), color='darkblue')
    ax.axvline(color='k', linewidth=0.5)
    ax.plot(4.2, V3(4.2,c), 'o', markersize=10, color='r')
    ax.set_xlabel('x', fontsize=10)
    ax.set_ylabel(r'$V_3(x)$', fontsize=10)
    ax.set_title(r"$v_3(x)=kx^6$", fontsize=12)

    plt.show()

def v4_plot(x_val,c):
    fig, ax= plt.subplots(1,1, figsize=(6,4), layout='constrained')
    ax.plot(x_val, V4(x_val,c), color='darkblue')
    ax.axvline(color='k', linewidth=0.5)
    ax.plot(3.5, V4(3.5,c), 'o', markersize=10, color='r')
    ax.set_xlabel('x', fontsize=10)
    ax.set_ylabel(r'$V_4(x)$', fontsize=10)
    ax.set_title(r"$v_4(x)=k|x|^{3/2}$", fontsize=12)

    plt.show()


#Grafico dei periodi  -------------------------------------------------------
def allp_plot(x_val,c, p):

    fig, (ax1,ax2) = plt.subplots(2,2, figsize=(8,6), layout='constrained')
    ax1[0].plot(x_val, p[0], color='teal')
    ax1[0].set_ylabel(r'$T_1(x_0) \; (s)$', fontsize=9)
    ax1[0].set_title(r"Periodi di oscillazione $V_1$", fontsize=12)

    ax2[0].plot(x_val, p[2], color='teal')
    ax2[0].set_xlabel(r'$x_0$', fontsize=9)
    ax2[0].set_ylabel(r'$T_3(x_0) \; (s)$', fontsize=9)
    ax2[0].set_title(r"Periodi di oscillazione $V_3$", fontsize=12)

    ax1[1].plot(x_val, p[1], color='teal')
    ax1[1].set_ylabel(r'$T_2(x_0) \; (s)$', fontsize=9)
    ax1[1].set_title(r"Periodi di oscillazione $V_2$", fontsize=12)

    ax2[1].plot(x_val, p[3], color='teal')
    ax2[1].set_xlabel(r'$x_0$', fontsize=9)
    ax2[1].set_ylabel(r'$T_4(x_0) \; (s)$', fontsize=9)
    ax2[1].set_title(r"Periodi di oscillazione $V_4$", fontsize=12)

    plt.show()

#Grafici dei periodi separati  -------------------------------------------------------
def p1_plot(x_val,c,p):
    fig, ax=plt.subplots(1,1, figsize=(6,4), layout='constrained')
    ax.plot(x_val, p[0], color='teal')
    ax.set_xlabel(r'$x_0$', fontsize=10)
    ax.set_ylabel(r'$T_1(x_0) \; (s)$', fontsize=10)
    ax.set_title(r"Periodi di oscillazione $V_1$", fontsize=12)

    plt.show()

def p2_plot(x_val,c,p):
    fig, ax=plt.subplots(1,1, figsize=(6,4), layout='constrained')
    ax.plot(x_val, p[1], color='teal')
    ax.set_xlabel(r'$x_0$', fontsize=10)
    ax.set_ylabel(r'$T_2(x_0) \; (s)$', fontsize=10)
    ax.set_title(r"Periodi di oscillazione $V_2$", fontsize=12)

    plt.show()

def p3_plot(x_val,c,p):
    fig, ax=plt.subplots(1,1, figsize=(6,4), layout='constrained')
    ax.plot(x_val, p[2], color='teal')
    ax.set_xlabel(r'$x_0$', fontsize=10)
    ax.set_ylabel(r'$T_3(x_0) \; (s)$', fontsize=10)
    ax.set_title(r"Periodi di oscillazione $V_3$", fontsize=12)

    plt.show()

def p4_plot(x_val,c,p):
    fig, ax=plt.subplots(1,1, figsize=(6,4), layout='constrained')
    ax.plot(x_val, p[3], color='teal')
    ax.set_xlabel(r'$x_0$', fontsize=10)
    ax.set_ylabel(r'$T_4(x_0) \; (s)$', fontsize=10)
    ax.set_title(r"Periodi di oscillazione $V_4$", fontsize=12)

    plt.show()

#Comportamento da terminale  -------------------------------------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(description= 'Periodi di oscillazione di potenziali al variare del punto iniziale')
    parser.add_argument('-v1','--v1_potential', action='store_true', help='show V1 potential graph')
    parser.add_argument('-v2','--v2_potential', action='store_true', help='show V2 potential graph')
    parser.add_argument('-v3','--v3_potential', action='store_true', help='show V3 potential graph' )
    parser.add_argument('-v4','--v4_potential', action='store_true', help='show V4 potential graph')
    parser.add_argument('-allv','--all_potentials', action='store_true', help='show potentials graph')
    parser.add_argument('-p1','--v1_periods', action='store_true', help='show V1 periods graph')
    parser.add_argument('-p2','--v2_periods', action='store_true', help='show V2 periods graph')
    parser.add_argument('-p3','--v3_periods', action='store_true', help='show V3 periods graph')
    parser.add_argument('-p4','--v4_periods', action='store_true', help='show V4 periods graph')
    parser.add_argument('-allp','--all_periods', action='store_true', help='show periods graph')

    return parser.parse_args()

#MAIN  -------------------------------------------------------
def main():
    dxx=0.1
    mass, k=2,2
    xx = np.arange(-5,5.05, 0.1)
    x_p=np.array([x for x in xx if x>=0])
    
    def calcola_p():
        p1=T(V1,mass,k,xx,dxx)
        p2=T(V2,mass,k,xx,dxx)
        p3=T(V3,mass,k,xx,dxx)
        p4=T(V4,mass,k,xx,dxx)
        return np.array([p1,p2,p3,p4])

    def imp():
        m,c=2,2
        m,c=set_V(m, c)  
        print('massa: {:} , k: {:}'.format(m, c))
        return m,c

    args=parse_arguments()
    if args.v1_potential == True:
        mass,k=imp()
        print((r"V_1(x) = {:} x^2".format(k)))
        v1_plot(xx,k)
    if args.v2_potential == True:
        mass,k=imp()
        print(r"V_2(x) ={:} x^4".format(k))
        v2_plot(xx,k)
    if args.v3_potential == True: 
        mass,k=imp()
        print(r"V_3(x) = {:} x^6".format(k))
        v3_plot(xx,k)
    if args.v4_potential == True:
        mass,k=imp()
        print(r"V_4(x) = {:} |x|^{3/2}".format(k))
        v4_plot(xx,k)
    if args.all_potentials == True:
        mass,k=imp()
        allv_plot(xx,k)
    if args.v1_periods == True:
        mass,k=imp()
        pp=calcola_p()
        print((r"V_1(x) = {:} x^2".format(k)))
        p1_plot(x_p,k,pp)
    if args.v2_periods == True:
        mass,k=imp()
        pp=calcola_p()
        print(r"V_2(x) ={:} x^4".format(k))
        p2_plot(x_p,k,pp)
    if args.v3_periods == True:
        mass,k=imp()
        pp=calcola_p()
        print(r"V_3(x) = {:} x^6".format(k))
        p3_plot(x_p,k,pp)
    if args.v4_periods == True:
        mass,k=imp()
        pp=calcola_p()
        print(r"V_4(x) = {:} |x|^{3/2}".format(k))
        p4_plot(x_p,k,pp)
    if args.all_periods == True:
        mass,k=imp()
        pp=calcola_p()
        allp_plot(x_p,k,pp)     

if __name__ == "__main__":
    main()