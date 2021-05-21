maior18 = homens = mulher_20 = 0 
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ').upper())
    print('-'*30)
    continuar = str(input('Quer continuar? [S/N] ').upper())
    if idade >= 18:
        maior18 += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulher_20 += 1
    if continuar in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} cadastrados.')
print(f'Temos {mulher_20} com menos de 20 anos.')