import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import argparse

import massa_invariante as minv
import fit_for_E7 as fit_e7


############################################
# GESTIONE DELLO SCRIPT DA RIGA DI COMANDO #
############################################

def parse_arguments():
    parser=argparse.ArgumentParser(description='fit massa invariante decadimento mesone J', 
                                   usage= 'python3 e7_e1.py  --opzione')
    
    parser.add_argument('-d', '--data', action='store_true', help='dati dell\'esperimento')
    parser.add_argument('-dh','--dmHist', action='store_true', help='istogramma delle masse invarianti')

    parser.add_argument('-fit', '--fit_distr', action='store', type=int, choices=[1,2], help=' mostra il fit per la distribuzione selezionata')

    parser.add_argument('-test', '--fit_test', action='store', type=int, choices=[1,2], help='mostra i risultati del fit per la distribuzione selezionata') 
    
    parser.add_argument('-chi','--chi_test', action='store', type=int, choices=[1,2], help='test del chi quadrato per la distribuzione selezionata')

    return parser.parse_args()


########################################
#                 MAIN                 #      
########################################

def J_meson_decay():
    dataset= pd.read_csv('/home/nicola_polito/MCF/dati/dati-e7/Jpsi_mumu.csv', sep=',')

    # MASS DISTRIBUTION -----------------------
    d_m=minv.data_distr(dataset)
    hist_m=minv.distr_hist(d_m)
    hist_mp=minv.distr_hist_peak(d_m)
    values=hist_m[0]   # numero di occorrenze in ciascuna classe
    delta=hist_m[1]    # estremi bins

    # DISTRIBUTIONS -----------------------
    text1= r'$f_{g1}(x) = A e^{-\frac{x - m}{2 \sigma^2}} + p_1 x + p_0$'
    arg1=['A', 'm', 'p1', 'p0','sigma']
    ptext1= [3.7, 2600]
    ptext1p=[3.2, 2200]

    text2 = r'$f_{g2}(x) = A_1 e^{-\frac{x - m}{2 \sigma_1^2}} + A_2 e^{-\frac{x - m}{2 \sigma_2^2}} + p_1 x + p_0$'
    arg2=['A1', 'A2', 'm', 'p1', 'p0','sigma1', 'sigma2']
    ptext2=[3.4, 2300]
    ptext2p=[3.15, 2200]

    #DATA FOR FIT -----------------------
    yy, xx = fit_e7.datifit(d_m, values)
    
    #DATA FOR FIT AROUND PEAK -----------------------
    dm_fit,  vfit, bfit, extrfit= fit_e7.datifit_peak(d_m, values, delta)
    
    '''
    print('Intervalli selezionanati per Fit:')
    for k in range(len(vfit)):
        print('{:0.3f} : {:0.3f} --> {:.0f}'.format(bfit[k], bfit[k+1], vfit[k]))
    '''
    
    yy1, xx1=fit_e7.datifit(dm_fit, vfit)
    #print(len(yy1), len(xx1))

    #FIT 1 -----------------------
    pstart1=np.ones(5, dtype=int) 
    params_f1, params_f1_cov= fit_e7.fit_regr(xx, yy, pstart1, fit_e7.fg1)
    fit1=fit_e7.fg1(xx, params_f1[0], params_f1[1], params_f1[2], params_f1[3], params_f1[4])

    #FIT 1 around peak -----------------------
    params_f1p, params_f1p_cov= fit_e7.fit_regr(xx1, yy1, pstart1, fit_e7.fg1)
    fit1peak=fit_e7.fg1(xx1, params_f1p[0], params_f1p[1], params_f1p[2], params_f1p[3], params_f1p[4])
    chi1=fit_e7.chi_test(fit_e7.fg1, 1, bfit, vfit, params_f1p)
    fit1exp=fit_e7.fg1(bfit[:-1], params_f1p[0], params_f1p[1], params_f1p[2], params_f1p[3], params_f1p[4])

    #FIT 2
    pstart2=np.ones(7, dtype=int)
    params_f2, params_f2_cov = fit_e7.fit_regr(xx, yy, pstart2, fit_e7.fg2)
    fit2=fit_e7.fg2(xx, params_f2[0], params_f2[1], params_f2[2], params_f2[3], params_f2[4], 
                  params_f2[5], params_f2[6])

    #FIT 2 around peak -----------------------
    params_f2p, params_f2p_cov= fit_e7.fit_regr(xx1, yy1, pstart2, fit_e7.fg2)
    fit2peak=fit_e7.fg2(xx1, params_f2p[0], params_f2p[1], params_f2p[2], params_f2p[3], 
                   params_f2p[4], params_f2p[5], params_f2p[6])
    chi2=fit_e7.chi_test(fit_e7.fg2, 2, bfit, vfit, params_f2p)
    fit2exp=fit_e7.fg2(bfit[:-1], params_f2p[0], params_f2p[1], params_f2p[2], params_f2p[3], 
                       params_f2p[4], params_f2p[5], params_f2p[6])


    #CLI
    args=parse_arguments()

    if args.data == True:
        print('Dati Esperimento: \n')
        f=open('/home/nicola_polito/MCF/dati/dati-e7/Jpsi_mumu.csv', 'rt')
        count=0
        for line in f:
            if(count<=5):
                print(line, '\n')
                count+=1
            else: break    
        f.close() 

    if args.dmHist == True:
        hist_m
        plt.show(block=True)
        hist_mp
        plt.show(block=True)

    if args.fit_distr == 1:
        plt.ion()       # Modalità interattiva ON

        print("Fit 1 sull'intera distribuzione \n")
        fit_e7.display_regr(arg1, params_f1, params_f1_cov)
        fig1=fit_e7.fit_plot(d_m, xx, fit1, text1, ptext1) 
        fig1.show()
        input("premi INVIO per continuare... \n")

        print("Fit 1 sul Picco \n")
        fit_e7.display_regr(arg1, params_f1p, params_f1p_cov)
        fig1p=fit_e7.fitp_plot(d_m, bfit, xx1, fit1peak, text1, ptext1p)
        fig1p.show()
        input("premi INVIO per continuare... \n")

    if args.fit_distr == 2:
        plt.ion()       # Modalità interattiva ON

        print("Fit 2 sull'intera distribuzione \n")
        fit_e7.display_regr(arg2, params_f2, params_f2_cov)
        fig2=fit_e7.fit_plot(d_m, xx, fit2, text2, ptext2)
        fig2.show()
        input("premi INVIO per continuare... \n")

        print("Fit 2 sul Picco \n")
        fit_e7.display_regr(arg2, params_f2p, params_f2p_cov)
        fig2p=fit_e7.fitp_plot(d_m, bfit, xx1, fit2peak, text2, ptext2p)
        fig2p.show()
        input("premi INVIO per continuare... \n")

    if args.chi_test == 1:
        print("Test del chi quadrato per la Distribuzione 1: \n")
        print('chi2: {:.3f} , chi2 ridotto: {:.3f} , n.grad di libertà: {:d}'.format(chi1[1], chi1[2], chi1[3]))

    if args.chi_test == 2:
        print("Test del chi quadrato per la Distribuzione 2: \n")
        print('chi2: {:.3f} , chi2 ridotto: {:.3f} , n.grad di libertà: {:d}'.format(chi2[1], chi2[2], chi2[3]))

    if args.fit_test == 1:
        plt.ion()       # Modalità interattiva ON

        print("Risultati Fit 1 \n")
        figpar1=fit_e7.par_fit(d_m, xx1, vfit, bfit, fit1peak, fit1exp, chi1[0], params_f1p[4])
        figpar1.show()
        input("premi INVIO per continuare... \n")
    
    if args.fit_test == 2:
        plt.ion()       # Modalità interattiva ON

        print("Risultati Fit 2 \n")
        figpar2=fit_e7.par_fit(d_m, xx1, vfit, bfit, fit2peak, fit2exp, chi2[0], params_f2p[6])
        figpar2.show()
        input("premi INVIO per continuare... \n")


if __name__ == '__main__':
    J_meson_decay()