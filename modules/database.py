import time
import sqlite3


# Permer d'établir la connection vers la base de données
# Si la base de données n'existe pas créer la dans la même arborescence
def connexion():
    con = sqlite3.connect('student.db')
    return con


# Permet de créer la table
# Si la table existe elle la supprime et la recré
# Si elle n'existe pas elle la crée
# Utiliser la requete de création de table
# Vous pouvez prendre appui sur les requêtes du fichier queries_helper.txt
def createTable():
    pass


# Cette fonction return la moyenne arithmétique d'un étudiant
# Prenez en compte les coefficients dans le calcul de la moyenne
# Dans l'écriture de la requête SQL utiliser les instructions SUM
# Et avec SUM appliquer directement la division
# Exemple: SUM(coeffNote) / SUM(coeff) AS MOYENNE
def getStudentMoy(name: str):
    pass


# Cette fonction insert dans le tableau
# Faites attention cette fois-ci au nombre de colonnes
# Faites attention à la requete SQL du fichier queries_helper.txt pour savoir combien de colonnes créer
# Prenez appui sur le fichier queries_helper.txt pour savoir combien de colonnes créer et quels sont leurs noms
def insertData(data: list):
    pass
