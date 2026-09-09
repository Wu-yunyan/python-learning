#写 info.py——用 input() 让用户输入姓名和年龄，打印「你好，XX，你明年 N+1 岁」（用到变量、int()、f-string）
name=input("请输入姓名：")
age=input("请输入年龄：")
print(f'你好，{name},你明年{int(age)+1}岁')
print(f'你好，{name}，你今年{age}岁，明年就{int(age)+1}岁了')
