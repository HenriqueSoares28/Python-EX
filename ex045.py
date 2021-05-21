from random import choice
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
lista = [0,1,2]
opc = int(input('Qual é a sua jogada? '))
opc2 = choice(lista)

sleep(1)
print('\033[1;33mJO\033[m')
sleep(1)
print('\033[1;33mKEN\033[m')
sleep(1)
print('\033[1;3mPO!!!\033[m')
sleep(1)

print('\033[1;35m-=\033[m'*15)

print('Computador jogou ', end='')
if opc2 == 0:
    print('PEDRA')
elif opc2 == 1:
    print('PAPEL')
else:
    print('TESOURA')

print('Jogador jogou ', end='')
if opc == 0:
    print('PEDRA')
elif opc == 1:
    print('PAPEL')
else:
    print('TESOURA')

print('\033[1;35m-=\033[m'*15)

if opc == 0:
    if opc2 == 0:
        print('EMPATE')
    elif opc2 == 1:
        print('BOT WINS!')
    else:
        print('PLAYER WINS!')
elif opc == 1:
    if opc2 == 0:
        print('PLAYER WINS!')
    elif opc2 == 1:
        print('EMPATE')
    else:
        print('BOT WINS!')
elif opc == 2:
    if opc2 == 0:
        print('BOT WINS!')
    elif opc2 == 1:
        print('PLAYER WINS!')
    else:
        print('EMPATE')