class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut
    
    def marquerCommeFinie(self):
        self.statut = "Terminée"
    
    def __str__(self):
        return f"{self.titre} - {self.description} [{self.statut}]"

class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, tache):
        self.taches.append(tache)
    
    def supprimerTache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]
    
    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.marquerCommeFinie()
    
    def afficherListe(self):
        return [str(tache) for tache in self.taches]
    
    def filterListe(self, statut):
        return [str(tache) for tache in self.taches if tache.statut == statut]

# Initialisation
tache1 = Tache(f"Faire les courses "," Acheter du lait et du pain\n")
tache2 = Tache(f"Rendre le rapport "," Finaliser et envoyer le rapport de projet\n")
tache3 = Tache("Aller à la salle de sport "," Séance de musculation à 18h\n")

liste = ListeDeTaches()

# Ajout des tâches
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

liste.supprimerTache("Rendre le rapport")
liste.marquerCommeFinie("Faire les courses")

# Affichage de toutes les tâches
print("Toutes les tâches:")
print(liste.afficherListe())

# Affichage des tâches à faire
print("Tâches à faire:")
print(liste.filterListe("À faire"))
