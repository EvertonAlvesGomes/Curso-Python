### area.py

## Calcular área de um terreno


# Funções

def area(larg, prof):    # recebe largura e profundidade
    return larg*prof


largura = float(input("Largura (m): "))
profundidade = float(input("Profundidade (m): "))

print(f"A área do terreno {largura}x{profundidade} é de {area(largura, profundidade)} m².")