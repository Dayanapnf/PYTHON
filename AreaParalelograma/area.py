def calculadoradaarea(base, altura):

    area = (base * altura)
    print("O valor da área do paralelograma é: ", area)


op = 0

while op != '1':
    print('--------------------------------------------------')
    print('                SEJA BEM-VINDO!')
    print('        Calculador de Área de Paralelogramo       ')
    print('--------------------------------------------------')
    print('Insira o comprimento da base:')
    base = int(input())
    print('--------------------------------------------------')
    print('Insira a altura:                                  ')
    altura = int(input())
    print('--------------------------------------------------')
    calculadoradaarea(base, altura)
    print('--------------------------------------------------')
    print('            PRECIONE "1" PARA SAIR                ')
    print('                     OU                           ')
    print('          PRECIONE "2" PARA CONTINUAR             ')
    print('--------------------------------------------------')
    op = (input())
