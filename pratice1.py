#交换两个整数的值
a=1
b=2
a,b=b,a
print(a,b)
#查找对象的内存
import sys
slogan='where'
size=sys.getsizeof(slogan)
print('size=',size)
#反转字符串
frist='how good day toady is'
seconed=frist[::-1]
print(seconed)
