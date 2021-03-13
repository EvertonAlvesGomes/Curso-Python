### fatorial_show.py


# --- FUNCTIONS --- #
def fatorial(n, show=True):
    """
    Calculates fatorial of a number and show the result with the print function
    (optionally).
    
    """
    fat = 1
    for i in range(n, 0, -1):
        fat *= i
    
    if show==True:
        print(f"O fatorial de {n} é {fat}")
    else:
        return fat
    

# --- MAIN PROGRAM --- #
ctr = True
n = int(input("Digite um número para calcular o fatorial: "))
fatorial(n, ctr)
if ctr == False:
    print(f"O fatorial de {n} é {fatorial(n, ctr)}")
