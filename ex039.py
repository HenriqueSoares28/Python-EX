ano = int(input('Ano do nascimento: '))
idade = 2021 - ano
print ('Quem nasceu em {} tem {} em 2021.'.format(ano, idade))
if idade < 18:
    print('Ainda faltam {} anos para seu alistamento'. format(18 - idade))
elif idade == 18:
    print('Você tem que se alista IMEDIATAMENTE!')
else:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(ano + 18))