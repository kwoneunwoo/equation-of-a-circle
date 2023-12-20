import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve

##========== Input ==========##
dot_a = -2, 2
dot_b = 4, -6
dot_c = 5, -5

##========== Calculate ==========##
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

circle_center = -A/2, -B/2
circle_radius = (A*A + B*B - 4*C)**(1/2) /2
circle_bang = f'{btfer(A/2, "x").replace(" ", "")}² + {btfer(B/2, "y").replace(" ", "")}² = {int(circle_radius*circle_radius)}'
print(f'원의 중점............: {circle_center}')
print(f'원의 반지름 계산식...: √({int((A*A + B*B - 4*C))}) / 2')
print(f'원의 반지름 숫자.....: {circle_radius}')
print(f'원의 방정식(일반형)..: x² + y² {btfer(A)}x {btfer(B)}y {btfer(C)} = 0')
print(f'원의 방정식(표준형)..: {circle_bang}')


##========== Visualization ==========##
plt.figure(circle_bang) # 창 제목 설정
plt.title(circle_bang) 
plt.axis('equal') # x, y축 비율 동일하게
plt.xlabel('X-axis') # x축 글씨
plt.ylabel('Y-axis') # y축 글씨
plt.axvline(color='dimgray') # x축 선 그리기
plt.axhline(color='dimgray') # y축 선 그리기
plt.grid(True, linestyle='--') # 그리드 생성

#https://www.pythonpool.com/matplotlib-circle/#h-method-2-using-the-equation-of-circle
def drow_circle(center, radius): 
    theta = np.linspace(0, 2 * np.pi, 100)  # 각도 범위를 0부터 2파이까지 100개의 점으로 나눔
    x = center[0] + radius * np.cos(theta)  # x 좌표 계산
    y = center[1] + radius * np.sin(theta)  # y 좌표 계산
    plt.plot(x, y)  # 원을 그림

    plt.text(center[0], center[1], center,
             horizontalalignment='center', verticalalignment='center') # 점 좌표 글씨

def drow_dot(x, y):
    plt.plot(x, y, 'ro') # 점 그리기
    plt.plot([x, x], [0, y], 'r--', linewidth=1.3) #x축으로 점선 그리기
    plt.plot([0, x], [y, y], 'r--', linewidth=1.3) #y축으로 점선 그리기
    plt.text(x+0.1, y+0.1, f'({x}, {y})') # 점 좌표 글씨

drow_circle(center=circle_center, radius=circle_radius)
drow_dot(dot_a[0], dot_a[1])
drow_dot(dot_b[0], dot_b[1])
drow_dot(dot_c[0], dot_c[1])

plt.show() # 좌표 보이기