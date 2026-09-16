# 读一个 .txt，统计每个词出现次数（字典计数）
# 练手 str.split()、.lower()、字典 d[w] = d.get(w,0)+1

d={}
with open ('para.txt','r',encoding='utf-8') as f:
    for line in f:
        line=line.replace('，', ' ').replace('.', ' ').split()
        for word in line:
            word=word.lower()
            d[word]=d.get(word,0)+1


# for word,freq in d.items():
#     print(f'{word},{freq}次')

for word,freq in sorted(d.items(),key=lambda pair:pair[1],reverse=True)[:3]:
    print(f'{word},{freq}次')