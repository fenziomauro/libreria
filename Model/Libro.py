class Libro:
    def __init__(self, autore, titolo,ripiano):
        self.autore = autore
        self.titolo = titolo
        self.ripiano=ripiano

    def toString(self):
        stringalibro = str(self.autore, ", ", self.titolo)
        return stringalibro



