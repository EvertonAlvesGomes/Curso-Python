### lista80.py

## O usuário digita 5 números e programa, sem usar a função sort(),
## Organiza a lista em ordem crescente.

mylist = list()
pos = 1

for num in range(0, 5):
    num = int(input('Digite um número: '))
    if len(mylist) > 0:
        if num > max(mylist):
            # mylist[len(mylist)-1)] = num   
            mylist.insert(len(mylist), num)   # adiciona o elemento ao final da lista
            print('Elemento adicionado ao final da lista')
        else:
            if num < min(mylist):
                mylist.insert(0, num)
                print("Elemento adicionado no início da lista")
            else:
                mylist.insert(pos, num)
                print(f"Elemento adicionado na posição {pos}")
                pos += 1
    else:
        mylist.append(num)

print(f'\nLista: {mylist}')
