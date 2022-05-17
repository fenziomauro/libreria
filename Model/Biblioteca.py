from Model.Piano import Piano


class Biblioteca:
    def __init__(self):
        self.Piani = []
        for i in range(1,4):
            piano = Piano()
            self.Piani.append(piano)

    def aggiungiLibro(self, piano, scaffale, ripiano, autore, titolo):
       try:
           self.Piani[piano-1].aggiungiLibro(scaffale,ripiano,autore,titolo)
       except(IndexError):
           print("Piano inesistente")

