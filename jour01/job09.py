class Produit:
    def __init__(self, nom, prixHT, TVA=0.2):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)
    
    def afficher(self):
        return f"Produit: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA*100}%, Prix TTC: {self.CalculerPrixTTC():.2f}"
    
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom
    
    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix
    
    def getNom(self):
        return self.nom
    
    def getPrixHT(self):
        return self.prixHT
    
    def getTVA(self):
        return self.TVA

# Création de plusieurs produits
produit1 = Produit("Ordinateur", 1000)
produit2 = Produit("Smartphone", 500, 0.1)

# Affichage des informations des produits
print(produit1.afficher())
print(produit2.afficher())

# Modification des produits
produit1.modifierNom("PC Portable")
produit1.modifierPrix(1200)
produit2.modifierNom("Téléphone")
produit2.modifierPrix(550)

# Affichage après modification
print(produit1.afficher())
print(produit2.afficher())
