from math import sqrt
from time import sleep
while True:
    a = int(input('Digite o a: '))
    b = int(input('Digite o b: '))
    c = int(input('Digite o c: '))
    print(f'{a}x²+{b}x+{c}')
    delta = (b)**2 - 4*a*c
    print(f'O Delta dessa função é {delta}')
    if delta > 0:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        print(f'Essa função possui como conjunto solução 2 raízes distintas {x1:.2f} e {x2:.2f}')
    elif delta == 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f'Essa função possui apenas uma solução {x1:.2f} ')
    else:
        print('As soluções não pertecem aos reais!!! ')
    keep= ' '
    while keep not in 'SN':
         keep = str(input('Quer continuar? [S/N] ')).upper()[0]
    if keep == 'N':
         break
print('FINISHING')
sleep(2)
print('Volte sempre!!!!!')
