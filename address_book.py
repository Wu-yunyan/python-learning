# 用字典存联系人 {姓名: 电话}
# 支持：添加（写入字典+存文件）、查询（按姓名查电话）、显示全部
# 持久化：每次改动后把字典写回 contacts.txt，下次启动能读回来

def save(contacts):
    with open('contacts.txt', 'w', encoding='utf-8') as f:
        for name, phone in contacts.items():
            f.write(f'{name},{phone}\n')

def load():
    contacts = {}
    try:
        with open('contacts.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()             # 去掉行尾换行
                if not line:                    # 跳过空行
                    continue
                name, phone = line.split(',')   # 按逗号拆成两半
                contacts[name] = phone
    except FileNotFoundError:
        pass          # 第一次运行还没这个文件 → 就用空字典
    return contacts


contacts =load()      # 从文件读回字典
while True:
    cmd = input('1加 2查 3列表 4删除 0退出：')
    if cmd == '1':
        name=input('请输入要添加的姓名:')
        number=input('请添加其联系方式：').strip()
        contacts[name]=number
        print(f'添加成功，{name}:{contacts[name]}')
    elif cmd == '2':
        name1=input('请输入要查询的姓名：')
        print(contacts.get(name1,'用户不存在'))
    elif cmd == '3':
        for n,m in contacts.items():
            print(f'姓名：{n},电话：{m}')
    elif cmd == '4':
        name2=input('请输入要删除的姓名:')
        # print(f'查找用户：{contacts.get(name2,'用户不存在')}')
        if contacts.get(name2) != None:
            del contacts[name2]
            print('已删除该用户')
        else:
            print('用户不存在')
    elif cmd == '0': 
        save(contacts)
        break
    else:
        print('无此命令，请输入 1加/2查/3列表/4删除/0退出')
