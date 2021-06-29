def leiaDinheiro(preco):
    while True:
        d = str(input(preco)).strip().replace(',','.')
        if d.isalpha():
            print(f'ERRO: "{d}" é um preço inválido!') 
        else:
            return float(d)