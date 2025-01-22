#VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO

cidade = input('Digite o nome de uma cidade\n')
cidade_minusculo = cidade.lower()
cidade_split = cidade_minusculo.split()
if 'santo' in cidade_split[0]:
    print('A cidade começa com a palavra Santo')
else:
    print('A cidade não começa com a palavra Santo')