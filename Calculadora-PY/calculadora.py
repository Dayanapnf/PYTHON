
def calculosoma():
    num1=float(input('Digite o número 1:'))
    num2=float(input ('Digite o número 2:'))
    return soma(num1,num2)


def calculosub():
    num1=float(input('Digite o número 1:'))
    num2=float(input ('Digite o número 2:'))
    return sub(num1,num2)

def calculomult():
    num1=float(input('Digite o número 1:'))
    num2=float(input ('Digite o número 2:'))
    return mult(num1,num2)

def calculodiv():
    num1=float(input('Digite o número 1:'))
    num2=float(input ('Digite o número 2:'))
    return div(num1,num2)
    

def soma(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1*num2


def div(num1, num2):
    return num1/num2


def calculadora(op):
    
    if (op == '1'):
        a=calculosoma()
        print('Resultado:', a)
        
    elif (op == '2'):
        a=calculosub()
        print('Resultado:', a)

    elif(op == '3'):
        a=calculomult()
        print('Resultado:', a)
    elif (op == '4' ):
        a=calculodiv()
        print('Resultado:', a)
    else:
        if(op != '5'):
            print('Opção invalida!')


op=0

while op != '5':
    print('--------------------------------------------------')
    print('                SEJA BEM-VINDO!')
    print('             Calculadora em PYTHON')
    print('--------------------------------------------------')
    print('Digite umas das opções:')
    print('--------------------------------------------------')
    print('1- SOMA')
    print('2- SUBTRAÇÃO')
    print('3- MULTIPLICAÇÃO')
    print('4- DIVISÃO')
    print('5- SAIR')
    op = (input())
    calculadora(op)
