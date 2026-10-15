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