import arquivo


def opc1(nome):
    print('-'*40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-'*40)
    arquivo.mostrar(nome)
    
    
def opc2():
    print('-'*40)
    print('CADASTRO'.center(40))
    print('-'*40)
    arquivo.adicionar()
    
    
    
    
def opc3():
    print('-'*40)
    print('Saindo do sistema... Até logo!'.center(40))
    print('-'*40)
    


def opc(num, opc=''):
    if num == 1:
        opc1(opc)
    if num == 2:
        opc2()
    if num == 3:
        opc3()