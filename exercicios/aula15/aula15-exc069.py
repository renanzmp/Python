#ANÁLISE DE DADOS DO GRUPO

pessoas_mais_18 = 0
homem = 0
mulheres_menos_20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper()
    while True:
        if sexo not in ['M', 'F']:
            print('Digite um sexo válido')
            sexo = input('Sexo: [M/F] ').upper()
        else:
            break
    if idade >= 18:
        pessoas_mais_18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    
    continuar = input('Quer continuar? [S/N] ').upper()
    while True:
        if continuar not in ['S', 'N']:
            continuar = input('Quer continuar? [S/N] ').upper()
        else:
            break
    if continuar == 'N':
        break

print(f'Um total de {pessoas_mais_18} pessoas maiores de idade foram cadastraos')
print(f'Um total de {homem} homens foram cadastrados')
print(f'Um total de {mulheres_menos_20} mulheres com menos de 20 anos foram cadastrados')