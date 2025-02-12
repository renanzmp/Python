#ESTATÍSTICAS EM PRODUTO

total = 0
produtos_mais_de_mil_reais = 0
produto_mais_barato = ''
preco_produto_mais_barato = 0


while True:
    nome = input('Digite o nome do produto:\n')
    preco = float(input('Digite o valor do produto em R$:\n'))

    while True:
        if preco <= 0:
            print('Digite um valor válido')
            preco = float(input('Digite o valor do produto em R$:\n'))
        else:
            break
    
    if preco > 1000:
        produtos_mais_de_mil_reais += 1

    if produto_mais_barato == '':
        produto_mais_barato = nome
        preco_produto_mais_barato = preco
    elif preco < preco_produto_mais_barato:
        produto_mais_barato = nome
        preco_produto_mais_barato = preco
    
    total += preco

    continuar = input('Quer continuar? [S/N]: ').upper()
    while True:
        if continuar not in ['S', 'N']:
            continuar = input(print('Quer continuar? [S/N]: ')).upper()
        else:
            break
    if continuar == 'N':
        break

print(f'Você gastou um total de R${total} na compra')
print(f'Você comprou um total de {produtos_mais_de_mil_reais} produtos que custam mais de R$1000')
print(f'{produto_mais_barato} é o produto mais barato da compra custando R${preco_produto_mais_barato}')