def notas(*num, sit = False):
    '''
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias).
        :param sit: valor opcionar, indicando se deve ou nao adicionar a situação.
        :return: dicionário com várias informações sobre a situação da turma.
    '''
    dici = dict()
    dici['total'] = len(num)
    dici['maior'] = max(num)
    dici['menos'] = min(num)
    dici['media'] = sum(num) / len(num)
    if sit:
        if dici['media'] < 6:
            dici['situação'] = 'Ruim'
        elif 6 <= dici['media'] < 7:
            dici['situação'] = 'Razoavel'
        else:
            dici['situação'] = 'Boa'    
    return dici


#main
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)