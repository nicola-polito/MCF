import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import pandas as pd
import argparse

# DATI -------------------
osc_data=pd.read_csv('/home/nicola_polito/MCF/dati/dati-e6/oscilloscope.csv', sep=',')
#array dai dati
CH1= np.array([osc_data['time'], osc_data['signal1']])
print(CH1[0]) #-->time
print(CH1[1]) #-->signal1
CH2= np.array([osc_data['time'], osc_data['signal2']])
print(CH2[1]) # --<signal2


# CALCOLO DERIVATE DEI SEGNALI CON LA DIFFRENZA CENTRALE -------------------

#general central_diff function
def central_diffg(xx, yy, nh):
    dd = yy[nh:] - yy[:-nh]
    hh = xx[nh:] - xx[:-nh]
    for ih in range(int(nh/2)):
        dd = np.append(yy[nh-ih-1]-yy[0], dd)
        dd = np.append(dd, yy[-1]-yy[-(nh-ih)])
    
        hh = np.append(xx[nh-ih-1]-xx[0], hh)
        hh = np.append(hh, xx[-1]-xx[-(nh-ih)])
    
    return dd/hh

# n_h=2
dc2_ch1=central_diffg(CH1[0], CH1[1], 2)
dc2_ch2=central_diffg(CH2[0], CH2[1], 2)
# n_h=100
dc100_ch1=central_diffg(CH1[0], CH1[1], 100)
dc100_ch2=central_diffg(CH2[0], CH2[1], 100)

der_sig1 = np.convolve(dc100_ch1,  np.ones(5), 'same') / 5
der_sig2 = np.convolve(dc100_ch2,  np.ones(5), 'same') / 5


# RICERCA MINIMI DEI SEGNALI -------------------

def min_seek():
    selmask_sig1= (np.abs(der_sig1) < 0.015) & (CH1[1]<-10)
    selmask_sig2= (np.abs(der_sig2) < 0.015) & (CH2[1]<-10)

    #print('---der0 sig1 ---', CH1[0][selmask_sig1])
    #print('---der0 sig2 ---', CH2[0][selmask_sig2])

    # accorpamento punti per Canale 1
    tpeak_sig1 = np.empty(0)
    vpeak_sig1 = np.empty(0)
    tsum = int(CH1[0][selmask_sig1][0])
    nsum = 1

    for it in range(1, len(CH1[0][selmask_sig1])):
        if((CH1[0][selmask_sig1][it] - CH1[0][selmask_sig1][it-1] >20) or (it == len(CH1[0][selmask_sig1])-1)):
            #print(tsum)
            tpeak_sig1=np.append(tpeak_sig1, tsum)
            vpeak_sig1=np.append(vpeak_sig1, CH1[1][tsum] )
            tsum=int(CH1[0][selmask_sig1][it])

    # accorpamento punti per Canale 2
    tpeak_sig2 = np.empty(0)
    vpeak_sig2 = np.empty(0)
    tsum = int(CH2[0][selmask_sig2][0])
    nsum = 1

    for it in range(1, len(CH2[0][selmask_sig1])):
        if((CH2[0][selmask_sig2][it] - CH2[0][selmask_sig2][it-1] >20) or (it == len(CH2[0][selmask_sig1])-1)):
            #print(tsum)
            tpeak_sig2=np.append(tpeak_sig2, tsum)
            vpeak_sig2=np.append(vpeak_sig2,CH2[1][tsum])
            tsum=int(CH2[0][selmask_sig2][it])

    return (tpeak_sig1, vpeak_sig1), (tpeak_sig2, vpeak_sig2)


# GRAFICI CANALI -------------------
def signals_plot():
    fig, ax=plt.subplots(2,1, figsize=(8,5), layout='constrained')
    fig.suptitle("Segnali in uscita all'oscilloscopio")
    ax[0].set_title('Canale 1')
    ax[0].plot(CH1[0],CH1[1], label='CH1')
    ax[0].set_ylabel('signal1 (mV)')
    ax[1].set_title('Canale 2')
    ax[1].plot(CH2[0],CH2[1], label='CH2')
    ax[1].set_ylabel('signal2 (mV)')

    for a in ax.flat:
        a.set(xlabel='time (ns)')
        a.legend()
    plt.show(block=True)


# GRAFICI SEGNALI DERIVATI -------------------
def der_sig_plot():

    fig1, ax=plt.subplots(2,1, figsize=(10,6), layout='constrained')
    fig1.suptitle("Derivata dei segnali tramite differenza centrale")
    ax[0].set_title('Canale 1')
    ax[0].plot(CH1[0], dc2_ch1, label=r'$\frac{d(sign1)}{dt}, n_h=2$', alpha=0.7)
    ax[0].plot(CH1[0], dc100_ch1, label=r'$\frac{d(sign1)}{dt}, n_h=100$', alpha=0.7)
    ax[0].set_ylabel('signal1 (mV/ns)')
    ax[1].set_title('Canale 2')
    ax[1].plot(CH1[0], dc2_ch2, label=r'$\frac{d(sign2)}{dt}, n_h=2$', alpha=0.7)
    ax[1].plot(CH1[0], dc100_ch2, label=r'$\frac{d(sign2)}{dt}, n_h=100$', alpha=0.7)
    ax[1].set_ylabel('signal2 (mV/ns)')

    for a in ax.flat:
        a.set(xlabel='time (ns)')
        a.legend()
        #a.set_xlim(9600,10300)


    # grafico derivata dh=100 avg 5
    fig2, ax=plt.subplots(figsize=(8, 6), layout='constrained')
    ax.set_title('Derivata Segnali Oscilloscopio - h=100 ns - media 5', fontsize=12, color='slategray')
    ax.plot(CH1[0], der_sig1, color='limegreen',   label='Canale 1')
    ax.plot(CH2[0], der_sig2, color='darkorange',  label='Canale 2', alpha=0.8)                 
    ax.legend(fontsize=9)
    ax.set_xlabel('t (ns)')
    ax.set_ylabel('V/s (mV/ns)')

    plt.show(block=True)


# GRAFICO MINIMO DEI SEGNALI -------------------
def min_sig_plot():    

    (tps1,vps1), (tps2,vps2)=min_seek()
    plt.subplots(figsize=(8,6))
    plt.title('Segnali Oscilloscopio con Minimi identificati', fontsize=12, color='slategray')
    plt.plot( CH1[0], CH1[1], color='limegreen',  label='Canale 1', alpha=0.7 )
    plt.plot( CH2[0], CH2[1], color='darkorange', label='Canale 2', alpha=0.7 )
    plt.plot( tps1, vps1, 'o', color='darkgreen',  label='Min. Canale 1' )
    plt.plot( tps2, vps2, 'o', color='red',        label='Min. Canale 2' )
    plt.legend(fontsize=9)
    plt.xlabel('t (ns)')
    plt.ylabel('V (mV)')
    plt.ylim(-90, 10)

    plt.show(block=True)


# CONFRONTO TRA I DUE CANALI -------------------
def same_ch(tps1,vps1, tps2,vps2):
    tcoin1 = np.empty(0)
    tcoin2 = np.empty(0)
    vcoin1 = np.empty(0)
    vcoin2 = np.empty(0)

    window = 200
    for t1, v1 in zip(tps1, vps1):

        for t2, v2 in zip(tps2, vps2):
            if np.abs(t2-t1) < window:
                tcoin1 = np.append(tcoin1, t1)
                tcoin2 = np.append(tcoin2, t2)
                vcoin1 = np.append(vcoin1, v1)
                vcoin2 = np.append(vcoin2, v2)
            if t2 > t1 :
                break
    
    return (tcoin1, vcoin1), (tcoin2, vcoin2)


# GESTIONE DELLO SCRIPT DA RIGA DI COMANDO -------------------
def parse_arguments():
    parser=argparse.ArgumentParser( description='Analisi Segnali Oscillosopio a 2 Canali',
                                   usage= 'python3 e6_e3.py  --opzione')
    parser.add_argument('-dset', '--dataset', action='store', 
                        default='/home/nicola_polito/MCF/dati/dati-e6/oscilloscope.csv', 
                        help='Segnali raccolti dai 2 canali dell oscilloscopio')
    parser.add_argument('-ch', '--channels', action='store_true', help='Grafici dei segnali in uscita dai 2 canali')
    parser.add_argument('-dc', '--der_sig', action='store_true', help='Derivate dei Segnali')
    parser.add_argument('-min', '--min_sig', action='store_true', help='Minimi dei Seganali')
    parser.add_argument('-cmp', '--compare_channels', action='store_true', help='Confronto tra i due canali')

    return parser.parse_args()


# MAIN -------------------
def oscilloscope_analysis():

    args=parse_arguments()
    osc_data=pd.read_csv(args.dataset, sep=',')
    print(osc_data.columns)

    if args.channels == True:
        signals_plot()
    if args.der_sig == True:
        der_sig_plot()
    if args.min_sig == True:
        min_sig_plot()
    if args.compare_channels == True:
       (tp_s1,vp_s1), (tp_s2,vp_s2)=min_seek()
       (tc1, vc1), (tc2, vc2)=same_ch(tp_s1,vp_s1,tp_s2,vp_s2)
       
       print('--------------------------------------------')
       print(' Numero Coincidenze        :', len(tc1) )
       print(' Tempo Coincidenze Canale 1:', tc1)
       print(' Tempo Coincidenze Canale 2:', tc2)
       print(' Coincidenze t2-t1         :', tc2-tc1)
       print(' Efficenza Canale 1        : {:.2f}'.format( len(tc1)/len(tp_s1)) )
       print(' Efficenza Canale 2        : {:.2f}'.format( len(tc2)/len(tp_s2)) )
    
if __name__=="__main__":
   oscilloscope_analysis()