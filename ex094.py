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
    lista.append(dici.copy())
 
    while True:
        cont = str(input('Quer continuar? [S/N] '))
        if cont in 'NnSs':
            break
        else:
            print('ERRO! Responda apenas com S ou N.')
    if cont in ('Nn'):
        break
     
for c in range(len(lista)):
    soma += lista[c]['idade']
cont = len(lista)
media = soma / cont
print('=-'*30)
print(f'A) Ao todo temos {len(lista)} cadastradas.')   
print(f'B) A média de idade é de {media:.2f} anos')
print('C) As mulheres cadastradas foram: ',end='')
for c in range(len(lista)):    
    if lista[c]['sexo'] in 'F':
        print(lista[c]['nome'], end=' ')
print()
print('D) Lista das pessoas que esttão acima da média:')
for c in range(len(lista)):
    if lista[c]['idade'] > media:
        print(f'    nome = {lista[c]["nome"]}; sexo = {lista[c]["sexo"]}; idade = {lista[c]["idade"]}')
print('<< ENCERRADO >>')