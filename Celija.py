""" prostor za importovanje """
import numpy as np

#------------------------------------

""" Celija moze da:
    celije cuvati ili u tuplu sa osvetljeno/tamno ili na komplet drugoj matrici (u ovom slucaju 0 -> nema celije -> 1 je celija u drugoj matrici)
    1) se pomera (ide ka svetlu)  (euklidska distanca)
    2) se razmnozava (kada ima dovoljno svetla tipa 3 sata je na svetlu)
    3) 'jede' (svetlo)
    4) ima poziciju (pocetnu X i tokom pomeranja)
    5) mozda da ima gene (nzm zasto) muskarci znaju zasto
    6) smrt (odredjen broj poteza) (skaliraj sa velicinom mape)
    ~ mozda napravim razlicite vrste celija ~ """


class Celija():

    """ da bi napravio objekat moras dati x i y pocetnu koordinatu za celiju """
    def __init__(self, pocetna_pozicija_x, pocetna_pozicija_y):
        self.pocetna_pozicija_y = pocetna_pozicija_x
        self.pocetna_pozicija_x = pocetna_pozicija_y

    """ pocetna pozicija celije, x i y ce da se menjaju """
    def pocetna_pozicija(self):
        # return print("pozicija:", self.pocetna_pozicija_x, self.pocetna_pozicija_y)
        return (self.pocetna_pozicija_x, self.pocetna_pozicija_y)

    # def test(self,other):
    #     return self.pocetna_pozicija[0] + other.pocetna_pozicija[0], self.pocetna_pozicija[1] + other.pocetna_pozicija[1]


#------------------------------------

""" Mesto za inicijalizovanje objekata (u listu samo appendujem objekte)"""
# c1 = Celija(1,1)
# c2 = Celija(1,1)

""" fabrika celija """
celije = []
for i in range(3):
    celije.append(Celija(i,i))


""" test svet (10x10) (u njemu i spavnujem celije)"""

svet = np.zeros((10,10), np.int8)

""" Celija.pocetna_pozicija() ima dva elementa pa na tim mestima u svetu se nalazi celija koja je obelezena sa 2 """
def spavnovanje(matrica, celija):
    matrica[celija.pocetna_pozicija()[0]][celija.pocetna_pozicija()[1]] = 2

""" prolazim kroz listu celija i spawnjujem ih """
for i in range(len(celije)):
    spavnovanje(svet, celije[i])

# svet[c1.pocetna_pozicija()[0]][c1.pocetna_pozicija()[1]] = 2

#------------------------------------
