class Point:
    # Constructeur
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Méthode pour afficher les coordonnées du point
    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    # Méthode pour afficher la coordonnée x
    def afficherX(self):
        print(f"La coordonnée x est : {self.x}")

    # Méthode pour afficher la coordonnée y
    def afficherY(self):
        print(f"La coordonnée y est : {self.y}")

    # Méthode pour changer la valeur de x
    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x
        print(f"La coordonnée x a été mise à jour à : {self.x}")

    # Méthode pour changer la valeur de y
    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y
        print(f"La coordonnée y a été mise à jour à : {self.y}")

# Instance
point = Point(3, 5)

#afficher les coordonnées
point.afficherLesPoints()  
point.afficherX()         
point.afficherY()         

# Changement des coordonnées
point.changerX(10)       
point.changerY(20)         

# coordonnée apres changements
point.afficherLesPoints()  