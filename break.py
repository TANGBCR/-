#密码的应用及录入
'''输入三次便退出'''
password='1234567'

for b in range(3):
    a=input("请输入密码")
    if password==a:
        print('密码正确')
        break
    else:
        print('密码错误')
print('已经错误三次，无法再次输入')

