### tupla20.py

## Uma tupla totalmente preenchida é utilizada para retornar
## um número por extenso solicitado pelo usuário

tupla20 = ("Zero", "Um", "Dois", "Três", "Quatro",
            "Cinco", "Seis", "Sete", "Oito", "Nove",
            "Dez", "Onze", "Doze", "Treze", "Quatorze",
            "Quinze", "Dezesseis", "Dezessete",
            "Dezoito", "Dezenove", "Vinte")

num = -1
while num < 0 or num > 20:
    num = int(input("Digite um número de zero a vinte: "))
    if num < 0 or num > 20 :
        print("Valor inválido!")

print(f"Você digitou o número {tupla20[num]}")