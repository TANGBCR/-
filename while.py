'''sum=0
a=0
while a<=5:
    a+=1
    sum+=a


    print('和为',sum)'''
a=1
sum=0
while a<=100:
    a+=1
    if a%2==0:
        sum+=a
    else:
        continue
print('和为',sum)

#第二种表示方式
for a1 in range(1,101,2):
    sum1=0
while a1<=100:
    sum1+=a1
print('和为',sum1)