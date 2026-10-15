import math

# Exercice : Générer un mail de contact pour une recherche d'emploi

# Énoncé :
# Écrivez un script Python qui collecte des informations personnelles et professionnelles auprès de l'utilisateur,
# puis génère automatiquement un texte de mail de contact pour une candidature spontanée.
# Le mail doit inclure les informations suivantes :
# - Nom et prénom de l'utilisateur
# - Adresse email et numéro de téléphone
# - Poste recherché
# - Nom de l'entreprise cible

# Votre script doit :
# 1. Utiliser des f-strings pour générer le texte du mail.
# 2. Générer le même texte de mail sans utiliser les f-strings (en concaténant les chaînes de caractères).
# 3. Afficher les deux versions du mail généré.

# Script pour collecter des renseignements et générer un mail de contact pour une recherche d'emploi

# ----------------- Collecte des renseignements auprès de l'utilisateur------------------
nom = input("Entrez votre nom: ")
prenom = input("Entrez votre prénom: ")
adresse_mail = input("Entrez votre adresse mail: ")
numero_telephone = input("Entrez votre numéro de téléphone: ")
poste_recherche = input("Entrez le poste recherché: ")
entreprise_cible = input("Entrez le nom de l'entreprise ciblée: ")

# ----------------- Génération du texte du mail ------------------
adresse_mail_finale = (f"{nom}{prenom}{adresse_mail}{numero_telephone}{poste_recherche}{entreprise_cible}@gmail.com")

# ----------------- Affichage du mail généré ------------------
print(adresse_mail_finale)
# ----------------- Génération du texte du mail sans utiliser f-strings ------------------
adresse_mail_finale_sans_f = (nom + prenom + adresse_mail + numero_telephone + poste_recherche + entreprise_cible + "@gmail.com")
# ----------------- Affichage du mail généré ------------------
print(adresse_mail_finale_sans_f)


# ----------------- EXERCICES DE MANIPULATION DE NOMBRES -----------------
# Voici quelques exercices pour pratiquer la manipulation de nombres en Python.
# Complétez le code ci-dessous pour afficher la somme de deux nombres de deux façons différentes
# 1. En utilisant des f-strings
# 2. En concaténant les chaînes de caractères
x= 10
y= 5
z= f"La sommme de x + y est égale à {x+y}"
print(z)
print(str(x)+str(y))

print(z)
# Voici quelques exercices pour pratiquer la manipulation de chaînes de caractères en Python.
# Complétez le code ci-dessous pour afficher une phrase de deux façons différentes
phrase = "Bonjour, je m'appelle John."
print(phrase)
print(phrase[::-1])
print(phrase.upper())


# Voici quelques exercices pour pratiquer la manipulation de types de données en Python.
# afficher le type des différentes variables suivantes : x y z phrase email telephone


# Voici quelques exercices pour pratiquer la saisie utilisateur en Python.
# Complétez le code ci-dessous pour demander à l'utilisateur son nom et son âge,
nom_utilisateur = input("Entrez votre nom: ")
age_utilisateur = int(input("Entrez votre age: "))
age_utilisateur = int(age_utilisateur) # conversion de age_utilisateur en entier

# puis afficher un message personnalisé avec son nom et l'année de naissance.
annee_naissance = (2026 - age_utilisateur)

print("Bonjour",nom_utilisateur,"Vous êtes né en",annee_naissance)
# ----------------- EXERCICES DE MANIPULATION DE VARIABLES -----------------

# Exercice 1 : Échange de valeurs
# Échangez les valeurs de deux variables a et b, puis affichez-les.
a = 5
b = 10
a,b = (b,a) 


# Exercice 2 : Calcul de la moyenne
# Calculez la moyenne de trois nombres donnés.
a, b, c = 4, 8, 12
nombre_moyenne = [4,8,12]
moyenne = sum(nombre_moyenne) / len(nombre_moyenne)
print(moyenne)

# Exercice 3 : Conversion Celsius en Fahrenheit
# Convertissez une température donnée en Celsius en Fahrenheit.
celsius = 25
fahrenheit = (celsius * 9)/5 + 32
print(fahrenheit)


# Exercice 4 : Calcul de l'aire d'un rectangle
# Calculez l'aire d'un rectangle à partir de sa longueur et de sa largeur.
longueur = 7
largeur = 3
aire = (longueur * largeur)

# Exercice 5 : Calcul du périmètre d'un cercle
# Calculez le périmètre d'un cercle à partir de son rayon.
# attention : vous aurez besoin de la constante math.pi pour cela (import math)
rayon = 5
import math
aire_cercle = (math.pi * rayon**2)


# Exercice 6 : Inversion de chaîne
# Inversez une chaîne de caractères donnée.
chaine = "Python"
chaine_inversee = chaine[::-1]
print(chaine_inversee)

# Exercice 7 : Calcul de la puissance
# Calculez la puissance d'un nombre donné (exemple : 2^3).
# affichez le résultat
base = 2
exposant = 3
puissance = base ** exposant
print(puissance)


# Exercice 8 : Vérification de la présence d'un mot
# Vérifiez si un mot donné est présent dans une phrase.
# affichez le résultat (True/False)
# en deux lignes de code

phrase = "Bonjour tout le monde"
mot = "tout"
if "tout" in phrase:
    print(True)
else:
    print(False)


# Exercice 9 : Calcul du reste
# Calculez le reste de la division de deux nombres.
# affichez le résultat
dividende = 17
diviseur = 4
reste = 17 % diviseur
print(reste)


# Exercice 10 : Conversion en majuscules
# Convertissez une chaîne de caractères en majuscules.
chaine = "hello world"
chaine_maj = chaine.upper()
print(chaine_maj)

# Exercice 11 : Conversion en minuscules
# Convertissez une chaîne de caractères en minuscules.
chaine = "HELLO WORLD"
chaine_min = chaine.lower()
print(chaine_min)

# Exercice 12 : Remplacement de caractères
# Remplacez un mot dans une phrase par un autre mot.
phrase = "J'aime Python"
nouvelle_phrase = phrase.replace("Python", "moi")
print(nouvelle_phrase)

# Exercice 13 : Calcul du carré d'un nombre
# Calculez le carré d'un nombre donné.
# affichez le résultat
nombre = 6
carre = nombre ** 2
print(carre)

# Exercice 14 : Extraction de sous-chaîne
# Extrayez une sous-chaîne d'une chaîne donnée "progr".
# affichez le résultat
# attention : les indices commencent à 0 en Python
# par exemple, pour "Programmation", l'indice 0 correspond à "P"

chaine = "Programmation"
sous_chaine = chaine[0:5]
print(sous_chaine)

# Exercice 15 : Arrondi d'un nombre flottant
# Arrondissez un nombre flottant à l'entier le plus proche.
# affichez le résultat
nombre_flottant = 3.7
nombre_arrondi = round(nombre_flottant)
print(nombre_arrondi)

# Exercice 16 : Vérification de la longueur d'une chaîne
# Vérifiez si une chaîne contient plus de 10 caractères.
# affichez le résultat 
chaine = "Bonjour"
if len(chaine)>10:
    longueur_sup_10 = "True"
else:
    longueur_sup_10 = "False"
print(longueur_sup_10)




# Exercice 17 : Conversion d'une chaîne en liste
# Convertissez une chaîne de caractères en une liste de mots.
chaine = "Apprendre Python est amusant"
liste_mots = list(chaine)
print(liste_mots)

