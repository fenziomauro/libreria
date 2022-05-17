from Model.Libro import Libro
from Model.Ripiano import Ripiano


class Scaffale:
    def __init__(self):
        self.Ripiani = []
        for i in range(6):
            ripiano = Ripiano()
            self.Ripiani.append(ripiano)


    def aggiungiLibro(self,ripiano,autore,titolo,):
        if ripiano-1<=6:
           self.Ripiani[ripiano-1].aggiungiLibro(autore,titolo,ripiano)
        else:
            print("Ripiano inesistente")

