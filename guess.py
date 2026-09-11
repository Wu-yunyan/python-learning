# 程序随机生成一个 1–100 的整数
# 玩家反复输入猜测，程序提示「大了」或「小了」
# 最多猜 7 次：
#   第 7 次内猜中 → 「恭喜，第 N 次猜中！」
#   7 次用完没中 → 「游戏结束，答案是 XX」

# import random

# num=random.randint(1, 100)
# i=1
# while (1):
#     guess=int(input("请输入你所猜的数字(1-100)："))
#     if num>guess:
#         print('猜小了')
#     elif num<guess:
#         print('猜大了')
#     else:
#         print(f'猜对了,恭喜第{i}次猜中')
#         break
#     if i==7:
#         print(f'游戏结束，答案是{num}')
#         break
#     i+=1

import random


num = random.randint(1, 100)

try:
    for i in range(1, 8):                   # 第 1 到第 7 次
        guess = int(input("请输入你要猜的数字(1-100)："))
        if num > guess:
            print('猜小了')
        elif num < guess:
            print('猜大了')
        else:
            print(f'猜对了，恭喜第{i}次猜中')
            break
    else:                                   # 7 次全错、循环自然跑完 → 到这里
        print(f'游戏结束，答案是{num}')

except ValueError:
    print('输入类型错误,游戏结束')

input('\n按回车键退出...')
