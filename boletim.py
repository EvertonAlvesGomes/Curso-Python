### boletim.py

## Boletim com listas compostas

aluno = list()  # lista para cadastro de um aluno individualmente
alunos = list() # lista para cadastro dos alunos
s_n = 'S'   # variável para controle do while loop

while s_n == 'S':
    aluno.append(str(input("Nome: ")))
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    alunos.append(aluno[:])
    aluno.clear()   # apaga a lista para cadastrar o próximo aluno
    s_n = input("Quer continuar? [S/N] ")[0].upper()
    print('\n')

# Resultados
print('Nº   NOME        MÉDIA')
print('----------------------')
for i in range(0, len(alunos)):
    print(f"{i}   {(alunos[i][0])}        {(alunos[i][1]+alunos[i][2])/2}")

print('----------------------')