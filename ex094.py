lista = list()
dici = dict()
soma = 0 
while True:
    dici['nome'] = str(input('Nome: '))
    while True:
        dici['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if dici['sexo'] in 'MF':
            break
        else:
            print('ERRO! Responda apenas M ou F')
    dici['idade'] = int(input('Idade: '))
    print(dici)
    lista.append(dici)

    
    while True:
        cont = str(input('Quer continuar? [S/N] '))
        if cont in 'NnSs':
            break
        else:
            print('ERRO! Responda apenas com S ou N.')
    if cont in ('Nn'):
        break
print(lista)    
'''print(lista)   
for c in range(len(lista)):
    soma += lista[c]['idade']
cont = len(lista)
media = soma / cont
print(cont)
print(soma)
print('=-'*30)
print(f'A) Ao todo temos {len(lista)} cadastradas.')   
print(f'B) A média de idade é de {media:.2f} anos')
#for c in range()
print('C) AS mulheres cadastradas foram ',end='')
for c in range(len(lista)):
    print(lista[c])
print()'''
