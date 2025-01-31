#CONVERSOR DE BASES NUMÉRICAS

num = int(input('Digite um número inteiro\n'))
base = int(input('Agora digite para qual base você quer transformar:\nDigite 1 para binário;\nDigite 2 para octal;\nDigite 3 para hexadecimal\n'))
base2 = bin(num)[2:]
base8 = oct(num)[2:]
base16 = hex(num)[2:]

while str(base) not in '1 2 3':
    print('Digite uma base válida!\n')
    base = int(input('Digite para qual base você quer transformar:\nDigite 1 para binário;\nDigite 2 para octal;\nDigite 3 para hexadecimal\n'))


if base == 1:
    print('O número na base decimal {} convertido para binário é {}'.format(num, base2))
elif base == 2:
    print('O número na base decimal {} convertido para octal é {}'.format(num, base8))
else:
    print('O número na base decimal {} convertido para hexadecimal é {}'.format(num, base16))