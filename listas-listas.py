### listas-listas.py

## Explorando outros recursos de listas

turma = [['Goula',27], ['Frodo',24], ['Humbertin', 25], ['Gabi', 26]]

for p in turma:
    print(f'{p[0]} tem {p[1]} anos de idade')

print(sorted(turma))    # ordem alfabética

victor_sants = ['Victor', 23]
turma.append(victor_sants[:])
print(turma)
victor_sants = ["Sant'Anna",23]
print(turma)
victor_sants.clear()    # apaga a lista