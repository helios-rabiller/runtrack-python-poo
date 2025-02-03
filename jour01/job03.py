
class Operation:
    # Construct 
    def __init__(self,nombre1=12,nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.result= self.__addition__()
    
    def __addition__(self):
        return self.nombre2 + self.nombre1 
        

    # display
    def __str__(self):
        return f"Le nombre1 est {self.nombre1}\nLe nombre2 est {self.nombre2}\nL'addition des 2 donne {self.result}"
                

# instance of class
operation_instance = Operation()

if __name__ == "__main__":
    print(operation_instance)