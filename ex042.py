a = float(input('Primeiro segmento do triangulo: '))
b = float(input('Segundo segmento do triangulo: '))
c = float(input('Terceiro segmento do triangulo: '))
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos escolhidos podem formar um triângulo.')
    if a == b == c:
        print('Seu triangulo é EQUILATERO')
    elif a != b != c != a:
        print('Seu triangulo é ESCALENO')
    elif a == b !=c or b == c !=a or c == a != b:
        print('Seu triangulo é ISÓCELES')
    
else:
    print('Os segmentos escolhidos não podem formar um triângolo.')
