import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

########################################
#            DATI PER I FIT            #
########################################

#FUNZIONI AUSILIARIE
def datifit(o,e):
    """ Dati per fit 

    Parametri: 
    ---------
    e : array delle occorrenze in ciascuna classe di osservazione
    o : array dei valori per la distribuzione

    Restituisce:
    -----------
    ydata : array con valori per la distibuzione per rappresentante della classe di osservazione
    xdata : array asse x
    """

    #ydata
    ydata=np.empty(0)
    for k in e:
        for i in range(int(len(o)/(len(e)))):
            ydata=np.append(ydata, k)

    #xdata
    M=np.max(o)
    m=np.min(o)
    xdata=np.linspace(m,M,len(ydata))

    return ydata, xdata


def extr(mask):
    """ Selezione valori attorno al picco.

    Parametri: 
    ---------
    mask : maschera per valori attorno al picco

    Restituisce:
    -----------
    sx, dx: estremi per i bins selezionati attorno al picco
    """

    sx=0; dx=0
    step=0
    ceck=True
    for i in range(len(mask)):
        if(mask[i] == ceck and step <3):
            step=step+1
            if(step == 1): 
                sx = i
            if(step == 2): 
                dx = i-1
            ceck=not(ceck)
        else: continue
    return sx, dx               


def datifit_peak(d_mass, nd, bins):
    """ Dati per i fit attorno al picco

    Parametri: 
    ---------
    d_mass : array dei valori per la distribuzione
    nd     : array delle occorrenze in ciascuna classe di osservazione
    bins   : estremi delle classi dell'istogramma

    Restituisce:
    -----------
    dm_fit  : valori selezionati attorno al picco
    deltafit: estremi per i bins selezionati attorno al picco
    binsfit : bins selezionati per il fit attorno al picco
    ndfit   : occorrenze nelle classi selezionate attorno al picco
    """

    maskfit = (bins > 2.8) & (bins < 3.5) #maschera per valori attorno al picco
    binsfit=bins[maskfit]

    #NOTA:
    #print(len(bins), " ", len(nd))

    deltafit=extr(maskfit)
    ndfit=nd[deltafit[0] : deltafit[1]]
    dm_fit=np.array([x for x in d_mass if (x >= binsfit[0] and x <= binsfit[-1])])
    
    return dm_fit, ndfit, binsfit, deltafit


########################################
#          FUNZIONI DI FIT             #
########################################

# FUNZIONE FIT 1 --------------------
def fg1(x, A=1, m=1, p1=1,p0=1, sigma=1):
    """ Distribuzione Attesa Gaussiana + lineare.
    
    Parametri:
    ---------
    x: array of float
        valori sui quali calcolare la distribuzione
    A, m, p0, p1: float, default 1
        parametri di regressione

    Restituisce:
    -----------
    A*exp{(-x-m)^2/ 2*sigma^2} + p1*x + p0
    """
    esp= -(((x-m)**2)/(2*sigma**2))
    gauss=A*np.e**esp
    lt=p1*x
    return gauss+lt+p0


# FUNZIONE FIT 2 --------------------
def fg2(x, A1=1, A2=1, m=1, p1=1, p0=1, sigma1=1, sigma2=1):
    """ Distribuzione Attesa Gaussiana doppia + lineare.
    
    Parametri:
    ---------
    x: array of float
        valori sui quali calcolare la distribuzione
    A1, m: float, default 1
        parametri di regressione gaussiana 1
    A2, m: float, default 1
        parametri di regressione gaussiana 1
    p0, p1: float, default 1
        parametri di regressione lineare
    
   Restituisce:
   -----------
   fit di distribuzione dei dati 
   """

    A= np.array([A1, A2])
    sigma=np.array([sigma1, sigma2])
    gauss1=np.zeros(len(x))
    gauss2=np.zeros(len(x))
    gauss=np.array([gauss1, gauss2])
    for i in range((len(A))):
        esp= -((x-m)**2)/(2*sigma[i]**2)
        term=A[i]*np.e**esp
        gauss[i]=term
    #print(gauss)
    lt=p1*x
    return gauss[0]+gauss[1]+lt+p0


########################################
#                  FIT                 #
########################################

# FUNZIONE DI REGRESSIONE SUL FIT --------------------
def fit_regr(xx, yy, pstart, distr):
    """ Fit dei dati per la distribuzione 'distr'

    Parametri:
    ---------
    xx    : array dei valori sull'asse x selezionati per il fit
    yy    : array dei valori sull'asse y selezionati per il fit
    pstart: valori iniziali dei parametri per la distribuzione 'distr'
    distr : distribuzione attesa
    
    Restituisce:
    -----------
    params: valori ottimizzati dei parametri
    params_covariance: stima della covarianza dei parametri ottimizzati
    """

    params, params_covariance = optimize.curve_fit(distr, xx, yy, sigma=np.sqrt(yy), p0=[pstart])
    #print(len(fit))
    
    return params, params_covariance 


# STAMPA PARAMETRI DI REGRESSIONE
def display_regr(arg, p, covp):
    """ Stampa i parametri di regressione

    Parametri:
    ---------
    arg  : lista di stringhe contenete i nomi dei parametri della distribuzione
    p    : valori ottimizzati dei parametri
    covp : valori ottimizzati dei parametri
    """

    err_params=np.sqrt(covp.diagonal())
    #Stampa parametri di regressione
    print('Parametri di Regressione fit: \n')
    for i,j,k in zip(arg, p, err_params):
        print('{:6s}:{:>13.3f}+-{:.3f}'.format(i,j,k))
    print()


# GRAFICO FIT SULLA DISTRIBUZIONE --------------------
def fit_plot(d_mass, xx, fit, text, ptext):
    """ Grafico Fit

    Parametri:
    ---------
    d_mass : valori per la distribuzione
    xx     : array dei valori sull'asse x selezionati per il fit
    fit    : fit dei dati
    text   : stringa di testo sul grafico
    ptext  : array delle coordinate x, y della posizione del testo
    """

    fig, ax = plt.subplots(1,1, figsize=(6,4), layout='constrained', facecolor='lightgrey')
    ax.hist(d_mass, bins=125, color='darkcyan', alpha=0.7, label='dati')
    ax.plot(xx, fit, color='navy', label='fit', linewidth=1.3, linestyle='--')
    ax.text(ptext[0], ptext[1], text, fontsize=10, family='serif',color='darkblue')
    ax.set_title('Fit sull\'intera distribuzione', fontsize=11)
    ax.set_facecolor('whitesmoke')
    ax.set_ylabel('n.decadimenti '+r'$J/\psi \rightarrow \mu \mu $', fontsize=9)
    ax.set_xlabel(r'$mc^2$', fontsize=9)
    ax.legend(fontsize=10)

    return fig


# GRAFICO FIT SUL PICCO --------------------
def fitp_plot(d_mass, binsfit, xx, fit, text, ptext):
    """ Grafico Fit attorno al picco

    Parametri:
    ---------
    d_mass : valori per la distribuzione
    binsfit: bins selezionati per il fit
    xx     : array dei valori sull'asse x selezionati per il fit
    fit    : fit dei dati
    text   : stringa di testo sul grafico
    ptext  : array delle coordinate x, y della posizione del testo
    """

    fig, ax = plt.subplots(1,1, figsize=(6,4), layout='constrained', facecolor='lightgrey')
    ax.hist(d_mass, bins=125, color='darkcyan', alpha=0.7, label='dati')
    ax.set_xlim(binsfit[0], binsfit[-1])
    ax.plot(xx, fit, color='navy', label='fit1', linewidth=1.3)
    ax.text(ptext[0], ptext[1], text, fontsize=10, family='serif',color='darkblue')
    ax.set_title('Fit attorno al picco', fontsize=11)
    ax.set_facecolor('whitesmoke')
    ax.set_ylabel('n.decadimenti '+r'$J/\psi \rightarrow \mu \mu $', fontsize=9)
    ax.set_xlabel(r'$mc^2$', fontsize=9)
    ax.legend(fontsize=10)

    return fig


# RISULTATI FIT --------------------
def par_fit(d_mass, xdata, ndfit, binsfit, fit, fitchi, gapsfit, sigmay):
    """ Pannello che mostra i risultati del fit

    Parametri:
    ---------
    d_mass : valori per la distribuzione
    xx     : array dei valori sull'asse x selezionati per il fit
    ndfit  : occorrenze nelle classi selezionate per il fit
    binsfit: bins selezionati per il fit
    fit    : fit dei dati
    fitchi : fit dei dati per i valori sui bins
    gapsfit: scarti dati-fit
    sigmay : incertezza nelle variabili della distribuzione calcolata
    """
    
    fig = plt.figure(figsize=(9,6), facecolor='lightgrey')
    gs = fig.add_gridspec(3,1, hspace=0.1, wspace=0)
    ax1,ax2, ax3= gs.subplots()
    fig.suptitle('Fit1/Dati', fontsize=14)

    #Fit
    ax1.hist(d_mass, bins=125, color='darkcyan', alpha=0.7, label='dati')
    ax1.set_xlim(binsfit[0], binsfit[-1])
    ax1.plot(xdata, fit, color='navy', label='fit1', linewidth=1.2)
    #ax1.text(3.7, 5800,r'$f_{g1}(x) = A e^{-\frac{x - m}{2 \sigma^2}} + p_1 x + p_0$', fontsize=12, family='serif',color='darkblue')
    ax1.set_ylabel('n.decadimenti '+r'$J/\psi \rightarrow \mu \mu $', fontsize=10)
    ax1.set_facecolor('whitesmoke')
    #ax1.tick_params('x', labelbottom=False)
    ax1.legend(fontsize=12)

    #Scarti
    ax2.errorbar(binsfit[:-1], gapsfit, yerr=np.abs(sigmay), fmt='o',color ='royalblue', label='scarti bins')
    #ax2.plot(xx1, gapslfit1, color='grey', label='scarti')
    ax2.axhline(0, color='darkorange') 
    ax2.set_ylabel('scarti (dati/fit)', fontsize=10)
    ax2.set_xlabel(r'$mc^2$', fontsize=10)
    ax2.set_facecolor('whitesmoke')
    ax2.legend(fontsize=12)

    #Scarti/errore  
    ax3.errorbar(binsfit[:-1], (fitchi/ndfit), yerr=np.abs(sigmay), fmt='o',color ='royalblue', label='dati/fit bins')
    #ax3.plot(xx1, (fit1peak/yy1), color='grey', label='dati/fit')
    ax3.axhline(1, color='darkorange') 
    ax3.set_ylabel('dati/fit', fontsize=10)
    ax3.set_xlabel(r'$mc^2$', fontsize=10)
    ax3.set_facecolor('whitesmoke')
    ax3.legend(fontsize=12)

    for ax in fig.get_axes():
        ax.label_outer()
    
    return fig


# TEST CHI^2 --------------------
def chi_test(f, n, bins, ndfit, fit_params):
    """ Implementazione del test del chi quadrato

    Parametri:
    ---------
    f    : distribuzione attesa 
    n    : intero che individua la distribuzione selezionata 
           n= {1,2}
    bins : bins selezionati per il test
    ndfit: occorrenze delle classi selezionate per il test
    fit_params: parametri usati per definire l'ipotesi di distribuzione
    
   Restituisce:
   -----------
   gapsfit: scarti
   chi2   : chi quadrato calcolato per la distribuzione attesa
   chi2_r : chi quadrato ridotto
   gdl    : gradi di libertà
   """
    if (n==1):
        fit=f(bins[:-1], fit_params[0], fit_params[1], fit_params[2], 
              fit_params[3], fit_params[4])
    elif (n==2):
        fit=f(bins[:-1], fit_params[0], fit_params[1], fit_params[2], fit_params[3], 
              fit_params[4], fit_params[5], fit_params[6])
    else:
        print("distribuzione selezionata non valida. RIPROVARE!")

    gapsfit=(ndfit - fit)
    chi2=np.sum((gapsfit)**2/ndfit)

    #numero di gdl
    gdl=len(ndfit) - len(fit_params-1)
    #ch12 ridotto
    chi2_r=chi2/gdl

    return gapsfit, chi2, chi2_r, gdl