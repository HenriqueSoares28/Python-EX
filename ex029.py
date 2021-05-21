velo = int(input('Qual a velocidade atual do carro? '))
if (velo<=80):
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = float(velo-80)*7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você terá que pagar uma multa de R${:.2f}!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')