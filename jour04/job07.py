import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"
    
    def get_valeur(self):
        if self.valeur in ['Valet', 'Dame', 'Roi']:
            return 10
        elif self.valeur == 'As':
            return 11  # Par défaut, on attribue 11 à l'As, on ajustera après
        else:
            return int(self.valeur)

class Jeu:
    def __init__(self):
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        couleurs = ["Cœur", "Carreau", "Trèfle", "Pique"]
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(self.paquet)
    
    def tirer_carte(self):
        return self.paquet.pop() if self.paquet else None

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
    
    def recevoir_carte(self, carte):
        self.main.append(carte)
    
    def calculer_score(self):
        score = sum(carte.get_valeur() for carte in self.main)
        # Ajustement des As si nécessaire
        as_count = sum(1 for carte in self.main if carte.valeur == 'As')
        while score > 21 and as_count > 0:
            score -= 10  # Transformer un As de 11 en 1
            as_count -= 1
        return score
    
    def afficher_main(self):
        return ", ".join(str(carte) for carte in self.main)

class Croupier(Joueur):
    def __init__(self):
        super().__init__("Croupier")
    
    def jouer(self, jeu):
        while self.calculer_score() < 17:
            self.recevoir_carte(jeu.tirer_carte())

# Fonction principale pour jouer une partie
def jouer_blackjack():
    jeu = Jeu()
    joueur = Joueur("Joueur")
    croupier = Croupier()
    
    # Distribution initiale
    for _ in range(2):
        joueur.recevoir_carte(jeu.tirer_carte())
        croupier.recevoir_carte(jeu.tirer_carte())
    
    print(f"Main du joueur : {joueur.afficher_main()} (Score: {joueur.calculer_score()})")
    print(f"Carte visible du croupier : {croupier.main[0]}")
    
    # Tour du joueur
    while joueur.calculer_score() < 21:
        action = input("Voulez-vous prendre une carte ? (o/n) ")
        if action.lower() == 'o':
            joueur.recevoir_carte(jeu.tirer_carte())
            print(f"Nouvelle main : {joueur.afficher_main()} (Score: {joueur.calculer_score()})")
        else:
            break
    
    # Si le joueur dépasse 21, il perd immédiatement
    if joueur.calculer_score() > 21:
        print("Vous avez dépassé 21, vous perdez !")
        return
    
    # Tour du croupier
    croupier.jouer(jeu)
    print(f"Main du croupier : {croupier.afficher_main()} (Score: {croupier.calculer_score()})")
    
    # Détermination du gagnant
    score_joueur = joueur.calculer_score()
    score_croupier = croupier.calculer_score()
    
    if score_croupier > 21 or score_joueur > score_croupier:
        print("Félicitations, vous avez gagné !")
    elif score_joueur < score_croupier:
        print("Le croupier gagne !")
    else:
        print("Match nul !")

# Lancer le jeu
if __name__ == "__main__":
    jouer_blackjack()
