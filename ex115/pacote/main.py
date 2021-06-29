
import menu
import opc
import arquivo
from time import sleep

arq = 'arquivo.txt'
if not arquivo.arqExiste(arq):
    arquivo.criarArquivo(arq)

    
    
while True:
    menu.menu()
    s = menu.select()
    opc.opc(s, arq)
    sleep(1)
    if s == 3:
        break