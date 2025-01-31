#APROVANDO EMPRÉSTIMOS

casa = float(input('Qual o valor da casa?\n'))
salario = float(input('Qual o seu salário?\n'))
anos = int(input('Em quantos anos você vai pagar pela casa?\n'))
meses = anos * 12
prestacao = casa / meses


if (casa / meses) < (30/100) * salario:
    print('O seu empréstimo foi aprovado, você pagará R${:.2f} mensal durante {} anos'.format(prestacao, anos))
else:
    print('O seu empréstimo não foi aprovado')

