#PRIMEIRO E ULTIMO NOME DE UMA STRING

nome = input('Digite seu nome completo\n')
nome_minusculo = nome.lower()
nome_split = nome_minusculo.split()
print(nome_split[0])
print(nome_split[-1])

