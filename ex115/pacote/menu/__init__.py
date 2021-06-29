from time import sleep


def leiaInt(texto):
    while True:
        try:
            i = int(input(texto))
        except:
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return i


def menu():
    print('-'*40)
    print('MENU PRINCIPAL'.center(40))
    print('-'*40)
    print('\033[0;33m1\033[m'' - ''\033[0;34mVer pessoas cadastradas\033[m')
    print('\033[0;33m2\033[m'' - ''\033[0;34mCadastrar nova Pessoa\033[m')
    print('\033[0;33m3\033[m'' - ''\033[0;34mSair do sistema\033[m')
    print('-'*40)


def select():
    while True:
        try:
            s = leiaInt('Sua opção: ')
            if s in range(1,4):
                break  
            else:
                print('\033[0;31mErro: digite uma opção válida!\033[m')
                sleep(1)
                menu()
        
        except ValueError:
            print('\033[0;31mErro, por favor digite um número inteiro válido.\033[m')
            continue
    return s
    
        