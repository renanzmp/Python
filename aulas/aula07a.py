n1 = int(input('Digite o 1° numero: '))
n2 = int(input('Digite o 2° numero: '))

soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
pot = n1 ** n2

print('A soma entre os números digitados é {},\n a subtração é {},\n a multiplicação é {}'.format(soma, sub, multi), end=' ')
print('a potenciação é {}'.format(pot))
