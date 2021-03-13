### pares_impares.py

## O programa solicita 7 números ao usuário. Os números são cadastrados
## numa única lista, separando-se os pares dos ímpares. Ao final, 
## os valores são mostrados de acordo com a separação feita e 
## em ordem crescente.

numeros = list()
pares = list()
impares = list()


for i in range(0,7):
    numeros.append(int(input("Digite um número: ")))

for n in numeros:
    if n%2 == 0:    # se o número for par
        pares.append(n)
    else:
        impares.append(n)

# Resultado:
print('\n')
print(f"Pares: {sorted(pares)}")
print(f"Ímpares: {sorted(impares)}")