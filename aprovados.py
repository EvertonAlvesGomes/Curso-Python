### aprovados.py

## Leia o nome e a média de um aluno, guardando também
## a situação em um dicionário. No final, mostre o conteúdo
## da estrutura na tela.

aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['situacao'] = "Aprovado"
else:
    aluno['situacao'] = "Reprovado"

# Resultado
print('\n')
for c in aluno.keys():
    print(f" : {aluno[c]}")