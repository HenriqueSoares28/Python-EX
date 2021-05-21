cont9 = pos3 = cont = 0
val1 = int(input('Digite um número: '))
val2 = int(input('Digite outro número: '))
val3 = int(input('Digite mais um número: '))
val4 = int(input('Digite o último número: '))
val = (val1, val2, val3, val4)
print(f'Você digitou os valores {val}')
for v in val:
    if v == 9:
        cont9 += 1
print(f'O valor 9 aprece {cont9} vezes')
if 3 in val:
    print(f'O número 3 apareceu na posição {val.index(3)+1}')

print('Os números pares escolhidos foram: ', end='')
for v in val:
    if v % 2 == 0:
        cont += 1
 
while cont > 0:
    print(f'{val[cont]}', end='')
    cont -= 1
