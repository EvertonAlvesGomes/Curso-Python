### funcoes2.py
## Explorando recursos de funções em Python

# help()  # função que permite entrar em modo de ajuda interativa
# help interativo do Python permite acessar documentação de funções,
# módulos e outros recursos da linguagem.

# Visualizando informações sobre uma função:
# help(print)     # entra direto no help interativo da função print
# print(print.__doc__)    # o atributo __doc__ representa a documentação da função


# docstring: documentação de função. Começa logo depois de def <funcao>
# As docstrings são separadas por dois trios de aspas duplas

def contador(i,f,p):
    """
    Faz uma contagem e mostra na tela os números.
    - (param) i = início da contagem
    - (param) f = fim da contagem
    - (param) p = passo
    - (return) sem retorno

    """
    for c in range(i,f,p):
        print(f"{c} ", end='')
    print("FIM!\n")



# Parâmetros opcionais:

def somar(a, b, c=0):
    """
    Soma três números.
    (param) a, b -> números a serem somados
    (param optional) c -> terceiro número a ser chamado
    (return) None

    """
    s = a + b + c
    print(f"A soma vale {s}")


# Escopo de variáveis:
def teste(b):
    """
    Função de teste de escopo

    """
    # As variáveis nesta função são válidas apenas para esta função.
    # Elas são chamadas variáveis locais, pois o escopo dessas variáveis
    # é dado apenas pela função teste(b).
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

    # fim da função

a = 5   # diferente do 'a' da função teste(b). Este 'a' é global, enquanto o da função é local.
# Qualquer alteração no 'a' acima não reflete em nada no 'a' da função teste(b) e vice-versa.
# Além disso, os dois 'a' têm endereços de memória diferentes.

# É possível utilizar uma variável como global dentro de funções. No escopo da função,
# utilize o comando 'global' antes da variável. Exemplo:

def teste2(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")


# ---------------------------------- #

# contador(1,100,4)
# help(contador)

somar(3,5,6)
somar(6,7)
h elp(somar)
