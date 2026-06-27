import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from PIL import Image


########################################
#                MWPC                  #
########################################

#CAMPO ELETTRICO IN UNA MWPC
def ef_lines():
    fig, ax = plt.subplots(figsize=(6,5))
    ax.imshow(np.asarray(Image.open('/home/nicola_polito/MCF/E10/MWPC/MWPC_electric_field.svg.png')))
    ax.set_title('Linee del Campo Elettrico in una MWPC', color='grey')
    ax.axis('off')
    return fig

#GEOMETRIA MWPC
class MWPC:
    '''
    Classe che implementa la geometria di una MWPC

    s      : spessore della camera (distanza tra i due piani catodici)
    l      : dimensione longitudinale della camera (parallela ai fili)
    n_wires: numero di fili anodici
    d_sw   : distanza tra fili e piani catodici
    d_ww   : distanza trasversale tra i fili
    ef     : campo elettrico all'interno della camera
    '''

    def __init__(self):
        self.s=1 #cm
        self.l=2 #cm
        self.n_wires= 5
        self.d_sw=0.5 #cm
        self.d_ww=0.3 #cm
        self.ef= self.mwpc_ef()

    def mwpc_set(self, settings):
        self.s= settings[0]
        self.n_wires=settings[1]
        self.d_sw=settings[2]
        self.d_ww=settings[3]
        self.pe=settings[4]
    
    def mwpc_ef(self):
        yc=np.random.random(1000) #campo nella direzione trasversale ai fili
        xc=np.random.uniform(low=0, high=2, size=1000)
        e_f=np.array([xc,yc])
        return e_f
    
    def r_wire(self):
        xw=np.arange(0.3, 2 ,0.3)
        yw=self.d_sw
        t=np.array([.0,.0])
        rw=np.array([t for x in range(len(xw))])
        for i in range(len(xw)):
            rw[i]=np.array([xw[i],yw])
        return rw



########################################
#        SIMULAZIONE  FENOMENO         #
########################################

#GENERAZIONE COPPIE ELETTRONE-IONE
class mwpc_genEI():
    """
    Classe che simula la generazione di coppie elettrone-ione in una mwpc

    np   : numero atteso di coppie elettrone-ione generate dalla distribuzione di poisson
    n_ei : numero di coppie elettrone-ione primarie, per evento
    p_ei : posizione coppie elettrone-ione primarie generate
    """
    
    def __init__(self):
        self.n_ei=0
        self.p_ei=np.empty(0)
        self.np = 5

    def ei_pair(self, mwpc):
        """
        ei_pair(): funzione che simula la generazione casuale di coppie elettrone-ione all'interno della camera:
            - il numero di coppie è regolato dalla distribuzione di poisson
            - la posizione delle coppie ha distribuzione uniforme lungo lo spessore della camera

        return p_ei, n_ei : posizione delle coppie generate, numero di coppie generate (per evento)
        """
        self.n_ei=np.random.poisson(self.np)
        t=np.array([0.0, 0.0])
        self.p_ei=np.array([t for x in range(self.n_ei)])
        for i in range(self.n_ei):
            y_ei=np.random.uniform(low=0, high=mwpc.s)
            x_ei=np.random.uniform(low=0, high=2)
            self.p_ei[i]=np.array([x_ei, y_ei])

    def __repr__(self):
        return ' Numero coppie elettrone-ione generate ionizzazione primaria: {:d} \
                \n Posizione coppie elettrone-ione generate ionizzazione primaria: \n {:} \n'.format(self.n_ei, self.p_ei)
    
    def __str__(self):
        return ' Numero coppie elettrone-ione generate ionizzazione primaria: {:d} \
                \n Posizione coppie elettrone-ione generate ionizzazione primaria: \n {:} \n'.format(self.n_ei, self.p_ei)
    

#PROCESSO DI DIFFUSIONE DI UN ELETTRONE E RIVELAMENTO PARTICELLA CARICA
class mwpc_event():
    """
    Classe che implementa la diffusione di una coppia e-i di generazione primaria in una mwpc
        params:
            su      : passo della diffusione per agitazione termica (cm)
            sf      : passo della diffusione per effetto del campo elettrico (cm)
            nr      : numero atteso di elettroni riassorbiti (1/nr --> probabilità di riassorbimento)
            tc      : tempo medio fra due urti durante la diffusione

            near_wire: anodo più vicino
            r_ei     : spostamento degli elettroni (cm)
            n_passi  : numero di passi della diffusione
            riv      : indice di rilevamento della particella carica
            td       : tempo di deriva degli elettroni

        set{params : val1}, default : val1
            parametri del processo
    """

    def __init__(self):
        self.near_wire=np.array([0,0])
        self.r_ei=np.empty(0)
        self.n_passi=0
        self.riv = True
        self.td=0

        self.params=('su', 'sf', 'nr', 'tc')
        self.val1= np.array([1e-5, 10e-5, 1e7, 1e-12]) #1e-7
        self.val2= np.array([1e-4, 5e-5, 1e4, 1e-12]) #5e-5
        self.set={ self.params[i]: j for i,j in zip(range(len(self.val1)), self.val1)}

    def set_p(self):
        print('SET 1: \n----- \n')
        for l,k in zip(self.params, self.val1):
            print(l, '=', k, '\n')
        print('SET2: \n----- \n')
        for l,k in zip(self.params, self.val2):
            print(l, '=', k, '\n')
        while(True):
            select=input('Select setting:')
            if(select == 'SET 1'):
                break
            if(select == 'SET 2'):
                self.set={ self.params[i]: j for i,j in zip(range(len(self.val2)),self.val2)}
                break
         
    def ei_diffusion(self, mwpc, pstart):
        '''
        ei_diffusion(pstart, step_t, step_e, rc): Simulazione del moto di diffusione delle coppie elettrone-ione: 
        - gli elettroni migrano verso il filo più vicino
        - una volta rilevato l'anodo più vicino, la diffusione avviene solo lungo la direzione trasversale ai fili (direzione del campo elettrico)
    
        mwpc  : rivelatore in cui avviene la diffusione
        pstart: posizione di generazione della coppia e-i

        return r_ei, n_passi: vettore che tiene traccia dello spostamento e numero di passi degli elettroni
        '''
    
        #condizioni iniziali
        self.r_ei=np.array(pstart[1])
        y_ei=pstart[1]
        e_step=self.set['sf']

        #rilevazione dell'anodo più vicino
        r=mwpc.r_wire()
        self.near_wire=r[0]
        m_wire=np.linalg.norm(r[0]-pstart)
        for p in r:
            term=np.linalg.norm(p-pstart)
            if(term < m_wire):
                m_wire=term
                self.near_wire=p
    
        #implementazione processo di diffusione per una coppia e-i
        #se la distanza dell'elettrone dal filo lungo la componente del campo è inferiore a 0.1 mm, si considera l'elettrone come rivelato con successo
        while(np.abs(y_ei - self.near_wire[1])>=0.1): 
            rc= np.random.poisson(1/self.set['nr']) #probabilità di riassorbimento
            #se l'elettrone è stato riassorbito o non ha raggiunto un piano catodico, la coppia non viene rivelata
            if(rc != 0 or y_ei>= mwpc.s or y_ei <=0):
                self.riv=False
                break

            y_ei= y_ei + self.set['su'] + e_step
            self.n_passi +=1
            self.r_ei=np.append(self.r_ei, y_ei)
            #print(t)
        if(self.riv == True):  
            self.r_ei=np.append(self.r_ei, self.near_wire[1])


    def derive_time(self):
        self.td=self.n_passi*self.set['tc']
    
    def __repr__(self): 
        return' Rivelato: {:} \n Anodo più vicino: {:} ' \
        '\n Numero Passi: {:d}  \n tempo di deriva per l\'evento: {:} secondi \n'.format(self.riv, self.near_wire, self.n_passi, self.td)
    
    def __str__(self): 
        return' Rivelato: {:} \n Anodo più vicino: {:} ' \
        '\n Numero Passi: {:d}  \n tempo di deriva per l\'evento: {:} secondi \n'.format(self.riv, self.near_wire, self.n_passi, self.td)
        

#DIFFUISONE DEGLI ELETTRONI
class mwpc_diffusion():
    """
    Classe che implementa la diffusione di un certo numero di elettroni in una mwpc

    nei_pair : numero di coppie elettrone-ione generate
    nei_riv  : numero di elettroni rivelati
    n_step   : numero di passi per ogni elettrone rivelato
    nei_td   : tempi di deriva per ogni elettrone rivelato
    nei_p    : posizione iniziale delle coppie di ionizzazione primaria
    y_ei     : spostamento di ciascun elettrone
    """

    def __init__(self, cp):
        self.nei_riv =0
        self.nei_pair=0
        self.nei_td =np.empty(0)
        self.n_step=np.empty(0)
        
        #coppie e-i generate e posizione
        self.pair2=mwpc_genEI()
        self.pair2.ei_pair(cp)
        self.nei_p=self.pair2.p_ei
        
        #Evento
        self.t= mwpc_event()

        #Array contenente i singoli eventi
        self.esp = np.empty(0)
    
    #Set Evento
    def setting1(self):
        self.t.set_p()
    
    def setting2(self, params):
        if(params=="SET 2"):
            self.t.set={self.t.params[i]: j for i,j in zip(range(len(self.t.val2)),self.t.val2)}

    def events(self):
        print('\n Il processo di diffusione ha registrato {:d} eventi: \n'.format(self.nei_riv))
        print(self.pair2)
        for i,k in zip(range(len(self.esp)), self.esp):
            print( " Evento {:}: \n --------".format(i+1))
            print(k)

    #PROCESSO DI DIFFUSIONE    
    def diff_process(self, cp):    
        for i,k in zip( range(len(self.pair2.p_ei)), self.pair2.p_ei):
            self.t= mwpc_event()
            y_ei=np.empty(0)
            self.esp=np.append(self.esp, self.t)
            self.t.ei_diffusion(cp,k)
            y_ei = np.append(y_ei, self.esp[i].r_ei)

            self.n_step= np.append(self.n_step, self.esp[i].n_passi)

            self.esp[i].derive_time()
            self.nei_td=np.append(self.nei_td, self.esp[i].td)
            self.nei_pair=self.pair2.n_ei

            if self.esp[i].riv == True:
                self.nei_riv +=1