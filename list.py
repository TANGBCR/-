#针对python里的列表函数进行的演习？
a=0
u=['good morning','Mr.s tang',93]
print(u)
'''
第二种方式进行输出
'''
u1=list(['good morning','Mr.s tang',93])
print(u1)
u1.append(3)
print(u1)
u2=[1,2,3]
u1.extend(u2)
print(u1)
u1.insert(3,u2)
'''
list函数的可用函数测试
'''
test=[1,2,3,4]
'''#remove函数,去除函数，按照你所给的数字进行去除
test.remove(1)
print(test)'''
#pop函数
'''test.pop(-3)
print(test)'''
#index函数
'''if 6 in test:
    print('yes')
else:
    print('no')'''
#切片函数：原来的list函数加上[::]详细见底下
'''print(test[1:3:1])'''
#del函数与clear函数,以及部分前面所学的部分实践
try1=[1,2,3,5,6,8,7,6]
#切片类
try2=try1[1:3]=[]
print(try2)
print(try1)

try3=[123,3452,4231,234,231,423,7,1,35,2,4]
try3.sort()
print(try3)
New_try=sorted(try1,reverse=False)
print(New_try)