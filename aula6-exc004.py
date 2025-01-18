#DISSECANDO UMA VARIÁVEL

a = input('Digite algo: ')
print(type(a))

print('É numérico?' , a.isnumeric())
print('É alfabético?' , a.isalpha())
print('É alfanumérico? ' , a.isalnum())
print('Tem somente espaços?' , a.isspace())