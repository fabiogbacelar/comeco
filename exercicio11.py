



def maiorMenor():
    maior = 0
    menor = 0
    num = 1
    flag = False #valor logico,binario
    while(num != 0 ):
        num = int(input('Informe um numero: '))
        if(num != 0):
            if(flag == False):
            #Primeira vez do codigo. eu instancia a variavel
                maior = num
                menor = num
                flag = True

            #Definir o maior e menor
            if(num > maior):
                maior = num

            if(num < menor):
                menor = num

        return 'Maior: {} \n Menor: {}'.format(maior, menor)