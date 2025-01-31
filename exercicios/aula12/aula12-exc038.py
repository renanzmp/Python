#COMPARANDO NUMEROS
print('Vamos comparar números')

num1 = int(input('Digite um número inteiro:\n'))
num2 = int(input('Digite outro número inteiro:\n'))

if num1 > num2:
    print('O número {} é maior que o número {}'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior que o número {}'.format(num2, num1))
else:
    print('Não existe valor maior, os números sao iguais')