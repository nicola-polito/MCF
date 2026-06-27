import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import argparse
from tqdm import tqdm
import time

import mwpc_implementation as rivelatore
import diffusion_exp as exp


############################################
# GESTIONE DELLO SCRIPT DA RIGA DI COMANDO #
############################################

def parse_arguments():
    parser=argparse.ArgumentParser(description='Simulazione della diffusione di particelle cariche in una MWPC', 
                                   usage= 'python3 E10_e1.py  --opzione')
    parser.add_argument('-ef', '--campoE', action='store_true', help='Campo Elettrico all\'interno della MWPC')
    parser.add_argument('-sim', '--evento', action='store_true', help='Simula un evento')
    parser.add_argument('-diff', '--diffusione', action='store_true', help='Simula diffusione elettroni')
    parser.add_argument('-exp', '--esperimento', action='store_true', help='Simula un esperimento')
    
    return parser.parse_args()


########################################
#                 MAIN                 #      
########################################

def mwpc_sim():
    print("Camera Proporzionale a Multifili per la rivelazione di particelle cariche. \n")
    CP=rivelatore.MWPC()
    r=CP.r_wire()
    print('Posizione fili: \n',r)
    print()

    args=parse_arguments()
    if args.campoE == True:
        rivelatore.ef_lines()

    if args.evento == True:
        pair1=rivelatore.mwpc_genEI()
        pair1.ei_pair(CP)
        sim1=rivelatore.mwpc_event()
        sim1.ei_diffusion(CP, pair1.p_ei[0])
        sim1.derive_time()
        print(sim1)

    if args.diffusione == True:
        SIM1=rivelatore.mwpc_diffusion(CP)
        SIM1.setting1()
        SIM1.diff_process(CP)
        SIM1.events()
    
    if args.esperimento == True:
        plt.ion() #MODALITA INTERATTIVA
        N=500
        ESP1=exp.esperimento(CP)
        ESP1.setting()
        ESP1.sim(N)
        #tqdm
        eff1, eff2=exp.efficienza_mwpc(ESP1)
        print()
        print('Efficienza di rivelazione di un elettrone: {:0.1f} % \n' \
        'Efficienza di rivelazione di una particella carica: {:0.2f} particelle al nanosecondo \n'.format(eff1*100, eff2))

        exp.particles_distr(ESP1, eff1, N)
        input("premi INVIO per continuare... \n")
        exp.time_distr(ESP1)
        time.sleep(5)
        input("premi INVIO per continuare... \n")

    plt.show(block=True)


if __name__ == '__main__':
    mwpc_sim()