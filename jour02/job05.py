class Voiture:
    def __init__(self,marque,modele,an,kilometrage,reservoir= 50,en_marche= False):
        self.__marque = marque
        self.__modele = modele
        self.__an = an
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def get_reservoir(self):
        return self.__reservoir
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_an(self):
        return self.__an
    def get_kilometrage(self):
        return self.__kilometrage
    def get_en_marche(self):
        return self.__en_marche
    def demarrer(self):
        self.__en_marche=True
        return self.__en_marche
    def arreter(self):
        self.__en_marche=False
        return self.__en_marche