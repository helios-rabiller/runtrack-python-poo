class Voiture:
    def __init__(self,marque,modele,an,kilometrage,reservoir= 5,en_marche= False):
        self.__marque = marque
        self.__modele = modele
        self.__an = an
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def __verifier_plein__(self):
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
    def set_marque(self,new_marque):
        self.__marque = new_marque
    def set_modele(self,new_modele):
        self.__modele = new_modele
    def set_an(self,new_an):
        self.__an = new_an
    def set_kilometrage(self,new_kilometrage):
        self.__kilometrage = new_kilometrage
    def set_en_marche(self,new_en_marche):
        self.__en_marche = new_en_marche
    def set_reservoir(self,new_reservoir):
        self.__reservoir = new_reservoir
    def demarrer(self):
        if self.__verifier_plein__() > 5:
            self.__en_marche=True
            print("demarre")
        else:
            self.arreter()
    def arreter(self):
        self.__en_marche=False
        print("arrêt")

voiture = Voiture("Citroen","C4 Picasso",4,134900)

voiture.demarrer()