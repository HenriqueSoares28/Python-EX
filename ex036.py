val = int(input('Valor da casa? R$'))
sal = int(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
pres = val/anos/12
por = sal*3/10
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(val,anos,pres))
if pres > por:
    print('Empréstimo \033[2;31m NEGADO!\033[m')
else:
    print('Empréstimo \033[2;32m ACEITO!\033[m')