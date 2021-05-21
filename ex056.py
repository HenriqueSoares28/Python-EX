soma = 0
velho = 0
nome_velho = ''
mulheres = 0
for p in range(1,5):
    print(F'----- {p}° PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mn':
        velho = idade
        nome_velho = nome
    if sexo in'Mm' and idade > velho:
        velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1

print ('A média de idade do grupo é de {:.1f} anos'.format(soma/4))
print ('O homem mais velho tem {} e se chama {}'.format(velho, nome_velho))
print ('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))
