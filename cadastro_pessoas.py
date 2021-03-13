### cadastro_pessoas.py

## Cadastro de pessoas, estatística de quantas pessoas foram cadastradas,
## média de idade, lista com todas as mulheres, lista com todas as pessoas
## acima da média de idade

pessoas = list()    # lista das pessoas cadastradas
pessoa = dict()     # dicionário para cadastrar pessoas
mulheres = list()   # lista de mulheres cadastradas
pessoas_media = list()  # lista de pessoas com idade acima da média

print("-"*30)
print("     CADASTRO DE PESSOAS   ")
print("-"*30)

sn = 'S'
soma_idades = 0
media_idade = 0
quant_pessoas = 0
cont_f = 0  # contador de pessoas do sexo feminino
cont_avg = 0    # contador de pessoas com idade acima da média

# Cadastro de pessoas
while sn == 'S':
    pessoa['nome'] = str(input("Nome: "))
    pessoa['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
    pessoa['idade'] = int(input("Idade: "))
    pessoas.append(pessoa.copy())   # armazena na lista o cadastro da pessoa
    pessoa.clear() 
    sn = str(input("Deseja continuar? [S/N] ")).upper()[0]
    print()
    

# Resultados
print("="*30)
quant_pessoas = len(pessoas)
print(f"Foram cadastradas {quant_pessoas} pessoas.\n")     # quantidade de pessoas cadastradas

for p in pessoas:
    soma_idades += p['idade']
media_idade = soma_idades/quant_pessoas # calcula média de idade
print(f"Média de idade: {media_idade:.2f}\n")
# print("Média de idade: {}".format(media_idade.2f))

# Mulheres cadastradas
for p in pessoas:
    if p['sexo'] == 'F':
        cont_f += 1
        mulheres.append(p.copy())
    
    if p['idade'] > media_idade:
        cont_avg += 1
        pessoas_media.append(p.copy())

if cont_f == 0:
    print("Não foram cadastradas mulheres.")
else:
    if cont_f == 1:
        print(f"A mulher cadastrada foi {mulheres[0]['nome']}")
    else:
        print("As mulheres cadastradas foram: ", end='')
        for c in range(0,cont_f):
            if (cont_f-c) == 1 and c != 0:
                print(" e ", end='')
            else:
                if c > 0:
                    print(", ", end='')
            print(f"{mulheres[c]['nome']}", end='')
print()
# Pessoas com idade acima da média
print("\nPessoas com idade acima da média:")
for c in range(0,cont_avg):
    print(f"    {pessoas_media[c]['nome']} com {pessoas_media[c]['idade']} anos")