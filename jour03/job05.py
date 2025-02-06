import random

class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.vie = 100
        self.cooldown_special = 0

    def attaquer(self, adversaire):
        degats = random.randint(8, 12)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

    def defendre(self):
        print(f"{self.nom} se défend et réduit les dégâts reçus au prochain tour.")
        return 0.5

    def special(self, adversaire):
        if self.cooldown_special == 0:
            degats = random.randint(15, 25)
            adversaire.vie -= degats
            self.cooldown_special = 3
            print(f"{self.nom} utilise une attaque spéciale et inflige {degats} points de dégâts à {adversaire.nom}.")
        else:
            print(f"{self.nom} ne peut pas encore utiliser son attaque spéciale (cooldown: {self.cooldown_special} tours).")

    def est_vivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.tour = 0

    def lancerJeu(self):
        joueur1 = Personnage("Boxeur 1")
        joueur2 = Personnage("Boxeur 2")
        
        print(f"Début du combat : {joueur1.nom} contre {joueur2.nom}")
        
        while joueur1.est_vivant() and joueur2.est_vivant():
            self.tour += 1
            print(f"\n--- Tour {self.tour} ---")
            
            self.tour_de_combat(joueur1, joueur2)
            if joueur2.est_vivant():
                self.tour_de_combat(joueur2, joueur1)
            
            joueur1.cooldown_special = max(0, joueur1.cooldown_special - 1)
            joueur2.cooldown_special = max(0, joueur2.cooldown_special - 1)
        
        self.verifierGagnant(joueur1, joueur2)
    
    def tour_de_combat(self, attaquant, defenseur):
        action = input(f"{attaquant.nom}, choisissez une action (attaque, défense, spécial) : ").strip().lower()
        reduction = 1.0

        if action == "attaque":
            attaquant.attaquer(defenseur)
        elif action == "défense" or action == "defense":
            reduction = attaquant.defendre()
        elif action == "spécial" or action == "special":
            attaquant.special(defenseur)
        else:
            print("Action invalide, attaque par défaut.")
            attaquant.attaquer(defenseur)

        defenseur.vie *= reduction
        print(f"{attaquant.nom} : {attaquant.vie} PV | {defenseur.nom} : {defenseur.vie} PV")
    
    def verifierGagnant(self, joueur1, joueur2):
        if joueur1.est_vivant():
            print(f"{joueur1.nom} a remporté le combat !")
        else:
            print(f"{joueur2.nom} a remporté le combat !")

# Lancer le jeu
jeu = Jeu()
jeu.lancerJeu()
