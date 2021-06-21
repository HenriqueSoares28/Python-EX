def fatorial(num=1, show=False):
    """
        -> Calcula o Fatorial de um número.
        :param n: O número a ser calculado
        :param show: (opcional) Mostra ou não a conta
        :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range (num, 0, -1):
        f *= c
    if show:
        def conta(num1, f1):
            print('-'*30)
            for j in range(num1, 1, -1):
                print(f'{j}', end=' x ')
            print(f'1 = {f1}')
        return conta(num, f)

    else:
        return print('-'*30), print(f)

#main
fatorial(5, True)
help(fatorial)
   