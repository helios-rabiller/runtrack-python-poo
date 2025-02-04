class Livre:
    def __init__(self,titre,auteur,pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
    
    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_pages(self):
        return self.__pages
    
    def set_auteur(self,new_auteur):
        self.__auteur = new_auteur
        print(f"L'auteur est : {self.__auteur}")
    def set_titre(self,new_titre):
        self.__titre = new_titre
        print(f"Le Titre est : {self.__titre}")
    def set_new(self,new_pages):
        try :
            if int(new_pages) >= 0:
                self.__pages = new_pages
                print(f"Il y a : {self.__pages}")
            else:
                print(" Error : mettez un nombre positif")
        except:
            print(" Error : mettez un nombre positif")

       
        
livre = Livre("Misérables","Gaspard",23)

livre.set_new(-2)
livre.set_auteur("da loca")
livre.set_titre("Vida")