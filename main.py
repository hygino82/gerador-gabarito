def letra_a(t: int):
    print('LETRA A')
    x = (8 - 3 * t) / 5.0
    print(f'3*x + {3 * t} +2*x -8 = 0')
    print(f'5*x = {8 - 3 * t}')
    print(f'x = {x}')
    print(30 * '-')


def letra_b(t: int):
    print('LETRA B')
    x = (4 * t + 50) / 20.0
    print(f'(10*x -25) * 2 = {4 * t}')
    print(f'20*x -50 = {4 * t}')
    print(f'20 * x = {4 * t + 50}')
    print(f'x = {x}')
    print(30 * '-')


def letra_c(t: int):
    print('LETRA C')
    x = (256 - t) / 4.0
    print(f'4*x + {t} = 16^2')
    print(f'4*x = 256 - {t}')
    print(f'4*x = {256 - t}')
    print(f'x = {x}')
    print(30 * '-')


def letra_d(t: int):
    print('LETRA D')
    x = (125 + t) / 5.0
    print(f'5*x - {t} = 5^3')
    print(f'5*x - {t} = 125')
    print(f'5*x = {t + 125}')
    print(f'x = {x}')
    print(30 * '-')


def letra_e(t: int):
    print('LETRA E')
    print(f'(3*x -7) / 4 = 15 - {t}')
    print(f'3*x -7 = 4 * {15 - t}')
    print(f'3*x  = {4 * (15 - t)} + 7')
    print(f'3*x  = {4 * (15 - t) + 7}')
    x = (4 * (15 - t) + 7) / 3.0
    print(f'x = {x}')
    print(30 * '-')


def letra_f(t: int):
    print('LETRA F')
    print(f'40 * (5*x + 1) = {t}')
    print(f'200*x + 40 = {t}')
    print(f'200*x = {t} - 40')
    print(f'200*x = {t - 40}')
    print(f'x = {t - 40} / 200')
    x = (t - 40) / 200.0
    print(f'x = {x}')
    print(30 * '-')


def letra_g(t: int):
    print('LETRA G')
    print(f'2*(4 - x) = 100 + {t}')
    print(f'8 - 2*x = {100 + t}')
    print(f'-2*x = {100 + t} - 8')
    print(f'-2*x = {100 + t - 8}')
    print(f'x = {100 + t - 8} / (-2)')
    x = -(100 + t - 8) / 2.0
    print(f'x = {x}')
    print(30 * '-')


def letra_h(t: int):
    print('LETRA G')
    print(f'7*x - 5*x = {t} + 3')
    print(f'2*x = {t + 3}')
    print(f'x = {t + 3} / 2')
    x = (t + 3) / 2.0
    print(f'x = {x}')
    print(30 * '-')


while True:
    numero = int(input('Informe o número do aluno -> '))
    if 0 < numero and 50 < numero:
        break
    letra_a(numero)
    letra_b(numero)
    letra_c(numero)
    letra_c(numero)
    letra_e(numero)
    letra_f(numero)
    letra_g(numero)
    letra_h(numero)


print('FIM DO PROGRAMA')