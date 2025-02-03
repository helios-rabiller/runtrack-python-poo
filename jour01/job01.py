nombre1=4
nombre2=0
class Operation:
    # Construct 
    def __init__(self):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    # Méthode pour afficher l'objet de manière lisible
    def __str__(self):
        return f"Operation(nombre1={self.nombre1}, nombre2={self.nombre2})"

# Instanciation de la classe avec les valeurs par défaut
operation_instance = Operation()

if __name__ == "__main__":
    print(operation_instance)
