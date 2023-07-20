notas = [] #vetor global = todas as funções podem
        # #visualizar/usar esse vetor

def preencherVetor(fim):
    for i in range(fim):
        num = int(input('Informe a {} nota : '.format(i+1)))
        notas.append(num) #Adicionando notas no vetor

def consultarVetor(fim):
    for i in range(fim):
        print('{} Posição: {}'.format(i+1,notas[i]))

def apagarPosicao(posicao):
    if(len(notas) < posicao):
        print('Impossivel remover,pois o tamanho e menor que a posicao')
    else:
        del(notas[posicao]) #Excluindo um dado do vetor
        print('removido com sucesso!')