
def positivoNegativo():
    soma = 0
    contarNegativo = 0
    for i in range(20):
        num = int(input('{} numero: '.format(i+1)))
        #a. soma dos positivos
        if(num > 0):
            soma += num
            #b.contando os negativos
        elif(num < 0):
            contarNegativo += 1
    return 'Positivos: {} \nContar Negativos: {}'.format(soma,contarNegativo)