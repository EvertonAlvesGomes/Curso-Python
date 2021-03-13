### funcoes.py

## Estudo sobre funções

# Funções são declaradas/definidas por:
# def <nome da funcao>(<args>):
    # conteudo

# Recomenda-se deixar um espaço de duas linhas entre duas definições de funções

# Recomenda-se separar as definições das funções e o restante do programa.
# O restante do programa é comumente chamado programa principal

import fun_import       # importação de arquivo com funções

def mostraLinha(quant):
    print("-"*quant)


def titulo(titulo, quant_linhas):
    mostraLinha(quant_linhas)
    print(titulo)
    mostraLinha(quant_linhas)

# -------- USO DAS FUNÇÕES ----------- #
# mostraLinha(5)
# msg = "Mensagem na Tela"
# titulo(msg, len(msg))

# a = int(input("Valor de a: "))
# b = int(input("Valor de b: "))
# c = fun_import.soma(a,b)
# print(f"Soma: {c}")

fun_import.contador(5, 3, 3, 6, 4)

lista = [3, 2, 5, 7]
print(f"Lista original: {lista}")
print(f"Lista dobrada: {fun_import.dobra_lista(lista)}")
print(f"Soma: {fun_import.soma(lista)}")