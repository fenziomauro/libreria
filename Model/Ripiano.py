from Model.Libro import Libro
class Ripiano:
    def __init__(self):
        self.Libri = []

    def aggiungiLibro(self, autore, titolo, ripiano):
            libro = Libro(autore, titolo, ripiano)
            if (len(self.Libri))<=9:
                self.Libri.append(libro)
                print("libro",titolo, "dell'autore", autore,"inserito in posizone",len(self.Libri))
            else:
                print("ripiano pieno selezionarne un altro")


















