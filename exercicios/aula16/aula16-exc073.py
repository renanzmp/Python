#TUPLAS COM TIMES DE FUTEBOL

times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athlético-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

prmeiros_5 = times[0:5]
ultimos_4 = times[-4:]
ordem_alfabetica = sorted(times)
vasco = times.index('Vasco')

print(f'Os 5 primeiros colocados são {prmeiros_5}')
print(f'Os últimos 4 colocados são {ultimos_4}')
print(f'Os times em ordem alfabética são {ordem_alfabetica}')
print(f'O Vasco está na {vasco + 1}° posição')
