from math import sqrt, fabs, pow
from os import system


def questao1(m:int):
    xa = 2
    ya = 7
    xb = m
    yb = 2 * m
    xa_xb = xa - xb
    ya_yb = ya - yb 
    d = sqrt(pow(xa - xb, 2) + pow(ya - yb, 2))
    print(f'A(2,7)  B({xb},{yb})')
    print(f'xa - xb = {xa_xb}')
    print(f'ya - yb = {ya_yb}')
    print(f'(xa - xb)^2 = {pow(xa_xb,2)}')
    print(f'(ya - yb)^2 = {pow(ya_yb,2)}')
    print(f'(xa - xb)^2 + (ya - yb)^2 = {pow(xa_xb,2)+pow(ya_yb,2)}')
    print(f'd = {d}')


def questao2(m:int):
    x = 2
    y = m
    modulo = fabs(3 * x + 5 * y - 9)
    d = modulo / (pow(3, 2) + pow(5, 2))
    print(f'd = {d}')
    print(f'd = {modulo} * sqrt(34) / 34')


def questao3a(m:int):
    print('Equação reduzida')
    print(f'y = (-2x+2) / {m}')
    print('Equação segmentária')
    print(f'x + y/(2/{m}) = 1')
    print('Equação paramétrica')
    print(f'x = (t + 2) / 2')
    print(f'x = t / 2 + 1')
    print(f'y = t / {m}')     


def questao3b(m:int):
    print('Equação reduzida')
    print(f'y = ({m}x) / 5 + 2) / {m}')
    print('Equação segmentária')
    print(f'x /(-10/{m}) + y / 2 = 1')
    print('Equação paramétrica')
    print(f'x = (t - 10) / {m}')
    print(f'y = -t / 5')


def questao4(m:int):
    print(f'2x + y -{m} = 0')
    print(f'(0; {m})')
    print(f'({m/2.0}; 0)')


def resolverQuestoes(m:int):
    print('Questao 1')
    questao1(m)
    print('-' * 30)
    print('Questao 2')
    questao2(m)
    print('-' * 30)
    print('Questao 3')
    print('Letra A')
    questao3a(m)
    print('Letra B')
    questao3b(m)
    print('-' * 30)
    print('Questao 4')
    questao4(m)
    print('-' * 30)

    
m = 7
while True:
    m = int(input('Informe o número: '))
    if (m <= 0):
        print('Terminado')
        break;
    system('clear') or None
    resolverQuestoes(m)
