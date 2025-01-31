#GERENCIADOR DE PAGAMENTOS

valor = float(input('Digite o valor do produto que você quer comprar:\n'))
while valor <= 0:
    print('Digite um valor válido!')
    valor = float('Digite o valor do produto que você quer comprar:\n')

forma_de_pagamento = int(input('Escolha a forma de pagamento:\nDIgite 1 para pagar à vista em dinheiro ou em cheque com 10% de desconto;\nDigite 2 para pagar à vista no cartão com 5% de desconto;\nDigite 3 para parcelar em 2x no cartão com o preço normal;\nDigite 4 para parcelar em 3 vezes ou mais no cartão com 20% de juros\n'))
while str(forma_de_pagamento) not in ('1 2 3 4'):
    print('Digite uma forma de pagamento válida')
    forma_de_pagamento = int(input('Escolha a forma de pagamento:\nDIgite 1 para pagar à vista em dinheiro ou em cheque com 10% de desconto;\nDigite 2 para pagar à vista no cartão com 5% de desconto;\nDigite 3 para parcelar em 2x no cartão com o preço normal;\nDigite 4 para parcelar em 3 vezes ou mais no cartão com 20% de juros:\n'))

if forma_de_pagamento == 1:
    desconto_a_vista = (90 / 100) * valor
    print('O valor à vista no dinheiro/cheque ficou R${:.2f}'.format(desconto_a_vista))
elif forma_de_pagamento == 2:
    desconto_cartao = (95 / 100) * valor
    print('O valor à vista no cartão ficou R${:.2f}'.format(desconto_cartao))
elif forma_de_pagamento == 3:
    parcela_2x = valor / 2
    print('O valor parcelado no cartão em 2x ficou R${:.2f} por mês, totalizando R${:.2f}'.format(parcela_2x, valor))
elif forma_de_pagamento == 4:
    parcela_x = int(input('Digite em quantas vezes você quer parcelar o produto em até 12x:\n'))
    valor_x = ((120 / 100) * valor)
    valor_parcela_x = valor_x / parcela_x
    while parcela_x < 3 or parcela_x > 12:
        print('Digite um valor de 3 para cima ou menor que 12')
        parcela_x = int(input('Digite em quantas vezes você quer parcelar o produto em até 12x:\n'))
    print('O valor parcelado no cartão em {}x ficou R${:.2f} por mês, totalizando R${:.2f}'.format(parcela_x, valor_parcela_x, valor_x))
    



