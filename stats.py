def average(scores):
    # 自己写：用 for 累加，再除以 len(scores)
    total=0
    for s in scores:
        total +=s
    
    return total/len(scores)
   
def highest(scores):
    # 自己写：用 for 找最大值（不许用 max()，先手写一遍）
    h=scores[0]
    for s in scores:
        if s>h:
            h=s
    return h

scores = [90, 85, 77, 60, 92]
print(f'平均分：{average(scores)}')
print(f'最高分：{highest(scores)}')