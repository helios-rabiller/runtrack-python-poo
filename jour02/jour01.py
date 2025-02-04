class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longeur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def modifier_longueur(self,new_longeur):
        self.__longueur = new_longeur
        print(f"La longueur a été mise à jour à : {self.__longueur}")
    def modifier_largueur(self,new_largeur):
        self.__largueur = new_largeur
        print(f"La largueur a été mise à jour à : {self.__largueur}")

rectangle = Rectangle(2, 2)

rectangle.modifier_longueur(24)
