""" Mesto za importovanje """
import numpy as np



""" Tabla koja je MxN velicine matrica """

M = 10     # dimenzije table ovo je horizontalno ( [0,0,0,0,0,0] )
N = 10     # dimenzije table ovo je vertikalno


tabla = np.zeros((M,N), np.int8) # sama tabla je sve nule velicine MxN

# tabla[x][y] -> x je horizontalno (M), a y je vertikalno (N)


""" Dan - Noc """

""" Krece od jedne tacke na sredini desne strane i onda sve tacke oko sebe pretvori u 1 pa u sledecem ciklusu opet to uradi sve dok ne dodje do M velicine
    gde se onda sa ivica oduzimaju po jedna tacka tj samo obrnuti proces od dolaska """

sat = 1 # ovo ce mi biti brojac

while sat != 2*N and sat != 0:  # sve dok brojac nije jednak dvema sirinama table tj dok ceo krug ne prodje kroz polje onda radi i nula jer je tada noc

    # u prvom satu samo na sredini table imamo truncicu sunca
    if sat == 1:
        tabla[int(M/2)][-1] = 1

    # OVDE SADA IDE ONO SRANJE GDE GLEDA OKO SEBE SVAKA TACKA I PRETVARA SVE OKO SEBE U JEDAN

    sat += 1 # ti na kraj
