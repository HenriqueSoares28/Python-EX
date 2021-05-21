sal = float(input('Qual é o salário do funcionário? R$'))
if sal >= 1250:
    au1 = sal/10
    print('O aumento do salário do funcinário será de R${:.2f} e o novo valor será R${:.2f}'.format(au1,au1+sal))
else:
    au2 = sal*15/100
    print('O aumento do salário do funcinário será de R${:.2f} e o novo valor será R${:.2f}'.format(au2,au2+sal))