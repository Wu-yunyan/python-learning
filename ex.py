word = input("输入一个英文单词：")
print(f"它有 {len(word)} 个字母")
print(f"大写：{word.upper()}")
print(f"小写：{word.lower()}")
print(f"首字母：{word[0]}")
print(f"尾字母：{word[-1]}")


s = '  Hello,  Security  '

# 第一组：改样子
print(len(s))                      # 20   长度（含空格）
print(s.upper())                   # HELLO, SECURITY
print(s.strip())                   # Hello, Security   ← 去掉了首尾空格
i=s.strip()
print(len(i))                   
print(s.replace('Security', 'World'))

# 第二组：切开 / 拼回
line = '2026-09-10,FAILED,admin,192.168.1.5'
parts = line.split(',')
print(parts)                       # ['2026-09-10', 'FAILED', 'admin', '192.168.1.5']
print(parts[2])                    # admin       ← 取出第3个字段
print(' | '.join(parts))           # 2026-09-10 | FAILED | admin | ...

# 第三组：查找 / 判断
print(line.find('admin'))          # 18    找到给下标
print(line.find('xyz'))            # -1    找不到给 -1（不报错！）
print(line.startswith('2026'))     # True
print(line.endswith('5'))          # True
