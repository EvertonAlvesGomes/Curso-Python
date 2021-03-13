### sorteia_par.py
## Sorteio de 5 números e soma dos números que são pares dentre os sorteados

from random import randint

# ----------- FUNÇÕES ---------- #
def sorteia():
    sorteados_list = []
    for n in range(0, 5):
        sorteados_list.append(randint(0,100))
    return sorteados_list


def sorteiaPar():
    soma_pares = 0
    lista = sorteia()
    print("Números sorteados: {}".format(lista))
    for n in lista:
        if n%2 == 0:    # número par
            soma_pares += n
    print("Soma dos pares: {}".format(soma_pares))

# ------ PROGRAMA PRINCIPAL ---- #
sorteiaPar()