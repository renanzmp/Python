#CRIANDO UM MENU DE OPÇÕES

num1 = float(input('Digite o primeiro número:\n'))
num2 = float(input('DIgite o segundo número:\n'))

def acoes(num1, num2):
    while True:
        print('Escolha uma opção:')
        menu = int(input('[1] Somar\n[2] Multiplicar\n[3] Mostrar o maior\n[4] Escolher novos números\n[5] Sair do programa\n'))
        
        while str(menu) not in '1 2 3 4 5':
            print('DIgite uma opão válida!')
            menu = int(input('[1] Somar\n[2] Multiplicar\n[3] Mostrar o maior\n[4] Escolher novos números\n[5] Sair do programa\n'))
        
        if menu == 1:
            soma = num1 + num2
            print(f'A soma entre {num1} e {num2} é {soma}')
        elif menu == 2:
            produto = num1 * num2
            print(f'O produto entre {num1} e {num2} é {produto}')
        elif menu == 3:
            if num1 > num2:
                print(f'O número {num1} é maior que o número {num2}')
            elif num1 < num2:
                print(f'O número {num2} é maior que o número {num1}')
            else:
                print('Os números são iguais')
        elif menu == 4:
            num1 = float(input('Digite o primeiro número:\n'))
            num2 = float(input('DIgite o segundo número:\n'))
        elif menu == 5:
            print('Fim do programa')
            break

acoes(num1, num2)