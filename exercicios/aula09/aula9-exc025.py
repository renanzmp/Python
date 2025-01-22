#PROCURANDO UMA STRING DENTRO DE OUTRA

nome = input('Digite seu nome completo\n')
nome_minusculo = nome.lower()
nome_split = nome_minusculo.split()

if "silva" in nome_split:
    print('Tem Silva no seu nome')
else:
    print('Não tem Silva no seu nome')
