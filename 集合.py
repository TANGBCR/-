'''第一钟表达方式：使用range函数'''
A=set(range(10))
print(A,type(A))
'''第二种方式：直接写'''
A1={1,2,3,4,5,5,6,6,2,34,6,6}#但是要注意，集合是{}，元组是(),字典是{name:key}

print(A1,type(A1))
'''元组和字典是能够转化为集合的'''
D1=[1,23,4,45,5,3,45,6,78]
T1=(1,23,4,4,5,6,6,778,8,9)
A2=set(D1)
A3=set(T1)
print(A2,type(A2))
print(A3,type(A3))
print(T1,type(T1))
print(D1,type(D1))


#print(……in……)/print(……not in……)
B={1,2,3,34,2,23123,7}
print(63 in B)
print(1 in B)
print(123 not in B)
print(34 not in B)

#对集合内部的修改：增删.add/.update/.remove/.clear/.discard/.pop
C=set(range(1,101))
print(C)
'''.add.update'''
'''加'''
'''.remove……'''
'''减'''
'''判定是否拥有重叠部分'''
S1={1,2,3,4,5,6,7,8,9}
S2={1,2,4}
print(S1.issuperset(S2))
#并集合部分
s1={1,2,3,4,5,6}
s2={0}
p2=s1 |s2
print(p2)

