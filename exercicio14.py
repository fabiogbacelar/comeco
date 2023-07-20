




from exercicio05 import coletarPositivo

def mediaVolei():
    soma = 0
    qtde = int(input('Informe a quantidade de pessoas no time: '))
    #coletar todas as alturas
    for i in range(qtde):
        altura = coletarPositivo()
        soma += altura
    return 'A altura media do time é {}' .format(soma/qtde)