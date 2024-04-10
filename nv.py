import numpy as np
import matplotlib.pyplot as plt
import os
import glob

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
def charger_fichiers_csv(nom_dossier):
    # Construire le chemin absolu du dossier
    chemin_absolu = os.path.abspath(nom_dossier)
    # Vérifier si le chemin est un dossier
    if not os.path.isdir(chemin_absolu):
        print(f"{nom_dossier} n'est pas un dossier valide.")
        return None
    
    # Liste pour stocker les données des fichiers CSV
    donnees_csv = {}
    
    # Parcourir les fichiers dans le dossier
    for fichier in glob.glob(os.path.join(chemin_absolu, '*.csv')):
        # Obtenir le nom du fichier sans l'extension
        nom_fichier = os.path.splitext(os.path.basename(fichier))[0]
        
        # Charger les données du fichier CSV
        try:
            donnees = np.loadtxt(fichier, delimiter=';')
            donnees_csv[nom_fichier] = Organisation_Donnees_Capteurs(donnees)
        except Exception as e:
            print(f"Erreur lors du chargement du fichier {fichier}: {str(e)}")
    return donnees_csv


donnees = np.loadtxt('SignauxCapteursMSD/SignauxCapteursOXMSD/S_OX1.csv', delimiter=';')
donnees3 = np.loadtxt('SignauxCapteurMAD3Spires/SignauxCapteurOXMAD3Spires/S_OX1.csv', delimiter=';')
donnees5 = np.loadtxt('SignauxCapteurMAD5Spires/SignauxCapteurOXMAD5Spires/S_OX1.csv', delimiter=';')
valeurs = Organisation_Donnees_Capteurs(donnees)
valeurs3 = Organisation_Donnees_Capteurs(donnees3)
valeurs5 = Organisation_Donnees_Capteurs(donnees5)


# for name, valeurs in SignauxCapteursMSD.items():
#         if name in SignauxCapteurMAD3Spires:
#             if name in SignauxCapteurMAD5Spires:
# valeurs3Spires = SignauxCapteurMAD3Spires[name]
# valeurs5Spires = SignauxCapteurMAD5Spires[name]
plt.plot(valeurs[0], valeurs[1],label='1')
plt.plot(valeurs[0], valeurs[2],label='2')
plt.plot(valeurs[0], valeurs3[1],label='3')
plt.plot(valeurs[0], valeurs3[2],label='4')
# plt.plot(valeurs[0], valeurs5[1],label='5')
# plt.plot(valeurs[0], valeurs5[2],label='6')
plt.xlim(0,0.0400)
plt.legend()
                # plt.set_xlabel("Time (s)",fontsize=12)
                # plt.set_ylabel("Tension (V)",fontsize=12)
plt.show()