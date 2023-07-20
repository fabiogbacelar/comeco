






def validacaoNotas():
    nota = float(input('Informe uma nota: '))
    while((nota < 0) or(nota >10)):
        print('Erro!! Informe uma nota entre 0 e 10')
        nota = float(input('informe uma nota: '))
    return nota

def miss():
    nomeVencedora = ''
    notaVencedora = 0
    for i in range(1,17):
        nome = input('Informe o nome da {} candidata: '.format(i))
        nota = validacaoNotas()#numeros com virgula e nao negativos
        #Verificacao da vencedora
        if(nota > notaVencedora):
            notaVencedora = nota
            nomeVencedora = nome
    return 'Vencedora: {}\nNota: {}'.format(nomeVencedora, notaVencedora)

