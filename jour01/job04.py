class Personne:
    # Constructeur
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    # Méthode pour se présenter
    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}."

# Instance
personne1 = Personne("Doe", "Jhon")
personne2 = Personne("Dupont", "Jean")


if __name__ == "__main__":
    print(personne1.SePresenter()) 
    print(personne2.SePresenter())  