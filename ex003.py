n1 = int(input ('Digite um numero: '))
n2 = int(input ('Digite outro numero: '))
s = (n1+n2)
cores = {
'limpa':'\033[m', 
'azul':'\033[34m',
'amarelo':'\033[33m',
'vermelho':'\033[31m'
}
print ('A soma entre {}{}{} + {}{}{} = {}{}{}'.format(cores['azul'], n1, cores['limpa'], cores['amarelo'], n2, cores['limpa'], cores['vermelho'], s, cores['limpa'],))