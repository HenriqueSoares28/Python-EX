c_none = ('\033[m')
c_red = ('\033[0;31m')
c_green = ('\033[0;32m')
c_yellow = ('\033[0;33m')
c_blue = ('\033[0;34m')
c_pink = ('\033[0;35m')
c_cyan = ('\033[0;36m')
c_grey = ('\033[0;37m')

from time import sleep
from random import randrange
resultado = ''
par_inpar = ''
print('{}{}{}'.format(c_yellow, '=-'*15, c_none))
print('VAMOS JOGAR PAR OU ÍMPAR')
print('{}{}{}'.format(c_yellow, '=-'*15, c_none))
sleep(3)
while True:
    pess = int(input('Digite um número: '))
    comp = randrange(1,10)
    pi = str(input('Par ou Ímpar [P/I] ? ').upper())
    div = (pess + comp) % 2
    if 'P' in pi:
        if div == 0:
            resultado = 'VENCEU!'
            par_inpar = 'Par'
        else:
            resultado = 'Perdeu.'
            par_inpar = 'Ímpar'
    elif 'I' in pi:
        if div == 0:
            resultado = 'Perdeu.'
            par_inpar = 'Par'
        else:
            resultado = 'VENCEU!'
            par_inpar = 'Ímpar'
    print('{}{}{}'.format(c_green, '-'*30, c_none))
    print(f'Você jogou {pess} e o computador {comp}.')
    print(f'Total de {pess + comp}, deu {par_inpar}!')
    print('{}{}{}'.format(c_green, '-'*30, c_none))
    print(f'Você {resultado}')
    print(f'{c_red}-{c_none}'*30)
    print('Vamos jogar novamente...')
    print('')
    sleep(2)