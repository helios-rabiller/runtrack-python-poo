class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self.__numero} - Titulaire: {self.__prenom} {self.__nom} - Solde: {self.__solde}€ - Découvert autorisé: {self.__decouvert}")
    
    def afficherSolde(self):
        print(f"Solde du compte n°{self.__numero} : {self.__solde}€")
    
    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant}€ effectué. Nouveau solde : {self.__solde}€")
        else:
            print("Le montant du versement doit être positif.")
    
    def retrait(self, montant):
        if montant > 0 and (self.__solde - montant >= 0 or self.__decouvert):
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.__solde}€")
        else:
            print("Fonds insuffisants pour effectuer ce retrait.")
    
    def agios(self):
        if self.__solde < 0:
            self.__solde -= 10  # Appliquer un agio de 10€
            print(f"Agios appliqués. Nouveau solde : {self.__solde}€")
    
    def virement(self, compte_destinataire, montant):
        if montant > 0 and (self.__solde - montant >= 0 or self.__decouvert):
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant}€ effectué vers le compte n°{compte_destinataire.__numero}")
        else:
            print("Fonds insuffisants pour effectuer ce virement.")

# Création des comptes
compte1 = CompteBancaire("12345", "Doe", "John", 500)
compte2 = CompteBancaire("67890", "Smith", "Jane", -50, decouvert=True)

# Affichage des comptes
compte1.afficher()
compte2.afficher()

compte1.versement(200)
compte1.retrait(100)
compte2.retrait(30)
compte2.agios()

# Virement de compte1 vers compte2
compte1.virement(compte2, 90)


compte1.afficherSolde()
compte2.afficherSolde()
compte1.afficher()
compte2.afficher()