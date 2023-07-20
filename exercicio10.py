



def calcularMedia():
    num = 1
    soma = 0
    contador = 0
    while(num != 0):
        num = int(input('Informe um numero: '))
        if(num % 2 == 0):
            soma += num #somando os pares
            contador += 1 # contando os pares
    return 'A media dos pares digitados é: {}'.format(soma/contador)