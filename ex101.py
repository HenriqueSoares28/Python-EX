def idade(ano):
    import datetime 

    i = datetime.date.today().year - ano
    return i


#main 
print('-'*20)
ano = int(input('Em que ano você nasceu? '))
ida = idade(ano)
if ida >= 18:
    print(f'Com {ida} anos: VOTO OBRIGATÓRIO!')
elif 16 >= ida < 18 or ida > 65:
    print(f'Com {ida} anos: VOTO FACULTATIVO!') 
else:
    print(f'Com {ida} anos: VOTO PROIBIDO!') 

