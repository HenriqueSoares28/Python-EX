d = int(input('Quantos dias alugado?')) 
km = int(input('Quantos Km rodados? '))
pd = d*60
pkm = km*0.15
p = pd+pkm
print('O total a pagar é de R${:.2f}'.format(p))