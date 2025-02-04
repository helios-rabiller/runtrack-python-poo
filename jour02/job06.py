class Commande:
    def __init__(self, num = 0):
        self.__num = num  
        self.__plats = {}  #  {"nom": prix}
        self.__status = "En cours"  #  ("En cours", "Terminée", "Annulée")
        self.__TVA = 0.2 
    
    # Getters
    def get_num(self):
        return self.__num
    
    def get_status(self):
        return self.__status
    
    def get_plats(self):
        return self.__plats
    
    def num_up(self):
        self.__num += 1
        return self.__num
    # Méthode pour ajouter un plat
    def ajouter_plat(self, nom_plat: str, prix: float):
        if self.__status == "En cours":
            self.__plats[nom_plat] = prix
        else:
            print("Impossible d'ajouter un plat : commande non modifiable.")
    
    # Méthode pour annuler une commande
    def annuler_commande(self):
        if self.__status == "En cours":
            self.__status = "Annulée"
            self.__plats.clear()
            self.num_up()
        else:
            print("La commande ne peut pas être annulée.")
    
    #  fin de commande
    def terminer_commande(self):
        if self.__status == "En cours":
            self.__status = "Terminée"
            self.num_up()
            return True
        else:
            print("La commande ne peut pas être terminée.")
            return False

    def __calculer_total_HT__(self):
        return sum(self.__plats.values())
    
    # Méthode pour calculer la TVA
    def calculer_TVA(self):
        return self.__calculer_total_HT__() * self.__TVA
    
    # Méthode pour afficher les détails de la commande
    def afficher_commande(self):
        print(f"Commande n°{self.__num} - Statut: {self.__status}")
        for plat, prix in self.__plats.items():
            print(f"- {plat}: {prix:.2f}€")
        print(f"Total HT: {self.__calculer_total_HT__():.2f}€")
        print(f"TVA ({self.__TVA * 100}%): {self.calculer_TVA():.2f}€")
        print(f"Total TTC: {(self.__calculer_total_HT__() + self.calculer_TVA()):.2f}€")
        self.__status = "En cours"
        return self.__status

commande = Commande()
commande.ajouter_plat("Flan",3.25)
commande.ajouter_plat("Cappucino",0.50)
commande.ajouter_plat("Croissant",1.30)
commande.annuler_commande()
commande.afficher_commande()
commande.ajouter_plat("Flamby",1.25)
commande.ajouter_plat("Cappucinotte",2.50)
commande.ajouter_plat("Croissantino",3.30)
commande.terminer_commande()
commande.afficher_commande()
