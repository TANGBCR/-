'''this one is aimed at revive what I learn during past year'''
import keyword

'''the first'''
print('')
print("")
# 例如直接输出结果类型可以用
'''for example'''
print('hello world')
print("hello world")
print(9 + 1)
'''将数据直接输出至文件中'''
a1 = open('C:/Users/T/Desktop/revive.txt', 'w+')
z = 9 + 1
print(z, file=a1)
a1.close()
'''注解：
一.总结

a：附加写，不可读。
a+：附加读写。追加写。

r：只读，最常用。不创建，不存在会报错。（读二进制文件可能会读取不全）
rb：只读。二进制文件按二进制位进行读取。不创建，不存在会报错。
rt：只读。文本文件用二进制读取。不创建，不存在会报错。
r+：可读写。覆盖写。不创建，不存在会报错。

w：只写。存在则覆盖。不存在则创建。
w+：可读写。存在则覆盖。不存在则创建。

二.区分

r只读，r+读写，不创建，即需要事先存在一个文件以供读/读写，若不存在文件会报错

w新建只写，w+新建读写，二者都会将文件内容清零，即事先不需要有该文件存在，若已经存在则会覆盖（以w方式打开，不能读出。w+可读写）

w+与r+区别：
r+：可读可写，若文件不存在，报错
w+: 可读可写，若文件不存在，创建

r+与a+区别：
r+：覆盖写
a+：追加写

示例：

f = open("1.txt",'w+')
f.write('123')
f = open("1.txt",'r+')
f.write('456')
f = open("1.txt",'a+')
f.write('789')
1
2
3
4
5
6
输出：456789

以a,a+的方式打开文件，附加方式打开
以 ‘U’ 标志打开文件, 所有的行分割符通过 Python 的输入方法(例#如 read*() )，返回时都会被替换为换行符\n. (‘rU’ 模式也支持 ‘rb’ 选项) .
r和U要求文件必须存在
不可读的打开方式：w和a

若不存在会创建新文件的打开方式：a，a+，w，w+

使用’r’一般情况下最常用的，但是在进行读取二进制文件时，可能会出现文档读取不全的现象；
使用’rb’按照二进制位进行读取的，不会将读取的字节转换成字符，二进制文件用二进制读取用’rb’ ；
rt模式下，python在读取文本时会自动把\r\n转换成\n，文本文件用二进制读取用‘rt’；
————————————————
版权声明：本文为CSDN博主「腾v」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_42670502/article/details/113486856'''
'''the seconed'''
'''转义字符'''
'''注意：\t的意思就是在四格一的位置中将没有使用的格输出到下面的四个空格
\n的意思就是换行
\'的意思就是转移字符，表示’不是该行语句的终点
\\只会输出一个\，如果想要输出两个\\（反字符），则需要写出\\\
原字符：如果不希望字符串中的转义字符起作用，则在原字符串之前加上r或者R（最后不能是反字符）
'''
'''示范代码'''
print('hello\nworld')
print('hello\tworld')
print('hellotcr\tworld')
print('hello\\world')
print('hello\\\world')
print( r'hello\nworld')
'''注意不能用保留词来给文件起名'''
#保留词有
print(keyword.kwlist)
#变量
#示范代码
name='唐烨'
print(name)
print(type(name))
print(id(name))
#多次赋值后的情况
name1='starpop'
name1='oil'
print(name1)#会被覆盖
#变量的类型1.int 2.float 3.bool 4.str///整数类型，浮点数类型，布尔类型，字符类型
#int类型//整数类型
jie=15678.567
a=int(jie)
print(a)
#BOOL 表达了两种情况1.true 2.false
a=11<18
print(bool(a))
#数据类型的转换
#input()输入函数//可以进行变量的转换
'''结构：变量+=+input（‘内容’）'''
C=int(input('数字一'))
B=int(input('数字二'))
print('数字一加数字二的结果为',B+C)
#注意如果没有加变量的类型，则
C1=input('数字一')
B2=input('数字二')
print('数字一加数字二的结果为',B2+C1)