""" VAZNA NAPOMENA: DA SE ZAUSTAVI PROGRAM KORISTITI CTRL C """
""" u dan noc sekciji fali ti ono brisanje od pola pa nadole """


""" Mesto za importovanje """
import numpy as np
import time

#-----------------------------------------------


""" Tabla koja je MxN velicine matrica """

M = 10     # dimenzije table ovo je horizontalno ( [0,0,0,0,0,0] )
N = 10     # dimenzije table ovo je vertikalno


tabla = np.zeros((M,N), np.int8) # sama tabla je sve nule velicine MxN

# tabla[x][y] -> x je horizontalno (M), a y je vertikalno (N)

#-----------------------------------------------


""" Dan - Noc """

""" Krece od jedne tacke na sredini desne strane i onda sve tacke oko sebe pretvori u 1 pa u sledecem ciklusu opet to uradi sve dok ne dodje do M velicine
    gde se onda sa ivica oduzimaju po jedna tacka tj samo obrnuti proces od dolaska """

sat = 1 # ovo ce mi biti brojac

while sat == sat:  # dan noc ide zauvek ili dok ja ne kazem

    """ kada je sat < 2N onda je i dalje dan, a taj jos jedan N je noc. Dok je < 2N ide sunce, kada je 2N < sat < 3N onda je mrak """
    if sat == 3*N:
        sat = 1

#==================

    """" u prvom satu samo na sredini table imamo truncicu sunca """
    """ RADI SAMO AKO IZ COSKA KRECE A TO NECU, HOCU DA MOZE DA KRENE ODAKLE HOCE, A PROBLEM JE STO ONE KOJE
        OSVETLI ONDA GLEDA OPET KAO DA NISU NIKAD OSVETLJENI, DA VIDIS STA MISLIM SAMO PROMENI PRVI IDX U M/2"""
    if sat == 1:
        tabla[-1][-1] = 1

#==================

    """ proverava gde je sve osvetljeno i sve oko njega pretvara u osvetljeno (bez dijagonala jer je sunce kruzno) svakim prolaskom sata
        moze se optimizovati tako sto stavim set svih tacaka koje je proverio da ne proverav sada (ali to ako me ne mrzi, nije zahtevan prog)"""


    """ ovaj deo ide kroz celu matricu pod uslovom da nije prvi sat i da je dan """
    if sat != 1 and sat < 2*N:

        for i in range(N):
            for j in range(M):

                """ ovaj deo kaze da ako je osvetljeno sve oko njega postaje osvetljeno """
                if tabla[i][j] == 1:
                    #print('nasao na', i, j)
                    #print(tabla, '\n')
                    #time.sleep(2)
                    """ moram da vidim da li ovi indeksi postoje ako ne postoje onda samo ne pisemo 1 tu
                        verovatno ima neki lepsi nacin da se to sredi ali nmg sad da razmisljam"""
                    try:
                        tabla[i+1][j] = 1
                    except IndexError:
                        pass
                    try:
                        tabla[i-1][j] = 1
                    except IndexError:
                        pass
                    try:
                        tabla[i][j+1] = 1
                    except IndexError:
                        pass
                    try:
                        tabla[i][j-1] = 1
                    except IndexError:
                        pass



        """ ovo je samo da restartujem brojac kolone na nula """
        j = 0


    print(tabla, '\n')

    """ samo povecavam sat """
    sat += 1 # ti na kraj

    """ ovo je da program saceka 10 sec pre nego sto prodje sledeci sat """
    time.sleep(.5)
