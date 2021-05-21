
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#sc = ca**2+co**2
#rh = sc**(1/2)
#print ('A hipotenusa vai medir {:.2f}'.format(rh))

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print ('A hipotenusa vai medir {:.2f}'.format(hi))