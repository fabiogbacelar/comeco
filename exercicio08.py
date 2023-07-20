def somarInteiro():
    soma = 0
    for i in range(1,11,1):
        num = int(input('{} numero: '.format(i)))
        soma += num
    return 'A soma dos numeros digitados foi {} '.format(soma)