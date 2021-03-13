### jogador_futebol.py

jogador = dict()
gols = list()

jogador = {'nome': '', 'gols': gols, 'n_partidas': 0}
jogador['nome'] = str(input("Nome do jogador: "))
jogador['n_partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for n in range(0,jogador['n_partidas']):
    gols.append(int(input(f"Quantos gols marcados na partida {n}? ")))

# ----- Resultados ----- #
print()
print("Dados do jogador:")
print(jogador)
print("-="*35)
print(f"Nome do jogador: {jogador['nome']}")
print(f"Gols marcados: {jogador['gols']}")
print(f"Total de partidas: {jogador['n_partidas']}")
print("-="*30)
print(f"O jogador {jogador['nome']} jogou {jogador['n_partidas']} partidas.")
for i in range(0,jogador['n_partidas']):
    print(f"    Na partida {i}, {jogador['nome']} fez {jogador['gols'][i]} gols.")
print(f"Total de gols marcados: {sum(jogador['gols'])}")