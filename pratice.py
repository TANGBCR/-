#本文件用于python的部分练习

c=input('请输入原始卡号')
d=input('请输入原始密码')
ID=c
password=d
a=1000.23   #余额
ti=0
qu=None #取款金额
cu=None #存款金额
sy=0    #本系统使用次数
print("welcome to the bnak,please choose the vocational work")
while True:
    ID1=input('请输入你的卡号')
    password1=input('请输入你的密码')
    a1=0
    if ID==ID1 and password==password1:
        a1==a
        break
    else:
        sy=sy+1
        if sy>=3:
            print('您已输入三次错误，已锁卡，请联系银行')
            break
        else:
            print('输入有误，请再次输入')
            continue

while True:
    '''
    存款
    取款
    退卡
    '''
    ti=input('请输入你想办理的业务类型')

    if ti=="取款":
        qu=float(input('请输入取款金额'))
        if qu>=1000.23:
            print('余额不足')
            continue
        else:
            a1=a-qu
            print('你取出',qu,'元，余额还有',a1)
            continue

    if ti=='存款':
        cu=int(input('请输入存款金额'))
        if cu<=1:
            print('存款金额不能低于1元')
        else:
            a1=a+cu
            print('你存入',cu,'元,现有金额',a1,'元')
    elif ti=='退卡':
        print('感谢您的使用，请拿好你的卡')
        break
    else:
        print('输入有误，请再次输入')
        continue



