#GRUPO DA MAIORIDADE
import datetime

ano = datetime.date.today().year
maiores_de_idade = 0



for i in range(1, 8):
    nascimento = int(input('{}° pessoa, escreva o seu ano de nascimento:\n'.format(i)))
    while nascimento > ano:
        print('Digite um ano válido')
        nascimento = int(input('{}° pessoa, escreva o seu ano de nascimento:\n'.format(i)))
        
    if ano - nascimento >= 18:
        maiores_de_idade += 1

menores_de_idade= 7 - maiores_de_idade

print('{} pessoas já atingiram a maioridade enquanto {} ainda não'.format(maiores_de_idade, menores_de_idade))
