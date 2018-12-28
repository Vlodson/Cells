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

    """ pomeranje celije: euklidska distanca do osvetljenog polja (da vidi da li moze da stigne do tamo a da ne umre)
        i gledanje da li je (x,y) osvetljenog vece ili manje od (x,y) celije onda +-1 na x y osi putem toga """

    def pomeraj(self, matrica_svet):


    """ smrt celije: ako celija nije na osvetljenom x sati umire (skontati kolko je x, za sada je 3 jer testiram) """

    def smrt(self, matrica_svet):
        counter = 0
        while self.pozicija()[0][1] == 1: # ovde ce biti i metoda pozicija koja kaze gde se trenutno nalazi celija i ako su trenutne koordinate celije 1 onda je celija ziva i ova metoda moze da ide
            if matrica_svet[self.pozicija()[0]][self.pozicija()[1]] == 0:
                counter += 1

            if counter == 3:
                self.pozicija()[0][1] == 0

    # def test(self,other):
    #     return self.pocetna_pozicija[0] + other.pocetna_pozicija[0], self.pocetna_pozicija[1] + other.pocetna_pozicija[1]


#------------------------------------

""" Mesto za inicijalizovanje objekata (u listu samo appendujem objekte)"""
# c1 = Celija(1,1)
# c2 = Celija(1,1)

""" fabrika celija """

celije = []
for i in range(3):
    celije.append(Celija(np.random.randint(0,9),np.random.randint(0,9))) # mozda se nekada poklope, trenutno je 3:41 mrzi me jako da ispisem jos 2 linije da se to sredi


""" svet celija (10x10) (u njemu i spavnujem celije)"""

svet_celija = np.zeros((10,10), np.int8)

""" Celija.pocetna_pozicija() ima dva elementa pa na tim mestima u svetu se nalazi celija koja je obelezena sa 2 """

def spavnovanje(matrica, celija):
    matrica[celija.pocetna_pozicija()[0]][celija.pocetna_pozicija()[1]] = 1

""" prolazim kroz listu celija i spawnjujem ih """
for i in range(len(celije)):
    spavnovanje(svet_celija, celije[i])

# svet[c1.pocetna_pozicija()[0]][c1.pocetna_pozicija()[1]] = 2

#------------------------------------

""" fizicki svet (u kom je dan noc ciklus i sve to) """

fizicki_svet = np.zeros((10,10), np.int8)
