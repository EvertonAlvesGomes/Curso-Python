### randomNumbers.py

from random import random, sample

# random_numbers = (int(random()*10),int(random()*10),int(random()*10),int(random()*10),int(random()*10))
random_numbers = tuple(sample(range(10),5))
# O método sample retorna uma lista. Por isso, é necessário fazer o casting para tuple.


# Números gerados:
print("Números gerados:")
for i in range(0,5):
    print(random_numbers[i], end=' ')

print("\n")

# Maior e menor número gerado:
# print(f"Maior número: {sorted(random_numbers)[4]}")
# print(f"Menor número: {sorted(random_numbers)[0]}")
print(f"Maior número: {max(random_numbers)}")
print(f"Menor número: {min(random_numbers)}")