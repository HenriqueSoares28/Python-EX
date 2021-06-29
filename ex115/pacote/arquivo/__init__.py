def leiaInt(texto):
    while True:
        try:
            i = int(input(texto))
        except:
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return i




def mostrar(nome):
    try:
        a = open(nome,'r')
    except:
        print('Erro ao encontrar arquivo.')
    else:
        lista = list(a.readlines())
        for c in range(0, len(lista), 2):
            print(f"{f'{lista[c].strip()}':30} {f'{lista[c+1].strip()} anos':>8}")
        a.close()
        
def adicionar():
    while True:
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        
        
        a = open('arquivo.txt','r')
        c = a.readlines()
        c.append(f'{nome}\n')
        c.append(f'{str(idade)}\n')
        
        a.close()
        
        a = open('arquivo.txt','w')
        a.writelines(c)
        
        
        c = str(input('Quer continuar: [S/N] ')).upper()
        if c in 'N':
            break
        else:
            continue
    

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
        

def criarArquivo(nome):
    try:
        a = open(nome, 'w')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')