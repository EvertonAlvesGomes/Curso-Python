### pesoPessoas.py

## Cadastre pessoas pelo nome e peso em kg. Ao final,
## Retorne a quantidade de pessoas cadatradas, as mais pesadas e as mais leves

pessoas = list()
dado = list()   # lista temporária para armazenar dados de uma única pessoa
mais_leves = list()     # lista das pessoas mais leves
mais_pesadas = list()   # lista das pessoas mais pesadas

s_n = 'S'   # variável para continuar ou finalizar o cadastro
maior_peso = 0     # maior peso
menor_peso = 0     # menor peso

# Por padrão, a primeira pessoa cadastrada será a de maior peso.
cont = 0

print("\n******* CADASTRO DE PESSOAS *******\n")

while s_n == 'S':
    dado.append(input('Nome: '))
    dado.append(int(input('Peso: ')))
    cont += 1   # incrementa o contador de cadastros
    
    pessoas.append(dado[:])

    if cont == 1:   # se há apenas uma pessoa cadastrada, maior e menor peso são iguais
        maior_peso = pessoas[0][1]  
        menor_peso = pessoas[0][1]
    else :
        if dado[1] > maior_peso:
            maior_peso = dado[1]
        if dado[1] < menor_peso:    # atualiza o menor peso
            menor_peso = dado[1]

    dado.clear()

    s_n = str(input('Quer continuar? [S/N] ')).upper()
    while (s_n != 'S') and (s_n != 'N'):
        print('Comando inválido.')
        s_n = str(input('Quer continuar? [S/N] ')).upper()

    print("\n")


for p in pessoas:
    if p[1] == maior_peso:
        mais_pesadas.append(p[0])
    else :
        if p[1] == menor_peso:
            mais_leves.append(p[0])

# Resultados
print(f"Foram cadastradas {len(pessoas)} pessoas.")

print(f'Menor peso: {menor_peso} kg. Peso de {mais_leves}')
print(f'Maior peso: {maior_peso} kg. Peso de {mais_pesadas}')