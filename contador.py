 ### contador.py

 ## Três tipos de contagem:
 ## 1) Contagem de 1 a 10, de 1 em 1
 ## 2) Contagem de 10 a 0, de 2 em 2
 ## 3) Contagem personalizada, com limites e passo definidos pelo usuário.
 ## Nesse caso, se o usuário digitar primeiro o limite superior e depois o inferior,
 ## o programa deve entender que a contagem é regressiva, independentemente se o passo
 ## é negativo ou positivo. Se o limite inferior for informado primeiro e o superior em segundo,
 ## a contagem deve ser sucessiva ainda que o passo seja negativo.

from time import sleep

def contagem(lim_inf, lim_sup, passo):
    cont = 0

    # verificação de passo nulo
    if passo == 0:
        passo = 1

    # contagem sucessiva
    if lim_inf < lim_sup:
        if passo < 0:
            passo *= -1     # correção do sinal do passo
        # realiza a contagem
        cont = lim_inf
        while cont <= lim_sup:
            print(cont, end=' ')
            cont += passo
            sleep(0.25)
        print("FIM!")
    else:
        if lim_inf > lim_sup:
            if passo > 0:
                passo *= -1     # correção do sinal do passo
            # realiza a contagem
            cont = lim_inf
            while cont >= lim_sup:
                print(cont, end=' ')
                cont += passo
                sleep(0.25)
            print("FIM!")
        else:   # lim_inf == lim_sup
            print("Os dois limites são iguais.\n")


def linha_div():
    print("="*30)

# Contagens padronizadas:
linha_div()
print("Contagem de 1 até 10 de 1 em 1:")
for cont in range(0,10):
    print(f"{cont+1} ", end='')
    sleep(0.25)
print("FIM!")

linha_div()
print("Contagem de 10 até 0 de 2 em 2:")
cont = 10
while cont >= 0:
    print(f"{cont} ", end='')
    cont -= 2
    sleep(0.25)
print("FIM!")


# Entrada de dados
linha_div()
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
final = int(input("Final: "))
passo = int(input("Passo: "))
print()

contagem(inicio, final, passo)