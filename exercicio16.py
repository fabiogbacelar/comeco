





def coletarPositivoInteiro():
    num = int(input)
    while(num <= 0):
        print('Erro!! informe um valor positivo')
        num = int(input('informe um numero: '))
    return num

def transformarPercentual(num, total):
    percentual = (num/ total) * 100
    return percentual


def eleicao():
    print('informe o total de votos brancos: ')
    brancos = coletarPositivoInteiro()
    print('informe o total de votos nulos: ')
    nulos   = coletarPositivoInteiro()
    print('informe o total de validos: ')
    validos = coletarPositivoInteiro()
    print ('informe o total de eleitores: ')
    total   = coletarPositivoInteiro()
    #Verificar se o total é igual a brancos,validos e nulos
    if((brancos+nulos+validos) == total):
        pBrancos = transformarPercentual(brancos,total)
        pNulos   = transformarPercentual(nulos,brancos)
        pValidos = transformarPercentual(validos,total)
        return 'Votos Brancos: {}%\nVotos Nulos: {}%\nVotos Validos: {}%'.format.(pBrancos,pNulos,pValidos)
    else:
        return 'Numeros de brancos,validos e nulos e diferente do total de eleitores'