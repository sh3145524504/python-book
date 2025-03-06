#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Date   : 11:50
# Autor  :SH
# File     :ss.py
# Software :PyCharm

#注释实操   主要是实操了end与sep的运行结果
print('heello',end='1')
print('word')

print("six","master",sep='/')
print('sister')

demo = 1
print(demo)

demo = 32465
print(demo)

sh = "a"
print(demo,sh,sep='/',end='1')
print(type(sh))

shen = 5 + 5j
print(type(shen))
lex = 10 + 8j
print(shen+lex)

name = 'WWH'
age = 18
print('我的名字：%s 我的年龄: %d'% (name,age))

xiaoshu = 1.23
print('%f' % xiaoshu)  #默认后六位小数

name = "wwh"
age = "18"
print(f"我的名字是{name}我的年龄是{age}")

source = 100
if source == 100:
    print("恭喜你考了满分")
elif source >= 80:
    print("你的成绩为优秀")
else:
    print('你的成绩不好')
# 以上是普通的if 判断 多选一

demo = input
if demo == 50:
    print("战斗达标")
    if demo >= 50 <=100:
        print("战斗力超标")

n1 = 66
n2 = 99
n1 += n2
print(n1)

# 求字符串长度（len函数）
W = "555555555"
print(len(W))

# 通过索引获得字符串的单个字符（即为-1）
print(W[0])

# 布尔类型的赋值（布尔类型即为True{真}以及False{假})
de1 = True
de2 = False

# 空值类型
n = None

# 使用type函数进行变量辨认
print(type(W))
print(type(de1))
print(type(de2))
print(type(n))
print(type(3.56))

# 使用input来输入
weight = float(input("请输入您的体重 (单位:kg) : "))
height = float(input("请输入您的身高 (单位:m) : "))
BMI = weight / height ** 2
print("您的BMI值为 : " + str(BMI))

#not > and > or (优先级) and即为一假全假 or为一真全真(True False)真假

#append 添加
#remove 删除
#max 最大
#min 最小
#sorted 排序

name = 'wwh'
age = 18
print("My Name is {name} and i am {age} years old")
print(f"My Name is {name} and i am {age} years old") #f格式化输出

i = 1   # 定义一个初始值，记录循环的次数，i=1表示从第一次开始
while i <= 5:
    print("我是一个大帅哥")
    i += 1 #每执行一次i的次数就加1

i = 1  # 定义i的值
while i <= 100:  # 规定i最大为100往下
    print(i)  # 打印输出i
    i += 1  # i每循环一次就加1


i = 1   #定义i的值
s = 0    #定义计算的结果，计算结果从0开始，没有相加
while i <= 100:   #规定i最大为100往下
    print(i)     #打印输出i
    s += i     #每次循环结果计算和i相加
    i += 1     #i每循环一次就加1
    print("计算结果是:",s)  #打印每次相加的结果
# print("计算机结果是：",s)  #打印最后计算结果

i = 1   #定义一个外循环次数
while i <= 3:   #循环三次
    print(f"这是第{i}次外循环") #使用f格式化输出，并记录每次i次外循环次数
    j = 1
    while j <= 3:
        print(f"这是第{j}次内循环") #格式化输出内循环
        j += 1
    i += 1
# 注意严格控制缩进，缩进决定层级，外循环一次，内循环就需要循环所定义的最大

#for循环
ww = "我要成为python高手"  #定义一个字符串
for i in ww:            #i是常规变量，可以随便定义，这里取i是因为常规用i
    print(i)           #最后实现用for去遍历取值的整体

# range()
# 用来记录循环次数,相当于计数器
for i in range(1,6):  #记录从1-6，遵循包前不包后原则[) 例如1-6就输出1-5
    print(i)

for i in range(5):  #只写循环五次是从0开始到5
    print("我是大帅哥")


#for循环计算1+2+3+。。100的值
a = 0
for i in range(1,101): #包前不包后，从1-100
    a += i    #每循环一次计算结果与i相加
    print("计算结果是",a)
#print("计算结果是",a) 仅输出最终结果
# 相比之下for循环比while循环更常见更简便一些。

#循环中使用break关键字
i = 1   #定义一个变量
while i <= 5:       #小明要跑五圈
    print(f"小明跑了{i}圈")     #使用格式化输出打印小明跑了i圈
    if i == 3:                     #定义在小明跑到第三圈的时候跑不动了
        print("小明跑不动了")
        break               #使用break在第三次循环时结束循环
    i += 1               #每循环一次的时候i+1

#continue关键字在循环中的使用
i = 1
while i <= 5:
    print(f"小明跑到了第{i}圈")
    if i == 3:
        print("小明第三圈太累了，不跑了休息一下")
        i += 1    #在continue关键字使用前，循环中需要修改计数器，否则他会一直死循环
        continue
    i += 1

#在for循环中使用例子
for i in range(5):
    if i == 3:
        continue   #跳过i=3，直接循环下一个
        # break     #在i等于3时结束循环
    print(i)   #这里注意缩进

# 字符串的编码的转换
a = "hellow"
print(type(a))   #str,字符串
a1 = a.encode()      #编码
print(a1)         #这时发现str被转换成了bytes，以字节为单位处理的Unicode编码
print(type(a1))
a2 = a1.decode()    #定义一个a2保存解码的结果，这时打印发现被解码成为字符串
print(a2)

st = "我要成为python高手"
st1 = st.encode("utf-8")
print(st1)   #这里打印发现转换成了以字节类型
print(type(st1))
st2 = st1.decode("utf-8")
print(st2)
print(type(st2))   #这里发现解码成了字符串类型

#  成员运算符
# 作用： 检查字符串中是否包含了某个字符串（即某个字符或多个字符）
# in ： 如果包含的话，返回True，不包含返回False
# not in ： 如果不包含的话，返回True，包含返回False
name = "wwh"
print("b" in name)      #False
print('w' in name)      #True
print('b' not in name)   #True
print('w' not in name)   #False
