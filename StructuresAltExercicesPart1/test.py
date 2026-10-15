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