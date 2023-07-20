from exercicio04 import somarInteiro
from exercicio05 import tabuada
from exercicio05 import coletarPositivo
from exercicio06 import exercicio06
from exercicio07 import impares
from exercicio08 import somarInteiro
from vetores import preencherVetor
from vetores import consultarVetor
from vetores import apagarPosicao
from exercicio09 import somaNumero
from exercicio10 import calcularMedia
from exercicio11 import maiorMenor
from exercicio12 import positivoNegativo
from exercicio13 import fatorial
from exercicio14 import mediaVolei
from exercicio15 import miss
from exercicio16 import eleicao

def mostrarMenu():
    print('\n\n\nEscolha umas das opcões abaixo: ' +
          '\n0. SAIR'         +
          '\n1. Exercicio 01' +
          '\n2. Exercicio 02' +
          '\n3. Exercicio 03' +
          '\n4. Exercicio 04' +
          '\n5. Exercicio 05' +
          '\n6. Exercicio 06' +
          '\n7. Exercicio 07' +
          '\n8. Exercicio 08' +
          '\n9. Exercicio 09' +
          '\n10. Exercicio 10' +
          '\n11. Exercicio 11' +
          '\n12. Exercicio 12' +
          '\n13. Exercicio 13' +
          '\n14. Exercicio 14' +
          '\n15. Exercicio 15' +
          '\n16. Exercicio 16' +
          '\n17. Exercicio 17' +
          '\n18. Exercicio 18' +
          '\n19. Exercicio 19' +
          '\n20. Exercicio 20' +
          '\n21. Preencher Vetor' +
          '\n22. Consultar Vetor' +
          '\n23. Apagar Posição do vetor')

def operacao():
    opcao = 1
    while(opcao != 0):
        #Chamar o metodo de cima
        mostrarMenu()
        #Coletar a opcão do usario
        opcao = int(input('Digita aqui o numero da opção escolhida: '))

        #Executa a ação
        if(opcao == 0):
            #instruções do exercicio
            return
        elif(opcao == 1):
            return
        elif(opcao == 2):
            return
        elif(opcao == 3):
            return
        elif(opcao == 4):
            #Utilizar o exercicio 04
            print('\nExercicio 04')
            print(somarInteiro())
        elif (opcao == 5):
            #Exercicio5
            print('\nExercicio 05')
            num = int(input('Informe o numero'))
            n = coletarPositivo()
            tabuada(num, n)
        elif (opcao == 6):
            # Exercicio06
            print('\nExercicio 06')
            inicio = int(input('Informe o inicio'))
            fim = int(input('informe o fim'))
            exercicio06(inicio, fim)
        elif (opcao == 7):
            #Exercicio7
            print('\nExercicio 07')
            impares()
        elif (opcao == 8):
            #Exercicio8
            print('\nExercicio 08')
            print(somarInteiro())
        elif (opcao == 9):
            #Exercicio9
            print('\nExercicio 09')
            print(somaNumero())
        elif (opcao == 10):
            #Exercicio 10
            print('\nExercicio 10')
            print(calcularMedia())
        elif (opcao == 11):
             #Exercicio 11
            print('\nExercicio 11')
            print(maiorMenor())
        elif (opcao == 12):
            #Exercicio 12
            print('\nExercicio 12')
            print(positivoNegativo())
        elif (opcao == 13):
             #Exercicio
            print('\nExercicio 13')
            num = int(input('informe um mumero: '))
            print(fatorial(num))
        elif (opcao == 14):
            #exercicio14
            print('\nExercicio 14')
            print(mediaVolei)
        elif (opcao == 15):
            #exercicio15
            print('\nExercicio 15')
            print(miss())
        elif (opcao == 16):
            print('\nExercicio16')
            print(eleicao())
        elif (opcao == 17):
            return
        elif (opcao == 18):
            return
        elif (opcao == 19):
            return
        elif (opcao == 20):
            return
        elif(opcao == 21):
            num = int(input('Informe o tamanho do vetor: '))
            preencherVetor(num)
        elif(opcao == 22):
            num = int(input('Informe o tamanho do vetor: '))
            consultarVetor(num)
        elif(opcao ==23):
            posicao = int(input('Informe a posicao que deseja apagar'))
            apagarPosicao(posicao-1)
        else:
            print ('Opcão escolhida nao é valida,digite novamente')