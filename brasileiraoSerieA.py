### brasileiraoSerieA.py

print("------------------------------")
print("      BRASILEIRÃO SÉRIE A     ")
print("------------------------------")

serie_a = ("Flamengo","Internacional","Atlético-MG","São Paulo","Fluminense",
            "Grêmio", "Palmeiras","Santos","Athletico-PR","Bragantino",
            "Ceará","Corinthians","Atlético-GO","Bahia","Sport","Fortaleza",
            "Vasco","Goiás","Coritiba","Botafogo")

# 5 primeiros colocados
print("Os cinco primeiros colocados foram:")
for c in range(0,5):
    print("- ", end='')
    print(serie_a[c])

# 4 últimos colocados
print("\nOs quatro últimos colocados (rebaixados) foram:")
for r in range(15,19):
    print("- ", end='')
    print(serie_a[r])

# Times em ordem alfabética
print("\nTimes em ordem alfabética:")
print(sorted(serie_a))

# Em qual posição ficou o galão da massa?
for galo in range(0,20):
    if serie_a[galo] is "Atlético-MG":
        print(f"\nO galim ficou na {galo+1}ª posição")
        break
    