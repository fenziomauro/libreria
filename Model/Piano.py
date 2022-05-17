from Model.Scaffale import Scaffale


class Piano:
    def __init__(self):
        self.Scaffali = {}
        for i in range(1,31):
            scaffale = Scaffale()
            self.Scaffali["SC" + str(i)] = scaffale

    def aggiungiLibro(self, scaffale, ripiano, autore, titolo):
        try:
            self.Scaffali[scaffale].aggiungiLibro(ripiano, autore, titolo)
        except(KeyError):
            print("Scaffale inesistente")





