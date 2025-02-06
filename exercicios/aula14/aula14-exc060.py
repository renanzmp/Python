#CÁLCULO DO FATORIAL

#USANDO WHILE
num1 = int(input('Digite um número inteiro:\n'))
num2 = num1
n = 1


while n < num2 - 1:
    n += 1
    fatorial = num1 * n
    num1 = fatorial

print(num1)

#USANDO FOR
num3 = int(input('Digite um número inteiro:\n'))

for i in range(1, num3):
    num3 *= i

print(num3)


