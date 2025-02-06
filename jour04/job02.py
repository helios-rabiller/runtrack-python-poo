class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print(f"J’ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")

# Instanciation d'une Personne et d'un Eleve
personne = Personne()
eleve = Eleve()

# L'élève dit bonjour et va en cours
eleve.bonjour()
eleve.allerEnCours()

# Modifier l'âge de l'élève à 15 ans
eleve.modifierAge(15)
eleve.afficherAge()

# Instanciation d'un Professeur de 40 ans
professeur = Professeur(age=40)

# Le professeur dit bonjour et commence son cours
professeur.bonjour()
professeur.enseigner()
