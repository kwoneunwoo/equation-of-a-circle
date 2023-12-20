# https://mathbang.net/455#gsc.tab=0
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

print(f'원의 중점............: ({-A/2}, {-B/2})')
print(f'원의 반지름 계산식...: √({int((A*A + B*B - 4*C))}) / 2')
print(f'원의 반지름 숫자.....: {(A*A + B*B - 4*C)**(1/2) /2}')
print(f'원의 방정식(일반형)..: x² + y² + ({A})x + ({B})y + ({C}) = 0')
print(f'원의 방정식(표준형)..: (x-({-A/2}))² + (y-({-B/2}))² = \
{int(((A*A + B*B - 4*C)**(1/2) /2)*((A*A + B*B - 4*C)**(1/2) /2))}')    