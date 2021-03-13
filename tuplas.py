### tuplas.py

## Estudo e testes de tuplas

# Tuplas são imutáveis. Não é possível alterá-las.

lanche = ("Hambúrguer", "43", "mouse", "34")

# Testes
print(lanche)   # tupla inteira
print(lanche[2])    # apenas o elemento 2 da tupla
print(lanche[0:2])  # os elementos do 0 ao (2-1) da tupla
print(lanche[1:])   # elementos a partir do 1
print(lanche[-1])   # apenas o último elemento
print(lanche[-2])   # apenas o elemento nº 2 
print(lanche[-3])   # apenas o elemento nº 1
print(len(lanche))  # quantidade de elementos na tupla

# Uso de estruturas de repetição 
print("\n")
for c in lanche:
    print(c)

# Como as tuplas são imutáveis, seu uso é recomendado para armazenar constantes.
# Tuplas são sempre delimitadas por parênteses, enquanto listas são delimitadas por colchetes.

print(sorted(lanche))   # retorna uma lista com os elementos da tupla em ordem alfabética

# Concatenando tuplas
a = (2, 2, 4, 5)
b = (1, 3, 2)
c = a + b   
d = b + a   # diferente de c, pois a ordem é diferente!
print(c)
print(d)
print(d.count(8))   # quantos 8 tem na tupla
print(d.index(2))   # índice do 2
print(d.index(2, 4))    # índice do 2 a partir da posição 4

# apagando uma tupla
del(d)