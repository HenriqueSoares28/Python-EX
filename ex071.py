valorfinal = nota100 = nota50 = nota20 = nota10 = nota5 = nota1 = 0
print('='*40)
print('{: ^40}'.format('BANCO CEV'))
print('='*40)
valor = int(input('Que valor você quer sacar? R$'))
while valor != 0:
    if valor >= 100:
        nota100 = valor//100
        valor = valor % 100
        print(f'Total de {nota100} cédulas de R$100')
    if valor >= 50:
        nota50 = (valor//50)
        valor = valor % 50
        print(f'Total de {nota50} cédulas de R$50')
    if valor >= 20:
        nota20 = valor//20
        valor = valor % 20
        print(f'Total de {nota20} cédulas de R$20')
    if valor >= 10:
        nota10 = valor//10
        valor = valor % 10
        print(f'Total de {nota10} cédulas de R$10')
    if valor >= 5:
        nota5 = valor//5
        valor = valor % 5
        print(f'Total de {nota5} cédulas de R$5')
    if valor >= 1:
        nota1 = valor//1
        valor = valor % 1
        print(f'Total de {nota1} cédulas de R$1')
print('='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
    