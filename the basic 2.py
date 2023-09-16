#运算符1.+2.- 3.* 4./
#关于多分支方面
#简易计算器 code'''isinstance 可以判断一个数是否为一个小数'''
'''num1=float(input("请输入数字"))
num2=float(input("请输入数字"))

print('选择你想要使用的运算方式\n1.加法\t2.减法\t3.乘法\t4.除法\t5.开平方\t6.平方')
char=input('')
while(1):
    if char=='加法':
        print(num1+num2)
        break
    if char=='减法':
        print(num1-num2)
        break
    if char=='乘法':
        print(num1*num2)
        break
    if char=='除法':
        print(num1/num2)
        break
    if char=='开平方':
        print(num1^(1/2))
        print(num2^(1/2))
        break
    if char=='平方':
        print(num1*num1)
        print(num2*num2)
        break
    if char=='退出':
        char1=input('是否确认退出系统\n,\t\tY/N')
        if char1=='Y':
            break
'''
#计算1~100之间的偶数和
'''a=1
sum=0'''
'''注意sum要声明'''
'''while a<=100:
    if a%2==0:#或者用if not bool(a%2):
        sum+=a
    a+=1
'''#for in 遍历循环：range 函数：整数序列 如果不需要用变量，可以用_代替，此时的结构与循环输出类似code：
'''print(sum)

a=str(input('输入'))
for b in a:
    print(b)
for z in range(10):
    print(z)
for _ in range(5):
    print('hello world')
u=0
for n in range(102):#或者用range(1,101):
    if not bool(n%2):
        u+=n
print(u)
'''#//是整除的意思,返回整数 **是幂符号 **n就是几次方
'''
#for 循环输出水仙花数：
for a in range (100,1000):  
    b=a//100
    c=a//10%10
    d=a%10
    if b*b*b+c*c*c+d*d*d==a:
        print('是水仙花数',a)

x=10
print(10**3)
'''
#退出语句：break,退出程序 continue，进入下一个循环
#输出1~50之间所有的倍数
for a in range(0,51):
    if a%5==0:
        print(a)
'''或者'''
b=1
while b<=50:
    b+=1#注意程序的逻辑顺序

    if not bool (b%5):#或者！=：不等于
        print(b)
        continue
#else可以与for in if while一起使用
#嵌套使用：包括了乘法表和其他的一部分例题，树状图中常用 输出矩阵 和 乘法表CODE：
#输出矩阵
for i in range(1,7):#确定其列数
    for j in range(1,9):#确定其行数
        print('*',end='\t')#end=''可以取消其自动换行的功能
    print('')#重新换行
print('********************************************************************************************************************')
#输出直角三角形
for i in range(1,7):#确定其列数
    for j in range(1,9):#确定其行数
        if j<=i:
            print('*',end='\t')#end=''可以取消其自动换行的功能
        continue
    print('')#重新换行
print('*********************************************************************************************************************')
#乘法表
for c in range(1,10):
    for d in range(1,10):
        print(c,'*',d,'=',c*d,end='\t')
    print('')

print('************************************************************************************************************************************')
#消除同样的结果：得到
for c in range(1,10):
    for d in range(1,10):
        if d<=c:#判断
            print(c,'*',d,'=',c*d,end='\t')
        continue#控制循环，break 也类似于此
    print('')

