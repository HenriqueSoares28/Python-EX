def metade(num, f=False):
    met = num / 2
    if f:
        return moeda(met)
    return met


def dobro(num, f=False):
    dob = num * 2
    if f:
        return moeda(dob)
    return dob


def aumentar(num, por, f=False):
    num += num * por/100
    if f:
        return moeda(num)
    return num


def diminuir(num, por, f=False):
    num -= num * por/100
    if f:
        return moeda(num)
    return num 


def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')


def resumo(val=0, taxaa=10, taxar=5):
    print('-'*30)
    print(f"{'RESUMO DO VALOR'.center(30)}")
    print('-'*30)
    print(f'Preço analizado: \t{moeda(val)}')
    print(f'Dobro do preço: \t{dobro(val, True)}')
    print(f'Metade do preço: \t{metade(val, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(val, taxaa, True)}')    
    print(f'{taxar}% de redução: \t{aumentar(val, taxar, True)}')    
    print('-'*30)