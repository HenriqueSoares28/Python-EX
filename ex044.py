print('='*10,'LOJAS CLEBÃO','='*10)
valor = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opc = int(input('Qual a opcão? '))
if opc == 1:
    porc1 = valor*10/100
    valor1 = (valor-(porc1))
    print('Sua compra a vista sairá por: R${:.2f}'.format(valor1))
elif opc == 2:
    porc2 = valor*5/100
    print('Sua compra a vista sairá por: R${:.2f}'.format(valor - (porc2)))
elif opc == 3:
    print('Sua compra sairá por: R${:.2f} sendo até duas parcelas de R${:.2f}'.format(valor, valor / 2))
elif opc == 4:
    parcelas = int(input('Qual o número de parcelas? '))
    totparc = valor + (valor*20/100)
    partparc = totparc / parcelas
    print('Sua compra sairá por um valor total de R${:.2f}, dividido em {} parcelas de R${:.2f}'.format(totparc, parcelas, partparc))
else:
    print('Opção invalida, tente novamente!')