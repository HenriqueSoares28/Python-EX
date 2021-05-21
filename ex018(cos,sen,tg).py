import math
a = int(input('Digite o ângulo que você deseja: '))
ar = math.radians(a)
sen = math.sin(ar)
cos = math.cos(ar)
tg = math.tan(ar)
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(a, sen))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(a, cos))
print('O ângulo de {:.1f} tem o TANGENTE de {:.2f}'.format(a, tg))
