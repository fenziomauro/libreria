from Model.Piano import Piano
from Model.Ripiano import Ripiano,Libro




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

    def contiene(self, piano, scaffale, ripiano):
        try:
            self.Piani[piano-1].contiene(scaffale,ripiano)
        except(IndexError):
            print("Piano inesistente")

    def getLibri(self, piano , scaffale):
        try:
            self.Piani[piano-1].getLibri(scaffale)
        except(IndexError):
            print("Piano inesistente")

    def cercaLibro(self, autore, titolo):
        pia=0
        for piano in self.Piani:
            pia=pia+1
            sca=0
            for scaffale in piano.Scaffali:
                sca=sca+1
                for ripiano in piano.Scaffali[scaffale].Ripiani:
                    for libro in ripiano.Libri:
                        if libro.titolo == titolo and libro.autore == autore:
                            print("Il libro dal titolo",libro.titolo,"dell'autore",libro.autore,"si trova al ripiano ", libro.ripiano,"dello scaffale sc",sca, "del piano",pia)



