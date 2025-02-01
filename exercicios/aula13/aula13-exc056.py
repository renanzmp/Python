#ANALISADOR COMPLETO

idade_homem_mais_velho = 0
nome_homem_velho = 0
idade_mulher_menos_20 = 0

nome_geral = []

idade_geral = []
idade_homem = []
idade_mulher = []

sexo_homem = []
sexo_mulher = []

for i in range(1, 6):
    nome = str(input('{}° pessoa, qual o seu nome?\n'.format(i)))

    idade = int(input('{}° pessoa, digite a sua idade:\n'.format(i)))
    while idade < 0:
        print('Digite uma idade válida')
        idade = int(input('{}° pessoa, digite a sua idade:\n'.format(i)))

    sexo = str(input(('Digite M para Masculino\nDigite F para feminino\n'))).upper().strip()
    if sexo not in 'F M m f':
        print('{}° pessoa, escolha um sexo válido'.format(i))
        sexo = str(input(print('Digite M para Masculino\nDigite F para feminino'))).upper().split()

    nome_geral.append(nome)
    idade_geral.append(idade)

    if idade < 20 and sexo == "F":
        idade_mulher_menos_20 += 1

    if sexo == 'M':
        idade_homem.append(idade)
        sexo_homem.append(sexo)
        if i == 1:
            idade_homem_mais_velho = idade
            nome_homem_velho = nome
        elif i > 1 and idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_velho = nome
    elif sexo == 'F':
        idade_mulher.append(idade)
        sexo_mulher.append(sexo)

soma_idade = sum(idade_geral)
media_idade = soma_idade / len(idade_geral)

print('A média de idade do grupo é {}'.format(media_idade))
print('O homem mais velho se chama {} e ele tem {} anos'.format(nome_homem_velho, idade_homem_mais_velho))
print('Ha {} mulheres com menos de 20 anos de idade'.format(idade_mulher_menos_20))



