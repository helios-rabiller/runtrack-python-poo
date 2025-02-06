class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts += 1
        print(f"{self.nom} a marqué un but !")

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        print(f"{self.nom} a effectué une passe décisive !")

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        print(f"{self.nom} a reçu un carton jaune.")

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        print(f"{self.nom} a reçu un carton rouge.")

    def afficherStatistiques(self):
        print(f"Joueur: {self.nom} ({self.position}, #{self.numero})")
        print(f"  Buts: {self.buts}")
        print(f"  Passes décisives: {self.passes_decisives}")
        print(f"  Cartons jaunes: {self.cartons_jaunes}")
        print(f"  Cartons rouges: {self.cartons_rouges}")
        print("-" * 30)

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
        print(f"{joueur.nom} a été ajouté à l'équipe {self.nom}.")

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom, action):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                return
        print(f"Joueur {nom} non trouvé dans l'équipe {self.nom}.")

# Initialisations
equipe1 = Equipe("FC Lions")
equipe2 = Equipe("Tigres Noirs")

# Création des joueurs
joueur1 = Joueur("Paul Dupont", 9, "Attaquant")
joueur2 = Joueur("Jean Martin", 10, "Milieu")
joueur3 = Joueur("Lucas Henry", 5, "Défenseur")
joueur4 = Joueur("David Leroy", 7, "Attaquant")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)

# Affichage 
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation d'un match
equipe1.mettreAJourStatistiquesJoueur("Paul Dupont", "but")
equipe2.mettreAJourStatistiquesJoueur("David Leroy", "but")
equipe1.mettreAJourStatistiquesJoueur("Jean Martin", "passe")
equipe2.mettreAJourStatistiquesJoueur("Lucas Henry", "jaune")
equipe1.mettreAJourStatistiquesJoueur("Paul Dupont", "rouge")


equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
