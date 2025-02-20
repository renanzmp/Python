#MAIOR E MENOR VALORES EM TUPLA
import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)
num4 = random.randint(1, 10)
num5 = random.randint(1, 10)
numeros = (num1, num2, num3, num4, num5)

print(f'Os números gerados foram:', end=" ")
for i in numeros:
    print(f'{i}', end=" ")
print(f'\nO maior número foi {max(numeros)}')
print(f'O menor número foi {min(numeros)}')

