# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
import matplotlib.pyplot as plt
def Organisation_Donnees_Capteurs(Donnees):
    x= np.zeros(len(Donnees))
    y1= np.zeros(len(Donnees))
    y2= np.zeros(len(Donnees))
    z=0
    for i in range(0,len(Donnees)):
        z += 1
        x[z - 1] = Donnees[i][0]
        y1[z - 1] = Donnees[i][1]
        y2[z - 1] = Donnees[i][2]
    return(x,y1,y2)

Donne1=np.loadtxt('test8.csv', delimiter=';')
Donnes=Organisation_Donnees_Capteurs(Donne1)
plt.plot(Donnes[0],Donnes[1])
