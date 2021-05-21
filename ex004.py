i = input('Digite algo: ')

print('Só tem espaços? ', i.isspace())
print('Só tem números? ', i.isnumeric())
print('Só tem letras? ', i.isalpha())
print('É alphanumérico? ', i.isalnum())
print('Está em maiusculas? ', i.isupper())
print('Está em minusculas? ', i.islower())
print('Está capitalizada? ', i.istitle())