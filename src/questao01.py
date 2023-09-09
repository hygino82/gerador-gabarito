from math import sqrt, pi,fabs

r = 5
h = 3
g = sqrt(r * r + h * h)
sb = pi * r * r
sl = pi * r * g
st = sb + sl
v = sb * h / 3.0

print(f'r = {r:.4f}')
print(f'h = {h:.4f}')
print(f'g = {g:.4f}')
print(f'sb = {sb:.4f}')
print(f'sl = {sl:.4f}')
print(f'st = {st:.4f}')
print(f'v = {v:.4f}')
print(f'f = {fabs(-7.54)}')