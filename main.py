from Model.Biblioteca import Biblioteca
from Model.Piano import Piano
from Model.Ripiano import Ripiano
from Model.Scaffale import Scaffale

biblioteca= Biblioteca()


biblioteca.aggiungiLibro(1,"SC3",2,"Guyton Hill","fisiologia")
biblioteca.aggiungiLibro(4,"SC3",2,"Guyton Hill","fisiologia")
biblioteca.aggiungiLibro(2,"SC3",2,"Stella Mia","Ali verdi")
biblioteca.contiene(1,"SC3",2)
biblioteca.contiene(1,"SC3",1)
biblioteca.getLibri(1,"SC3")
biblioteca.cercaLibro("Stella Mia","Ali verdi")




