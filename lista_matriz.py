### lista_matriz.py

## Matriz 3x3

matriz = [[], [], []], [[], [], []], [[], [], []]
linha = list()
coluna = list()

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = input(f"Digite o elemento {i},{j}: ")

print('\nMatriz:')
for m in matriz:
    print(m)