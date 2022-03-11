import os
import time
from tqdm import tqdm
# Importer toutes les fonctions du module database


# La fonction coeffAvg calculera la moyenne coefficiée
# Elle prendra en paramètre la note et le coefficient
# Elle retournera un réel alors pensez a caster le resultat de sortie
def coeffAvg(note: float, coeff: int) -> float:
    pass


# Cette fonction lira dans un fichier
# Tous les fichiers dont vous avez besoin sont dans le dossier files
# Cette fonction prendra le chemin du fichier et le nom du fichier
# Regarder la fonction scafoldServerData() pour voir comment la fonction openFile se construit
# Cette fonction lit le contenu du fichier
# Elle retourne un tableau contenant des tuples
# Chaque tuple comporte 5 valeurs
# Les tuples sont comme suit:
#   (
#       name,
#       subject.lower(),
#       float(note),
#       int(coeff),
#       float(coeffNote)
#   )
#       name: le nom de l'étudiant
#       subject: le nom de la matière passée en paramètre
#       note: la note de l'étudiant
#       coeff: le coefficient de la note
#       coeffNote: la note coefficiée
def openFile(filePath: str, subject: str) -> list:
    pass


# Cette fonction permet de récupérer les données des fichiers
# Et les mettre dans la base de données Sqlite3
# Mais cette fonction sera déclencher que depuis le client
# Ainsi cette fonction permettra de configurer la base de données du serveur
def scafoldServerData():
    # ....................
    iterator = 0
    processbar = tqdm([
        openFile('files/anglais.txt', 'anglais'),
        openFile('files/java.txt', 'java'),
        openFile('files/math.txt', 'math'),
        openFile('files/reseau.txt', 'reseau')
    ])
    incrementor = 1/len(processbar)
    print('Begin insertion in database...')
    for process in processbar:
        time.sleep(0.25)
        insertData(process)
        iterator += incrementor * 100
        processbar.set_description("Processing %s" % iterator)
    print('Finish insertion in database...')


# Cette fonction prendra le nom de l'etudiant
# Prenez le soin d'implémenter une fonction setMention
#   Cette fonction donnera la mention et le status d'admissibilité de l'étudiant
#   Donc elle retournera un tuple et ce tuple sera utilisé en index 0  pour la mention et en index 1 pour l'admissibilité
#   Si Moyenne < 10: (FAIBLE, NON)
#   Si Moyenne >=10 et <=11: (PASSABLE, OUI)
#   Si Moyenne >=12 et <=13 (ASSEZ-BIEN, OUI)
#   Si Moyenne >=14 et <=16: (BIEN, OUI)
#   Si Moyenne >=17 et <=18: (TRES-BIEN, OUI)
#   SI Moyenne >=19: (EXCELLENT, OUI)
# Et retournera un string qui se présentera comme suit:
# ---------------------------------- #
# name | coeff | coeffNote | MOYENNE #
# ---------------------------------- #
#   X  |   X   |     X     |    X    #
# Mention: EXCELLENT                 #
# Admis(e): OUI/NON                  #
# ---------------------------------- #
def getStudentVoucher(name: str):
    name = str(name).lower().capitalize()
    # ..............
    pass
