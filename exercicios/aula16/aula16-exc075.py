#ANÁLISE DE DADOS EM UMA TUPLA

num1 = int(input('Digite um número:\n'))
num2 = int(input('Digite um número:\n'))
num3 = int(input('Digite um número:\n'))
num4 = int(input('Digite um número:\n'))
cont_9 = 0
numeros = (num1, num2, num3, num4)
posicao_3 = 0

if 3 in numeros:
    posicao_3 = numeros.index(3) + 1

for i in numeros:
    if i == 9:
        cont_9 += 1

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {cont_9} vezes')

if posicao_3 == 0:
    print('O valor 3 não apareceu em nenhuma posição')
else:
    print(f'O valor 3 aparaceu na {posicao_3}° posição')

print(f'Os valores pares digitados foram', end=" ")
for j in numeros:
    if j % 2 == 0:
        print(f'{j}', end=" ")


