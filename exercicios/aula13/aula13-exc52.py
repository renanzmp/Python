#NÚMERO PRIMO

num = int(input('Digite um número inteiro:\n'))
dividiu = 0
n = 1


while(n < num + 1):
    if num % n == 0:
        dividiu += 1
    n+=1


if num == 0:
    print('Número 0')
elif num < 0:
    print('Número negativo')
elif dividiu < 3:
    print('Número Primo')
else:
    print('Número Não Primo')