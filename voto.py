### voto.py
## Determine se o voto é obrigatório, facultativo ou negado
## a partir do ano de nascimento do usuário.

# --- IMPORTAÇÕES --- #
from datetime import datetime


# --- FUNÇÕES --- #
def voto(ano_nasc):
    global ano_atual
    if (ano_atual-ano_nasc >= 18) and (ano_atual-ano_nasc < 65):
        return "OBRIGATORIO"    # voto obrigatório
    else:
        if (ano_atual - ano_nasc >= 16) or (ano_atual-ano_nasc >= 65) :
            return "FACULTATIVO"    # voto facultativo
        else:
            return "NÃO VOTA"    # voto negado 


# --- PROGRAMA PRINCIPAL --- #
ano_atual = datetime.now().year
ano_nasc = int(input("Em que ano você nasceu? "))
print(f"Com {ano_atual-ano_nasc} anos o voto é {voto(ano_nasc)}")