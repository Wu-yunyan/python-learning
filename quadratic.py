import math

def quadratic(a,b,c):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError('bad operand type')
    if a==0:
        raise ValueError('方程不是二元一次方程')
        return
    d=b*b-4*a*c
    if d<0:
        raise ValueError('方程无实数解')
        return
    
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    return x1,x2

a=float(input('输入方程参数a:'))
b=float(input('输入方程参数b:'))
c=float(input('输入方程参数c:'))

try:
    x1,x2=quadratic(a,b,c)
    print(f'方程的解是：{x1}，{x2}')
except ValueError as e:
    print(e)



# print('quadratic(2,3,1)=',quadratic(2,3,1))
# print(f'quadratic(1,3,-4)={quadratic(1,3,-4)}')

# if quadratic(2,3,1) !=(-0.5,-1.0):
#     print('测试失败')
# elif quadratic(1,3,-4) !=(1.0,-4.0):
#     print('测试失败')
# else:
#     print('测试成功')