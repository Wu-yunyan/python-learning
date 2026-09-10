#D2 2026-09-10 
try:
    score=float(input('请输入你的成绩：（分）'))
except ValueError:
    print('输入格式错误，退出')
else:
    match score:
        case x if x>100 or x<0:
            print('无效输入')
        case x if x >=90:
            print('优秀')
        case x if x>=80:
            print('良好')
        case x if x>=60:
            print('及格')
        case x if x>=0:
            print('不及格')
        case _:
            print('无效输入')

# score=float(input('请输入你的成绩：（分）'))
# if score<0 or score>100:
#     print('无效输入')
# elif 90<=score:
#     print('优秀')
# elif 80<=score:
#     print('良好')
# elif 60<=score:
#     print('及格')
# elif 0<=score:
#     print('不及格')