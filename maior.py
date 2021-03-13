### maior

def maior(num):
    return max(num)

sair = 'S'
valores = list()

print("Digite os valores para descobrir qual o maior. Pressione 'N' para sair.")
while sair == 'S':
    valores.append(int(input("Valor: ")))
    sair = str(input("Deseja continuar? [S/N] ")).upper()[0]

print(f"\nO maior número é {maior(valores)}")