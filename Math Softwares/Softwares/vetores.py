import math
from time import sleep
while True:
    print('''[1] Para vetores no PLANO
[2] Para vetores no ESPAÇO''')
    res = int(input('Qual a sua escolha? '))
    if res == 1:
        v1x = float(input('Digite o Valor de X para o Primeiro vetor: '))
        v1y = float(input('Digite o Valor de Y para o Primeiro vetor: '))
        v2x = float(input('Digite o Valor de X para o Segundo vetor: '))
        v2y = float(input('Digite o Valor de Y para o Segundo vetor: '))
        modv1 = math.sqrt(v1x**2 + v1y**2)
        print(modv1)
        modv2 = math.sqrt(v2x**2 + v2y**2)
        print(modv2)
        mot = modv1 * modv2
        mv = v1x*v2x + v1y*v2y
        print(mv)
        cosseno =  mv/mot
        print(cosseno)
        coss = math.acos(cosseno)
        print(f'O Ângulo formado por esses 2 vetores é {math.degrees(coss):.1f}')
    elif res == 2:
        v1x = float(input('Digite o Valor de X para o Primeiro vetor: '))
        v1y = float(input('Digite o Valor de Y para o Primeiro vetor: '))
        v1z = float(input('Digite o Valor de Z para o Primeiro vetor: '))
        v2x = float(input('Digite o Valor de X para o Segundo vetor: '))
        v2y = float(input('Digite o Valor de Y para o Segundo vetor: '))
        v2z = float(input('Digite o Valor de Z para o Segundo vetor: '))
        modv1 = math.sqrt(v1x ** 2 + v1y ** 2 + v1z ** 2)
        print(modv1)
        modv2 = math.sqrt(v2x ** 2 + v2y ** 2 + v2z ** 2)
        print(modv2)
        mot = modv1 * modv2
        mv = v1x * v2x + v1y * v2y + v1z * v2z
        print(mv)
        cosseno = mv / mot
        print(cosseno)
        coss = math.acos(cosseno)
        print(f'O Ângulo formado por esses 2 vetores é {math.degrees(coss):.1f}')
    else:
        print('TENTATIVA ÍNVALIDA TENTE NOVAMENTE!!')
    con = ' '
    while con not in 'SN':
        con = str(input('Quer continuar? [S/N] ')).upper()[0]
    if con == 'N':
        break
print('Foi bom tem a sua companhia!')
print('ENCERRANDO.....')
sleep(3)
print('ATÉ MAIS... ')
