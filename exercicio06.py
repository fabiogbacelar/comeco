def exercicio06(inicio,fim):
    if(inicio > fim):
        for i in range(inicio,fim,  -1):
            print(i)
    else:
        for i in range(inicio,fim+1):
            print(i)

