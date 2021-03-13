### jogador_gols.py


def ficha(nome, gols=0):
    if nome == "":
        nome="<desconhecido>"
    if gols == "":
        gols = 0
    
    print(f"O jogador {nome} marcou {gols} gol(s) no campeonato.")

nome = str(input("Nome do jogador: "))
gols = input("Gols marcados: ")
ficha(nome, gols)