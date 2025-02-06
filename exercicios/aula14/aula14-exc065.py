#MAIOR E MENOR VALORES

lista_numeros = []

while True:
    num = int(input('Digite um número:\n'))
    lista_numeros.append(num)
    while True:
        resposta = str(input('Deseja digitar outro número?\n[S] - Sim\n[N] - Não\n')).strip().upper()
        if resposta in ['S', 'N']:
            break
        print('Digite uma resposta válida')
    if resposta == 'N':
        break

maior = max(lista_numeros)
menor = min(lista_numeros)
media = sum(lista_numeros) / len(lista_numeros)

print(f'O menor número digitado foi {menor}, o maior número digitado foi {maior} e a média dos números digitados é {media}')



        
