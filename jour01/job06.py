class Animal:
    def __init__(self):
        self.age = 0  
        self.prenom = ""  

    
    def vieillir(self):
        self.age += 1  

   
    def nommer(self, nom):
        self.prenom = nom  

    def afficher_age(self):
        print(f"L'âge de l'animal est : {self.age}")

    def afficher_nom(self):
        print(f"Le nom de l'animal est : {self.prenom}")

# instance
animal = Animal()

# Affichage 
animal.afficher_age() 

# Faire vieillir 
animal.vieillir()

# update
animal.afficher_age() 

# Nom
animal.nommer("Rex")

# Affichage du nom
animal.afficher_nom()  