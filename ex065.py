'''Bloco de cores'''
c_none = ('\033[m')
c_red = ('\033[0;31m')
c_green = ('\033[0;32m')
c_yellow = ('\033[0;33m')
c_blue = ('\033[0;34m')
c_pink = ('\033[0;35m')
c_cyan = ('\033[0;36m')
c_grey = ('\033[0;37m')
'''Bloco de cores'''

parar =  False
cont = soma = media = num = 0
maior = num
menor = num
while not parar:
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    media = soma/cont
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    par = str(input('Quer continuar? [S/N] ').upper())
    if par in 'N':
        parar = True
print(' ')
print('{}{}{}'.format(c_red, '-='*30, c_none))
print('Você digitou {} números e a média foi de {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'. format(maior, menor))
print('{}{}{}'.format(c_red, '-='*30, c_none))