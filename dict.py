A={"name":"TY","age":18}
A['grades']=98
print(A)
A['grades']=100
print(A)
del A["name"]
print(A)
'''A.clear()
print(A)'''
#获取关键字
B=A.keys()
print(B)
print(type(B))
print(list(B))
#获取值
C=A.values()
print(C)
print(type(C))
print(list(C))
#同时获取值和关键字
D=A.items()
print(D)
print(type(D))
print(list(D))
#字典元素的遍历
for items in A:
    print(items,'   ',end='')
#字典的高级操作：字典生成式
value=['19','唐烨']
key=['ages','name']
a=zip(value,key)
print(list(a),end='\n')

#2:
'''name=['food','fruits','books']
price=['15元/斤','10元/斤','25元/本']
{name=names,prices=price for name,price in zip(name,prices)}:
    print(list())'''#错误
#3:
item=["food","fruit","books"]
price=['15元/斤','10元/斤','25元/本']
UID={item:price  for item,price in zip(item,price)}
print(UID)
