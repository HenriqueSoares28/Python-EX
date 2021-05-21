
from time import sleep
valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))
opc = 0
sair = False
maior = 0
while not sair:
    print('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
    ''')
    opc = int(input('>>>> Qual sua opção? '))
    if opc == 1:
        print('A soma entre os valores {} e {} é {}.'.format(valor_1, valor_2, valor_1 + valor_2))
    if opc == 2:
        print('A multiplicação entre os valores {} e {} é {}.'.format(valor_1, valor_2, valor_1 * valor_2))
    if opc == 3:
        maior = valor_1
        if valor_2 > valor_1:
            maior = valor_2
        print('O número {} é o maior valor.'.format(maior))
    if opc == 4:
        valor_1 = int(input('Primeiro valor: '))
        valor_2 = int(input('Segundo valor: '))
    if opc == 5:
        sair = True
    sleep(5)   

