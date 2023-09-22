# 列表————与C中的数组类似，有序存储数据，能够映射数据（唯一？），可以重复存储数据，可以存储不同类型的数据且能够CODE
# 如果想创建列表，使用[]，或者是内置函数list()
# CODE
'''
c=['唐某人','18','你好']#其位置状态0，1，2
b=list(['唐某人','18','你好'])
print(c)
print(b)
print(type(c))
print(type(b))
print(c[1],'\n',c[0])#notice: need use the [] to get the data
print(id(c))
print(id(b))
c=['唐某人','18','你好','hello world']
print(c)'''  # 验证了列表能够加入数据
# 可以通过indec()函数来获取列表的索引，即数据的位置
'''print(c.index('18'))'''
# 但是不能查询不存在于列表的数据，不然会报错
# 或者用
'''print(c[-3],c[2])'''
# 直接写位置
# 如果要获取列表中的多个数据
'''切片操作'''
# 结构【start:stop:step】
'''a=[1,2,3,34,5,67,8,96,54,313,4353,5]'''
'''print(a[1:7:1])'''  # step 其间隔距离，默认为一（就是没有写的后果）
# 负数则与其相反，从后往前切片
'''print(a[-1:-7:-1])
print(a[::-1])
print(a[-1::1])'''
# 判断用in ,依次输出数据用for in 函数
'''print(10 in a)
for u in a:
    print(u,end='\t')'''
'''a=[1,2,3,4,5,6,7]
for a1 in a:
    print(a1,end='\t')
print('')
a.append(8)#不能加多个数字，会报错
print(a)#id不变
a.extend([9,10,11])#添加不止一个元素,但是是另一个列表中的
print(a)
#a.insert(位置，数据)
a.insert(2,114514)
print(a)
#切片操作
a2=[1,2,41,2]#可以添加多个元素
a[1:]=a2
print(a)
print(a2)
'''
'''
#列表的删除操作remove(),pop(),切片操作，clear(),del
a=[1,2,3,4,5,6,7,89,0]
a.remove(7)
a.pop(0)
a1=a[2:]
print(a1)#用a[1:N]=[]便可以确认删除切片内容
a.clear()
print(a)
del a1
print(a1)#a1被删除，a1不再存在x
'''
'''a=[1,2,3,5,6,3]
#进行修改
a[2]=9#将位置为二的地方进行修改，把3--》9
print(a)
a[1:3]=[8,10]#将位置为1，2的地方进行替换
print(a)
'''
# 也可以这样子：a[1：3]=[n1,n2,n3,n4.....n**n]
# 从而进行加入元素的操作
# 用sort函数将列表中的函数进行排序，
# reverse能够将顺序调整为降序和正序
# code:
'''
a=[2,4.1,4,62,3,51324234,54315637.4564,253246356,5624652,234134]#纯粹是乱打的
print(a)#原来的列表
a.sort()
print(a)#排序以后的列表
a.sort(reverse=True)
print(a)#倒序状态，reverse=True表示的为倒序状态，故：reverse=false为正序状态
print('....................................内置函数sorted...........................................')
b=[2,4.1,4,62,3,51324234,54315637.4564,253246356,5624652,234134]
print(b)#原来的函数
c=sorted(b)#产生一个新列表
print(c)
print(b)#原列表不变
#也可以用这个
c1=sorted(b,reverse=True)
C2=sorted(b,reverse=False)
print(C2)
print(c1)
print(b)'''
# 列表生成式：【i for I in range(10)】
# code
'''r1=[i for i in range(10)] 
print(r1)'''
# 为啥不用print(r1=[i for i in range(10)]
'''print(r2=[i for i in range(10)])'''  # 会报错
# 第一个i可以将其转化为不同的算式
# code
'''c1=[i**i for i in range(11)]#**幂乘
print(c1)'''
# 字典：先存储数据，再而通过hash函数计算位置
# 创建字典，1.通过花括号2.通过dict函数
# cod
'''
s1={'name':'唐某人' ,'age':18,'height':175}
print(s1)
print(type(s1))
s2=dict({'name':'唐某人','age':18,'height':175})
print(s2)#这种通常不用，过于麻烦
s3=dict(name='唐某人',age=18,height=175)
print(s3)#中文属于字符串的一种，故要加上''
#空字典————
s4={}
print(s4)
print('.................................获取字典中的元素...............................')
#注意：如果想获取字典中的元素，则使用1.[]2..get[],个人推荐用后面的，至少不会报错
# code
print(s1['name'])
print(s1['age'])
#print(s1['like'])#查找不存在与dict中的元素时会报错
#因此使用第二种说法
print(s1.get('name'))
print(s1.get('age'))
print(s1.get('like'))#只会输出一个NONE的空值，不会报错
#in/not in 是对元素是否存在于字典中进行的判断
#del,clear是对字典中的元素进行删除,输出布尔值
#code:
print('like' in s1)
print('like' not in s1)
del s1['name']#所以为什么要把这个转化为列表在删除？？
print(s1)
s2.clear()
print(s2)
#如果想要增加元素，则：
#code
s1['like']='music'
print(s1)
#字典的结构为{keys:value,.....}
#因此
u1=s1.keys()
u2=s1.values()
print(u1)
print(u2)
print(list(s3))#将字典转化为列表
#字典元素的遍历#for  in
for u3 in s1:
    print(u3)

    print(u3,s1.get(u3))#输出字典中的值
'''
'''
# 注意，字典的本质为keys-value对
# 但是keys(关键词）不允许重复，value允许重复

# code
s1 = {'name': '唐某人', 'age': 18, 'height': 175, 'name': '唐烨'}  # 重复的会被覆盖
print(s1)
# 注意，字典的内存浪费极大
s1 = {'name': '唐某人', 'age': 18, 'height': 175, 'name1': '唐某人'}
print(s1)
# 将两个不同的列表变成一个字典————zip()函数
r1 = ['name', 'age', 'height', 'strength']
r2 = ['唐某人', 18, 175, 100]
# s2=zip(r1,r2)

# print(s2)#直接写会变成地址
# 字典生成式：{item.upper:value for keys,value in zip(keys,values)}
# 没什么好讲的，直接看代码
s2 = {r1: r2 for r1, r2 in zip(r1, r2)}
print(s2)
s3 = {r1.upper(): r2 for r1, r2 in zip(r1, r2)}  # 加入Upper变为大写
print(s3)  # ctrl+shift+alt+L能让代码看起来更舒服
'''
# 元组
# 元组是一个不可变的序列，而列表与字典是可变序列，故
# 元组不能变,与字符串相似
# 这点是以内存地址是否变化来确定的，同时以是否能进行增删改的操作进行
# code
'''
l1 = [1, 2, 3, 5, 63, 245, 6]
print(id(l1))
l1.append(23)
print(l1)
print(id(l1))

s1 = {'name': '唐某人', 'age': 18, 'height': 175}
print(id(s1))
s1['like'] = 'music'
print(id(s1))

c1 = 'hello'
print(id(c1))
c1 = c1 + '  world'
print(id(c1))
print(c1)

t1 = (1, 2, 45, 62, 12, 4)  # 元组
# 创建方式有两种：第一种：t2=(),第二种：用内置函数tuple()
# 只包含一个元素的元组需要使用小括号和逗号
# creat a tuple
# 1
t2 = (1, 2, 34, 5, 'hello world')
print(t2)
print(type(t2))
t3 = tuple((1, 2, 3, 41323, 421, 'hello world'))
print(t3)
print(type(t3))
t4 = ('hello world',)
print(t4, '\t', type(t4))
# creat a empty tuple
# creat a empty list
# creat a empty dict
t = ()
t5 = tuple()

l = []
l1 = list()

d = {}
d1 = dict()
print(type(t), '\t', type(t5))
print(type(l), '\t', type(l1))
print(type(d), '\t', type(d1))
'''
# 一个小小的想法#失败：注：这是尝试对字典的直接生成，将先前生成的数据直接导入字典中:仍要尝试
'''a=int(input('请输入数字'))
while a<=100:#用int/str
    if a<=20:
        a+=1
        continue
    if 20<a<=50:
        a*=2
        print(a)
        continue
    elif 50<a<=100:
        a**=a
        print(a)
        continue
    else:
        print(a)
        break
        '''
'''if a>100:
    b=str(input('录入字符'))#能不能让这个的数量能够判断？
    f=(input('输入数字'))#在这里进行创建一个字典
    r1={b.upper(): f for b,f in zip(b,f)}
    print(r1)
'''  # 没有办法进行对字典的理想化生成
# 元组的笔记：元组可以存储其他的几种东西：列表，字典，数字，字符，存储的数据结构类型不变，但是其内容可以变
# 个人对元组的一些猜想 ：元组的本质是确定一个固定的内存地址，从而保证它内存空间的完整与不可变性
# 如：
'''t1 = (18, 'hello world', [1, 2, 4, 5], {'name': '唐某人', 'age': 18, 'height': 175})
print(t1)
print(type(t1), '\n', type(t1[0]), '\t', type(t1[1]), '\n', type(t1[2]), '\n', type(t1[3]))
# 进行修改：
# t1[2]=t1[2].append(6)#不能这样改
t1[2].append(10)  # append中不允许为空
print(t1[2])
print(t1)
a = t1[3].keys()
print(a)
t1[3]['like'] = 'music'  # 用等号
print(t1)
c=t1[2][1:3]
print(c)
t1[2][2]=c
print(t1)
print('.................................................................................................................................')
#元组可以遍历输出
for i in t1:
    print(i)
'''
'''
# 集合：集合是没有value 的字典且与列表，字典一样，均属于可变的序列
# 也是通过hash函数来将数据输入集合中
# 创建一个集合的方式：{}和set函数
n1 = {'hello world', 'xv', 19}
n2 = set(range(10))
# n3=set('heelopsja',91,'sijal')#不能这样创建，会报错
print(n2, n1)
n3 = set(['heelopsja', 91, 'sijal'])  # 正确的创建方法
print(n3)
n4 = set([1, 2, 3, 4, 4, 4, 51, 32])  # 集合不允许有重复的元素，他会自动将重复的元素变为一个，且集合为无序的组合
print(n4)
n5 = set('python')
print(n5)  # 无序性
n6 = {}
n7 = set()  # 空集合
print(type(n6), type(n7))
# 类似于列表 字典，用in ,not in 来判断是否存在于集合中
# code:
a1 = set([1, 2, 3, 4, 56, 7, 8, 6, 54, 3, 45, 3])
print(10 in a1)
print(2 in a1)
print(10 not in a1)
print(2 not in a1)
#输出布尔值
#向集合中增加元素.add()[单个元素] .update()[多个元素]
#从集合中删除元素.remove()[不存在元素时报错].discord[不存在元素时不报错].clear（）[懂得都懂].pop()[删除任意元素】

a1.add(100)
print(a1)
a1.update([23,24,25,26,27])#记得加中括号
print(a1)

a1.remove(100)
print(a1)
a1.discard(10000000000000000000000000000000000000)
print(a1)
a1.pop()
print(a1)
a1.clear()
print(a1)
'''
# 判断集合是否相等：==\!=
# 判断一个集合是否是另一个集合的子集：issubset()   ,超集issuperset(),交集：isdisjoint()没有交集为TRUE
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
s2 = {1, 2, 3, 4, 5, 7, 8, 6, 9, 10}
print(s1 == s2)
print(s1 != s2)
print(s2.issubset(s1))
print(s1.issuperset(s2))  # 超集就是超过了这个集合的集合
# 交集：
n1 = {1, 2, 3, 4, 5}
n2 = {4, 5, 6, 7, 8}
print(n1.intersection(n2))
print(n1 & n2)  # 两者是等价操作
# 并集
print(n1.union(n2))
print(n1 | n2)  # 两者是等价的
# 差集
print(n1.difference((n2)))
print(n1 - n2)  # 两者是等价的
# 对称差集
print(n1.symmetric_difference(n2))
print(s1 ^ s2)  # 两者是等价的
# 四种操作均不改变集合的量
# 集合生成式：{i*i for i in range(1,n)}#没有元组生产式
