import math
n = float(input('Digite um número: '))
#print('O valor digitado foi {} e a sua porção inteira é {:.0f}'. format(n,n))
print('O valor digitado foi {} e a sua porção inteira é {}'. format(n, math.trunc(n)))