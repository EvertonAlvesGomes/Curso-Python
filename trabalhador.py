### trabalhador.py

## Solicite ao usuário que entre com dados de uma pessoa:
## nome, ano de nascimento e carteira de trabalho (CTPS).
## Se a CTPS for válida, solicite ao usuário entrar com dados
## de ano de contratação e salário.
## Retorne: nome, idade, CTPS, ano de contratação, salário e 
## qual ano a pessoa irá se aposentar.

from datetime import datetime

worker = dict()

worker['nome'] = str(input("Nome: "))
worker['ano_nasc'] = int(input("Ano de nascimento: "))
worker['ctps'] = int(input("Carteira de Trabalho (0 = não tem): "))
if worker['ctps'] != 0:
    worker['ano_cont'] = int(input("Ano de contratação: "))
    worker['salario'] = float(input("Salário: R$ "))
else:
    worker['ano_cont'] = "N/A"
    worker['salario'] = "N/A"

# -------- RESULTADOS -------- #
print()
print(f"Nome: {worker['nome']}")
print(f"Idade: {datetime.now().year - worker['ano_nasc']}")
print(f"CTPS: {worker['ctps']}")
if worker['ctps'] != 0:
    print(f"Contratação em {worker['ano_cont']}")
    print(f"Salário: {worker['salario']}")
    print(f"Aposentadoria será com {worker['ano_cont'] + 35 - worker['ano_nasc']} anos")


