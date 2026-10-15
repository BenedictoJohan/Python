
''' CODE PIN '''

code_pin = input("Entrez votre code pin: ")

if code_pin == "4567":
    print("Correct")
else:
    print("incorrect")





''' SIGNE DU NOMBRE '''

nombre_entier = int(input("Entrez un nombre entier: "))

if nombre_entier > 0:
    print("Positif")
elif nombre_entier == 0:
    print("Nul")
elif nombre_entier < 0:
    print("Négatif")





''' PAIR OU IMPAIR '''

nombre_parité = int(input("Entrez un nombre entier: "))

if (nombre_parité % 2) == 0:
    print(nombre_parité,"est un nombre pair.")
else:
    print(nombre_parité,"est un nombre impair.")






''' ENFANT ADOLESCENT OU ADULTE '''

age = int(input("Entrez votre âge: "))

if age < 12:
    print("Vous êtes un enfant")
elif age >= 12 and age < 18:
    print("Vous êtes un adolescent")
else:
    print("Vous êtes un adulte")






''' PERTE OU PROFIT '''

prix_fabrication = float(input("Entrez le prix de fabrication du produit: "))
prix_vente = float(input("Entrez le prix de vente du produit: "))

perte_profit = (prix_vente - prix_fabrication)

if perte_profit > 0:
    print("Profit")
else:
    print("Perte")






''' TROUVER LE MAXIMUM '''

nombre_un = float(input("Entrez un premier nombre: "))
nombre_deux = float(input("Entrez un deuxième nombre: "))
nombre_trois = float(input("Entrez un troisième nombre: "))

nombre_list = [nombre_un, nombre_deux, nombre_trois]

if max(nombre_list) == nombre_un:
    print("Le maximum est le premier nombre",nombre_un)
elif max(nombre_list) == nombre_deux:
    print("Le maximum est le second nombre",nombre_deux)
else:
    print("Le maximum est le troisième nombre",nombre_trois)







''' EXERCICE DU TRIANGLE RECTANGLE '''

print("Entrez les longueurs dans un ordre croissant s'il vous plaît")

cote_un = float(input("Entrez la longueur du premier coté: "))
cote_deux = float(input("Entrez la longueur du deuxième coté: "))
cote_trois = float(input("Entrez la longueur du troisième coté: "))

cote_list = [cote_un, cote_deux, cote_trois] # On créer une liste avec la valuers des longueurs pour faciliter les prochains calculs.

if (cote_trois**2) == (cote_un**2) + (cote_deux**2): # Cette fonction if vérifie si le triangle est rectangle.
    triangle = True
else:
    triangle = False

if cote_trois != max(cote_list):
    print("Les longueurs des côtés n’ont pas été saisies dans l’ordre croissant.") # Ici on empêche le programme de continuer si les valeurs n'ont pas été entrées dans un ordre croissant.
else:
    if triangle == True:
        print("Le triangle est rectangle")
    elif triangle == False:
        print("Le triangle n'est pas rectangle")






        ''' PARTIE 2 '''



    '''ANNÉE BISSEXTILE'''

annee_bis = int(input("Entrez une année: "))

if (annee_bis % 4) == 0 and (annee_bis % 100) != 0:
    print("Année bissextile")
else:
    print("Année non bissextile")






    ''' SOCIÉTÉ DE TRANSPORT '''

prix_de_base = 10

age_visiteur = int(input("Entrez votre âge: "))

if age_visiteur <= 5:
    print("Le prix du transport est de 0 euros")
elif age_visiteur < 16:
    prix_5_16 = prix_de_base / 2
    print("Le prix du transport est de",prix_5_16,"euros")
elif age_visiteur <= 21:
    prix_16_21 = prix_de_base * 0.60
    print("Le prix du transport est de",prix_16_21,"euros")
elif age_visiteur < 51:
    print("Le prix du transport est de",prix_de_base,"euros")
elif age_visiteur >= 51:
    prix_51 = prix_de_base * 0.90
    print("Le prix du transport est de",prix_51,"euros")





    ''' VOYAGE SCOLAIRE '''

duree_voyage = int(input("Entrez la durée du voyage en jour: "))
nombre_eleves = int(input("Entrez le nombre d'élèves: "))

prix_nourriture = 3.50 * nombre_eleves

if nombre_eleves < 20:
    prix_herberg = nombre_eleves * 4.20
elif nombre_eleves <=35:
    prix_herberg = nombre_eleves * 3.80
elif nombre_eleves >35:
    prix_herberg = nombre_eleves * 4.00

if nombre_eleves > 25:
    prix_transport = nombre_eleves * 100
else:
    prix_transport = nombre_eleves * 110

prix_total_voyage = prix_transport + prix_herberg + prix_nourriture

print("Le prix du voyage revient à",prix_total_voyage,"euros")




''' VINCI LOCATION '''

citadine = 80
berline = 100
sportive = 130

essance = 1.93
diesel = 1.89

type_vehicule = input("Entrez le type de véhicule que vous souhaitez louer parmis les suivants (Citadine Berline Sportive): ")
carburant = input("Entrez le type de carburant utilisé par le véhicule (Essance ou Diesel): ")
duree_location = int(input("Entrez la durée de location en jour: "))
distance_km = int(input("Entrez la distance que vous allez parcourir en km: "))

offre_commerciale = input("Souhaitez vous souscrire à l'offre commerciale pour 30 euros sachant que vous bénificirez d'une réduction de 10 pourcents sur votre location (Répondez par oui ou non): ")

if carburant == "Diesel":
    prix_carburant = distance_km * diesel
else:
    prix_carburant = distance_km * essance


if type_vehicule == "Citadine":
    prix_total_loc = prix_carburant + citadine
elif type_vehicule == "Berline":
    prix_total_loc = prix_carburant + berline
elif type_vehicule == "Sportive":
    prix_total_loc = prix_carburant + sportive


if offre_commerciale == "oui":
    int(prix_total_loc) == (prix_total_loc * 0.90)

print("Le prix total de la location est de",prix_total_loc)




''' NATATION '''

nombre_seances = int(input("Entrez le nombre de séances que vous allez faire dans l'année: "))

tarifA = 10.50
tarifB = 15.50
prix_abonnement = 145

avantageux = nombre_seances * (tarifB - tarifA)

total_A = tarifA * nombre_seances
total_B = tarifB * nombre_seances

montrer_prix = input("Voulez vous voir le prix que vous aurais coûté chauqe tarif ? (yes or no): ")

if avantageux > prix_abonnement:
    print("Le tarifA est plus avantageux")
else:
    print("Le tarifB est plus avantageux")

if montrer_prix == "yes":
    print("TarifA:",total_A)
    print("TarifB:",total_B)




''' VOYELLE CONSONNE OU CARACTÈRE SPÉCIAL '''

list_consonne = ["b","B","c","C","d","D","f","F","g","G","h","H","j","J","k","K","l","L","m","M","n","N","p","P","q","Q","r","R","s","S","t","T","v","V","w","W","x","X","z","Z"]
list_voyelle = ["a","A","e","E","i","I","o","O","u","U","y","Y"]

symbole = input("Entrez un caractère: ")

if symbole in list_consonne:
    print(symbole,": est une consonne")
elif symbole in list_voyelle:
    print(symbole, ": est une voyelle")
else:
    print(symbole, ": est un caractère spécial")





''' FACTURE '''

prix_ht = float(input("Entrez le prix de l'objet hors taxe: "))

prix_ttc = prix_ht * 1.196

if prix_ttc < 1000:
    prix_final = prix_ttc
elif prix_ttc >=1000 and prix_ttc < 2000:
    prix_final = prix_ttc * 0.99
elif prix_ttc >= 2000 and prix_ttc < 5000:
    prix_final = prix_ttc * 0.97
elif prix_ttc >= 5000:
    prix_final = prix_ttc * 0.95

remise = prix_ttc - prix_final

prix_ht, prix_ttc, prix_final, remise = round(prix_ht, 2), round(prix_ttc, 2), round(prix_final, 2), round(remise, 2)

print("Prix HT:",prix_ht)
print("Prix TTC:",prix_ttc)
print("Remise:",remise)
print("Prix net à payer:",prix_final)




''' CALCULATRICE '''

premier_nombre = float(input("Entrez le premier nombre: "))
operation = input("Entrez l'opération (addition, soustraction, division, multiplication): ")
deuxieme_nombre = float(input("Entrez le deuxième nombre: "))

if operation.casefold() == "addition":
    resultat = premier_nombre + deuxieme_nombre
    print(premier_nombre,"+",deuxieme_nombre,"=",resultat)

elif operation.casefold() == "soustraction":
    resultat = premier_nombre - deuxieme_nombre
    print(premier_nombre,"-",deuxieme_nombre,"=",resultat)

elif operation.casefold() == "division":
    if deuxieme_nombre == 0:
        print("Division par 0 !")
    else:
        resultat = premier_nombre / deuxieme_nombre
        print(premier_nombre,"/",deuxieme_nombre,"=",resultat)

elif operation.casefold() == "multiplication":
    resultat = premier_nombre * deuxieme_nombre
    print(premier_nombre,"*",deuxieme_nombre,"=",resultat)

else:
    print("Opération non valide")



''' IMPÔTS '''

revenu = float(input("Entrez votre revenu: "))

if revenu <= 10000:
    impots = 0

elif revenu <= 25000:
    tranche = revenu - 10000
    impots = tranche * 0.10

elif revenu <= 50000:
    tranche = revenu - 25000
    impots = tranche * 0.15

elif revenu > 50000:
    tranche = revenu - 50000
    impots = tranche * 0.20

print("L'impôt à payer est de", impots)





''' NATURE D'UN TRIANGLE'''


cote_triangle1 = float(input("Entrez la longeur du premier coté du triangle: "))
cote_triangle2 = float(input("Entrez la longeur du deuxième coté du triangle: "))
cote_triangle3 = float(input("Entrez la longeur du troisième coté du triangle: "))


list_triangle = [cote_triangle1, cote_triangle2, cote_triangle3]

list_triangle.sort()

if list_triangle[2] > (list_triangle[0]+list_triangle[1]):
    print("Les longueurs fournies ne forment pas un triangle valide.")

elif cote_triangle1 == cote_triangle2 and cote_triangle2 == cote_triangle3:
    print("C'est un triangle équilatéral.")

elif cote_triangle1 == cote_triangle2 or cote_triangle2 == cote_triangle3 or cote_triangle1 == cote_triangle3:
    print("C'est un triangle isocèle.")

else:
    print("C'est un triangle scalène.")



''' SALAIRE NET '''


salaire_brut = float(input("Entrez votre salaire Net: "))
ventes_realisees = int(input("Entrez le nombre de ventes que vous avez réalisées: "))
anciennete = int(input("Depuis combien d'années travaillée vous ici: "))
cadre = input("Êtes vous un cadre ? (oui/non): ")

pourcentage_prime = 0
pourcentage_taxe = 0

print("Salaire de base :",salaire_brut)

if ventes_realisees > 100:
    pourcentage_prime += 10
    prime_ventes = salaire_brut * 0.10
    print("La prime de vente est de",prime_ventes)

if anciennete >= 5 and anciennete <= 10:
    pourcentage_prime += 5
    prime_anciennete = salaire_brut * 0.05
    print("La prime d'ancienneté est de",prime_anciennete)
else:
    pourcentage_prime += 10

if cadre.casefold() == "oui":
    pourcentage_prime += 5
    prime_cadre = salaire_brut * 0.05
    print("La prime de cadre est de",prime_cadre)

salaire_brut_prime = salaire_brut * (pourcentage_prime/100 + 1)

print("Salaire brut avec primes:",salaire_brut_prime)

if salaire_brut_prime < 2000:
    pourcentage_taxe += 20
elif salaire_brut_prime <= 5000:
    pourcentage_taxe += 30
elif salaire_brut_prime > 5000:
    pourcentage_taxe += 40

salaire_net = salaire_brut_prime - (salaire_brut_prime * (pourcentage_taxe/100))

montant_taxes = salaire_brut_prime - salaire_net

print("Montant des taxes:",montant_taxes)
print("Salaire Net:",salaire_net)



''' MOT DE PASSE '''

