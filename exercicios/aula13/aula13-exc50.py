#SOMA DOS PARES

s = 0

for i in range(0, 6):
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        s += num

print(s)
