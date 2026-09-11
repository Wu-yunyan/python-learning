# 输入一个密码，检查它是否满足：

# 长度 ≥ 8
# 至少含 1 个数字
# 至少含 1 个大写字母
# 至少含 1 个特殊字符（如 !@#$%）
# 全部满足 → 输出「强」；满足 2–3 条 → 「中」；否则「弱」，并列出缺了哪几条。

specials = '!@#$%^&*()-_=+[]{};:,.<>?/'
password=input("设置密码：")
has_digit = 0
has_upper = 0
has_special = 0
long_enough = 0


if len(password)>=8:
    long_enough =1
else:
    print('你的密码长度小于8')

for i in password:
    if i.isdigit():
        has_digit =1
    if i.isupper():
        has_upper =1
    if i in specials:
        has_special =1

if has_digit ==0:
    print('你的密码没有数字')
if has_upper ==0:
    print('你的密码没有大写字母')
if has_special ==0:
    print('你的密码没有特殊字符')

flag=has_digit+has_upper+has_special+long_enough

if flag==4:
    print('密码强度：强')
elif flag>=2:
    print('密码强度：中')
else:
    print('密码强度：弱')

