nome = str(input("Escreva seu nome completo: "))
print('Nome em maiusculo: ',(nome.upper()))
print('Nome em minusculo: ',(nome.lower()))
num = (len(nome))
esp = (nome.count(' '))
letras = (num-esp)
print ('Quantidade de letras: ',(letras))
nome1 = (nome.split()[0])
num1 = (len(nome1))
print ('Quantidade de letras do 1° nome:',(num1))