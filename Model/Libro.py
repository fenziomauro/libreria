class Libro:
    def __init__(self, autore, titolo,ripiano):
        self.autore = autore
        self.titolo = titolo
        self.ripiano=ripiano
    def __str__(self):
        return self.titolo + " ," + self.autore


