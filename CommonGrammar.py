# -*- coding: utf-8 -*-
# @Time    : 2020/8/15 6:04
# @Author  : kangqing
# @Email   : kangqing.37@gmail.com
# @File    : CommonGrammar.py
# @Software: PyCharm
""" python语法简单记录 """
"""
基本数值计算
"""
print('*** python没有 i++ i-- 和 ++i --i等自增自减写法, i += 1可以这样写')
print('除法返回浮点型 = ', 17 / 3)
print('与java相同，取余数 = ', 17 % 3)
print('相当于java中的 / 取商 = ', 17 // 3)
print('相当于java中Math.pow(a, b)计算a ^ b = ', 3 ** 4)
print('-----------------------------------------------')


"""
字符串
"""
# 字符串前边加 r 防止转移成特殊字符, 例如 \n
print(r'D:\some\name')
print("会自动换行,", end="")
print('如果不想换行')
print('-----------------------------------------------')


'''
python独特的复制操作，相当于
a = 1
b = 2
c = 3
'''
a, b, c = 1, 2, 3
print('-----------------------------------------------')


'''
比较运算符
'''
d = [1, 2]
print(a == b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a != b)
print('a和b是同一个对象', a is b)
print('a和b不是是同一个对象', a is not b)
print('a是d容器中的成员', a in d)
print('a不是d容器中的成员', a not in d)
print('-----------------------------------------------')


'''
逻辑运算符
'''
print('逻辑与', (a and b) in d)
print('逻辑或', (a or b) in d)
print('逻辑非', not (a in d))
print('-----------------------------------------------')


'''
条件语句：
'''
if a == 1:
    print('主要记住elif,否则如果的意思 a = ', a)
elif a == 2:
    pass
else:
    pass
print('-----------------------------------------------')


'''
python中bool类型, True  False 注意大写
'''
print(1 == 1)
print(1 == 2)
print('-----------------------------------------------')


'''
while循环能代替java中的 fori循环，即可操纵 i
'''
i = 0
while i < 10:
    print(i + 1, end=' ')
    # 相当于 fori 主要是这行 i 是可控的
    if i == 5:
        i += 2
        continue
    i += 1
print('')
print('-----------------------------------------------')


'''
for循环，可以用来循环字符串、列表、等等
'''
# 换行, for循环输出字符串中的每一个字符
print('')
s = '123456'
for x in s:
    print(x, end=" ")

# for循环输出列表中的每一个元素
d = [1, 2, 3]
# 换行
print('')
for x in d:
    print(x, end=' ')

# for循环1-10左闭右开
print('')
for x in range(10):
    print(x + 1, end=' ')
print('')
print('-----------------------------------------------')


'''
列表索引操作
'''
# 换行
print('')
d = ['bob', 'tom', '小明', '小李']
print('d列表包括：', d)
print('d[0] = ', d[0])
print('d[1] = ', d[1])
print('d[2] = ', d[2])
print('d[3] = ', d[3])
# python支持索引负数，即倒叙-1开始
print('python支持索引负数，倒叙-1开始, d[-1] = ', d[-1])
print('d[-2] = ', d[-2])
print('-----------------------------------------------')


'''
分片
分片操作，冒号隔开，以字符串为例
分片也可以负数，倒数第一个为-1索引
分片左闭右开,不写起始位置默认0,不写终止位置默认为-1,都不写复制整个序列
分片可以设置步长，步长默认为1，步长不能为0，步长可以使负数，负数的情况下索引要从大往小写
'''
s = '0123456789'
print('s[:] = ', s[:])
print('s[:3] = ', s[:3])
print('s[8:] = ', s[8:])
print('s[0:3] = ', s[0:3])
print('s[-3:-1] = ', s[-3:-1])
print('s[-3:9] = ', s[-3:9])
print('s[-3:10] = ', s[-3:10])

print('步长为2分片s[0:5:2] = ', s[0:5:2])
print('步长为负数则先写索引大的s[9:3:-2] = ', s[9:3:-2])
print('步长为负数则先写索引大的s[-1:-6:-2] = ', s[-1:-6:-2])
print('同样可以省略任何一个s[::] = ', s[::])
try:
    print('步长不能为0会异常s[::0] = ', s[::0])
except ValueError:
    print('步长不能为0, ValueError: slice step cannot be zero')
print('此时字符串s为', s)
print('-----------------------------------------------')


'''
序列的长度、最大值、最小值、赋值操作、删除操作、分片赋值
'''
d = [1, -1, -12, 3, 34, 0, 6]
print('输出列表d为', d)
print('d的长度是 = ', len(d))
print('最大值 = ', max(d))
print('最小值 = ', min(d))
# 相当于把列表最后一个元素 6 替换成了 98
d[-1] = 98
print('给列表赋值d[-1] = 98 此时最大值是 = ', max(d))
print('再次输出列表d, 相当于把列表最后一个元素 6 替换成了 98, 新列表是 ', end=' ')
print(d)
# 删除列表中的最后一个新元素
del d[-1]
print('del d[-1] 删除最后一个元素此时列表最后一个元素是 = ', d[-1])
print('执行分片赋值操作d[-3:] = [100, 100, 100]')
d[-3:] = [100, 100, 100]
print('分片赋值之后输出d', d)

print('-----------------------------------------------')


'''
列表方法
append(x):在列表的最后插入新的值x
clear():清空列表的内容
copy():用于复制一个列表
count():统计某个元素在列表中出现的次数
extend():用于在列表结尾插入一个新的列表，也就是用新的列表来扩展原来的列表，但是不产生新的列表
index(x):用于从列表中查找x元素第一次出现位置的索引
insert(index, value)用于把值value插入到列表索引index的位置
pop():默认从列表中的最后一个元素移除，并返回该值
pop(index):移除索引index的元素，并返回该值
remove(x):移除列表中元素x的第一次匹配项
reverse():反转列表每一个元素
sort(reverse = True):降序排序
sort()
'''
d = list([1, 2, 3])
d.clear()
d.append(1)
d.append(10)
d.append(10)
d.append(3)
d.append(5)
print('d清空后重新插入d = ', d)
d_copy = d.copy()
print('复制出来的与d不指向同一地址 d is d_copy = ', d is d_copy)
print('d.copy()复制出来的列表d_copy = ', d_copy)
print('统计d中10出现的次数 = ', d.count(10))
d.extend(d_copy)
print('用d_copy扩展d列表 d.extend(d_copy) 之后输出d', d)
print('从d中找出某个数第一次出现位置的索引 d.index(10) = ', d.index(10))
d.insert(0, 20)
print('d.insert(0, 20)把值20插入到d的索引0的位置，输出d = ', d)
print('pop()移除列表中的最后一个元素,并返回值 = ', d.pop(), '新的d = ', d)
print('pop(-2)移除索引为-2的元素并返回该值 = ', d.pop(-2), '新的d = ', d)
print('remove(1)移除d中元素10的第一个匹配项', d.remove(1), '新的d = ', d)
d.reverse()
print('d.reverse() 反转d = ', d)
d.sort()
print('sort()对列表进行排序', d)
d.sort(reverse=True)
print('d.sort(reverse=True)列表降序排列', d)
print('d.sort()操作会改变原列表，如果不想改变可以使用分片获取副本d_copy = d[:]，或者sorted(x)操作其副本')
print('-----------------------------------------------')


'''
元组
元组也是一种序列，但是元组是只读的
元组声明方法是  用,分割一些值  即使声明一个元素的元组也是  3,  一般会加上(3,)
元组存在的意义：
1)元组可以在映射中作为键值使用，而列表不能这么做，因为列表是可变的
2)很多内建函数和方法的返回值就是元组，也就是说，如果要使用这些内建函数或方法的返回值，就必须使用元组
'''
yz1 = (3,)
yz2 = (3, 4, 5, 6)
print('转换列表或者字符串为元组：')
yz_d = tuple(d)
print('yz_d = tuple(d) 把d转换为元组,输出元组yz_d = ', yz_d)
yz_s = tuple('coffee')
print('把字符串转换为元组,则字符串会拆分 输出yz_s = ', yz_s)
print('-----------------------------------------------')
