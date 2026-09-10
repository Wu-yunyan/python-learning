# 九九乘法表：两层 for，内层范围依赖外层变量
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j} * {i} = {i*j}',end='\t')
#     print()

#打印星号三角形 / 金字塔（练缩进和循环变量关系）
for i in range(1,7):
    print(' '*(6-i)+'*'*(2*i-1))
