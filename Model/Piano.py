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

    def contiene(self, scaffale, ripiano):
        self.Scaffali[scaffale].contiene(ripiano)

    def getLibri(self, scaffale):
        print("Lista libri nello scaffale", scaffale)
        rip=0
        for i in self.Scaffali[scaffale].Ripiani:
            rip=rip+1
            if len(i.Libri)==0:
                print("Nessun libro è presente sul ripiano",rip)
            else:
                print("Sul ripiano numero", rip, "sono presenti i seguenti libri:")
                for l in i.Libri:
                    print("AUTORE:",l.autore,"TITOLO:",l.titolo)










