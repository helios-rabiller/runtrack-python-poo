class Personnage:
    # Constructeur
    def __init__(self, x, y):
        self.x = x  
        self.y = y  
    def gauche(self):
        self.x -= 1   
    def droite(self):
        self.x += 1   
    def haut(self):
        self.y -= 1   
    def bas(self):
        self.y += 1  

    def position(self):
        return (self.x, self.y)

# Instance
personnage = Personnage(2, 2)

# Affichage
print("Position initiale :", personnage.position())

# Déplacement du personnage
personnage.gauche()  
print("Après déplacement à gauche :", personnage.position()) 

personnage.haut() 
print("Après déplacement en haut :", personnage.position())
