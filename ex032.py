from datetime import date
ano = int(input('Me diga um ano qualquer (coloque 0 para analizar o ano atual): '))
if ano == 0:
    ano = date.today().year
if (ano % 4) == 0 and ano % 100 != 0 or ano %400 == 0:
    print('O ano escolhido é um ano Bissexto!')
else:
    print('O ano escolhido não é um ano Bissexto!')
