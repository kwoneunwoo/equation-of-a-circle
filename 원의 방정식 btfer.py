from sympy import symbols, solve

dot_a = -2, 2
dot_b = 4, -6
dot_c = 5, -5

#계산식: x^2 + y^2 + Ax + By + C = 0
A, B, C = symbols('a, b, c')
ans = solve([
    dot_a[0]*dot_a[0] + dot_a[1]*dot_a[1] + A*dot_a[0] + B*dot_a[1] + C,
    dot_b[0]*dot_b[0] + dot_b[1]*dot_b[1] + A*dot_b[0] + B*dot_b[1] + C,
    dot_c[0]*dot_c[0] + dot_c[1]*dot_c[1] + A*dot_c[0] + B*dot_c[1] + C
])
A, B, C = ans[A], ans[B], ans[C]

def btfer(num, char:str = None):
    if char != None:
        if num == 0: return char
        else: return f'({char} {btfer(num=num)})'
    else:
        if num < 0: return f'- {-num}'
        elif num > 0: return f'+ {num}'
        else: return '' 

#def btfer(num):
#    if num < 0: return f'- {-num}'
#    elif num > 0: return f'+ {num}'
#    else: return ''

circle_center = -A/2, -B/2
circle_radius = (A*A + B*B - 4*C)**(1/2) /2
circle_bang = f'{btfer(A/2, "x").replace(" ", "")}^2 + {btfer(B/2, "y").replace(" ", "")}^2 = {int(circle_radius*circle_radius)}'
print(f'원의 중점............: {circle_center}')
print(f'원의 반지름 계산식...: √({int((A*A + B*B - 4*C))}) / 2')
print(f'원의 반지름 숫자.....: {circle_radius}')
print(f'원의 방정식(일반형)..: x^2 + y^2 {btfer(A)}x {btfer(B)}y {btfer(C)} = 0')
print(f'원의 방정식(표준형)..: {circle_bang}')