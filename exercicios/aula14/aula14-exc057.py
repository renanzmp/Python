#VALIDAÇÃO DE DADOS

sexo = str(input('Qual o seu sexo?\nDigite M para Masculino e F para Feminino\n')).upper()

while sexo not in "M F":
    print('Digite um valor válido!')
    sexo = str(input('Qual o seu sexo?\nDigite M para Masculino e F para Feminino\n')).upper()

if sexo == 'M':
    print('Você é do sexo Masculino')
else:
    print('Você é do sexo Feminino')
