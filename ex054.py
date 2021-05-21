cont = 0
cont2 = 0
for p in range(1,8):
    idade = int(input('Em que ano a {}ª pessoa nasceu? '.format(p)))
    idade2 = 2021 - idade
    if idade2 >= 18:
        cont += 1
    else:
        cont2 += 1       
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont))
print('Ao todo tivemos {} pessoas menores de idade'.format(cont2))