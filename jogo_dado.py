### jogo_dado.py

## Quatro jogadores jogam um dado (valor 1 a 6); 
## O vencedor é aquele que tirar o maior valor


from random import randint

# Jogadores
j1 = {'Nome':"Jogador 1", 'Jogada':randint(1,6)}
j2 = {'Nome':"Jogador 2", 'Jogada':randint(1,6)}
j3 = {'Nome':"Jogador 3", 'Jogada':randint(1,6)}
j4 = {'Nome':"Jogador 4", 'Jogada':randint(1,6)}
jogadores = [j1, j2, j3, j4]    # lista de jogadores

# Lista das jogadas
jogadas = [0,0,0,0]

# ------------ Resultados -----------: #
print("Valores sorteados:")
print(f"O jogador {j1['Nome']} tirou {j1['Jogada']}")
print(f"O jogador {j2['Nome']} tirou {j2['Jogada']}")
print(f"O jogador {j3['Nome']} tirou {j3['Jogada']}")
print(f"O jogador {j4['Nome']} tirou {j4['Jogada']}")
print()

# Ordenando as jogadas
for i in range(0,4):
    jogadas[i] = jogadores[i]['Jogada']

jogadas.sort(reverse=True)     # ordem decrescente

# Mostrando o ranking
print("Ranking dos jogadores:")
for i in range(0,4):
    if jogadores[i]['Jogada'] == jogadas[0]: # 1º lugar
        jogadores[i]['Pos'] = 1     # cria uma nova key para a posição
    else:
        if jogadores[i]['Jogada'] == jogadas[1]:    # 2º lugar
            jogadores[i]['Pos'] = 2    
        else:
            if jogadores[i]['Jogada'] == jogadas[2]:    # 3º lugar
                jogadores[i]['Pos'] = 3
            else:
                if jogadores[i]['Jogada'] == jogadas[3]:    # 4º lugar
                    jogadores[i]['Pos'] = 4

# Primeiro lugar
i = 0
while jogadores[i]['Pos'] != 1:
    i += 1  # incrementa 1
print(f"1º lugar: {jogadores[i]['Nome']} com {jogadores[i]['Jogada']}")

# Segundo lugar
i = 0
while jogadores[i]['Pos'] != 2:
    i += 1  # incrementa 1
print(f"2º lugar: {jogadores[i]['Nome']} com {jogadores[i]['Jogada']}")
    
# Terceiro lugar
i = 0
while jogadores[i]['Pos'] != 3:
    i += 1  # incrementa 1
print(f"3º lugar: {jogadores[i]['Nome']} com {jogadores[i]['Jogada']}")

# Quarto lugar
i = 0
while jogadores[i]['Pos'] != 4:
    i += 1  # incrementa 1
print(f"3º lugar: {jogadores[i]['Nome']} com {jogadores[i]['Jogada']}")