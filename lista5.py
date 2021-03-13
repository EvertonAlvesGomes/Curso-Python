### lista5.py

# Leitura de 5 números e armazenamento em lista

mylist = list()

for n in range(0,5):
    n = int(input("Digite um número: "))
    if n not in mylist: # número será adicionado somente se não estiver na lista
        mylist.append(n)

# Resultados
print(f"\nLista: {mylist}")
print(f'Maior: {max(mylist)}')
print(f'Menor: {min(mylist)}')