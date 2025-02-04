class Student:
    def __init__(self,nom,prenom,nombre,credits=0,niveau=""):
        self.__nom = nom
        self.__prenom = prenom
        self.__nombre = nombre
        self.__credits = credits
        self.__niveau = niveau

    def get_credits(self):
        return self.__credits 
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_nombre(self):
        return self.__nombre
    def get_niveau(self):
        return self.__niveau
    
    def add_credits(self,new_credits):
        try :
            if int(new_credits) < 0:
                self.__credits= int(self.__credits + int(new_credits))
                if self.__credits >= 0 :
                    return self.__credits 
                else:
                    print("le crédits étudiant ne peut pas descendre en dessous de zéro")
                    self.__credits = 0
                    return self.__credits
            elif int(new_credits) >= 0:
                self.__credits = self.__credits + new_credits 
                return self.__credits
            else:
                print("Erreur : mettez un nombre")
        except ValueError:
            print("Il y a eu un probléme avec la classe")
    def __student_eval__(self):
        if self.__credits >=90:
            self.__niveau = "Excellent"
            return self.__niveau
        elif self.__credits >=80:
            self.__niveau = "Trés Bien"
            return self.__niveau
        elif self.__credits >=70:
            self.__niveau = "Bien"
            return self.__niveau
        elif self.__credits >=60:
            self.__niveau = "Passable"
            return self.__niveau
        else:               
            self.__niveau = "Insuffisant"
            return self.__niveau
        
    def student_info(self):
        self.__student_eval__()      
        print(f"Prenom = {self.__prenom}\nNom = {self.__nom}\nid = {self.__nombre}\nNiveau = {self.__niveau}")#\nCredits = {self.__credits}

        


       

etudiant = Student("Doe","Jhon",145)

etudiant.add_credits(10)
etudiant.student_info()
etudiant.add_credits(50)
etudiant.student_info()
etudiant.add_credits(10)
etudiant.student_info()
etudiant.add_credits(10)
etudiant.student_info()
etudiant.add_credits(10)
etudiant.student_info()
