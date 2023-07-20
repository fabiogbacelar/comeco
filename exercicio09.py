def somaNumero():
    num = 1
    soma = 0
    while(num != 0):
        num = int(input('Informe um numero: '))
        soma += num
    return ' A soma dos numeros digitados é: {}'.format(soma)

