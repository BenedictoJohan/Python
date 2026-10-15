prenom = input("Entrez votre prénom: ")
age = int(input("Entrez votre âge: "))
taille = int(input("Entrez votre taille en cm: "))

age_5ans = age + 5
taille_metre = float(taille / 100)
print("Bonjour",prenom,"!")
print("Dans cinq ans vous aurez",age_5ans,"ans")
print("Votre taille est de",taille_metre,"m")