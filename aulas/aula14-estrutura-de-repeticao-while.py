'''for i in range(1, 10):
    int(input('Digite a sua idade:\n'))
print('Fim')'''

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um número:\n'))
    
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} números ímpares e {} números pares'.format(impar, par))