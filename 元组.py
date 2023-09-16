S1='star','unity',7
print(S1)
print(type(S1))
'''使用内置tuple函数进行创建元组'''
S2=tuple(('sid','Meier','civilzation',6))
print(S2)
print(type(S2))
'''关于元组的一般写法'''
S3=('unity','pycharm',6)
print(S3,type(S3))
print(type(S3))

#一个应用实例
year=input('输入您想查询的年份')
months=input('请输入月份')
days=input('请输入几号')
print('正在输出结果，请等待')
tuple1=(31,29,31,30,31,30,31,31,30,31,30)
tuple2=(31,28,31,30,31,30,31,31,30,31,30)

if year%400==0 or (year%4==0 and year%100!=0) :
    day=sum(tuple1[:months-1])
    fin=days+day
    print('你输入的时间为',year,'年',months,'月',days,'天是',year,'年的',fin,'天')
else:
    day = sum(tuple2[:months-1])
    fin = days + day
    print('你输入的时间为', year, '年', months, '月', days, '天是', year, '年的', fin, '天')