#ANALISADOR DE TEXTOS

nome = input('Digite seu nome completo\n')  

maiusculas = nome.upper()
minusculas = nome.lower()

nome_sem_espaço = nome.replace(' ', '')

letras = len(nome_sem_espaço)

nome_dividido = nome.split()
letras_nome_divido = len(nome_dividido[0])
print(maiusculas, minusculas, letras, letras_nome_divido)