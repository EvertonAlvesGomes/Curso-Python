### fun_import.py

## Funções a serem importadas por outros códigos

def soma(a, b):
    return a + b
    # sem o 'return', a função retorna 'None'


def soma(num):
    soma = 0
    for v in num:
        soma += v
    return soma

def contador(*num): # o asterisco indica que a função deve desempacotar o argumento 'num'
    # *num é similar aos ponteiros de C e C++
    # O asterisco permite passar quantos parâmetros quiser
    print(num)  # imprime uma tupla com os números de 'num'
    for valor in num:
        print(valor, end=' ')
    print(f"\nQuant. elementos: {len(num)}")
    print("Fim!")


def dobra_lista(lista):
    for i in range(0, len(lista)):
        lista[i] = lista[i]*2
    return lista