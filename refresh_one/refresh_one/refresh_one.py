#coding=gbk
'''
#one input() print()
a = input("please!input words")
print(eval(a))
'''

'''
#two eval() print()
b = "3+2"
print(eval(b))
'''

#Three（1）列表的定义与基本操作。（2）元组的定义与操作（3）字典的定义与操作。（4）集合的定义与操作。
'''
#(1)
my_list1 = ["a","b","c","d"]
my_list2 = ["p","e","k"]

#遍历 for/while
for value in my_list:
     print(value)

l = len(my_list)
i = 0
while i < l:
    # 通过下标索引获取元素
    value = my_list[i]
    print(value)
    i = i + 1

#append()添加,extend(),insert(),index(),count(),pop(),remove(),sort(),reversed(),clear()
my_list1.append("p")
print(my_list1)
my_list1.extend(my_list2)
print(my_list1,sep = "\n")
my_list1.insert(2,"m")#在指定位置index前插入元素object
print(my_list1)
#update
my_list1[2] = 3
print(my_list1)
#sequence
if 3 in my_list1:

    print("YES!Index in",format(my_list1.index(3)),"number of occurrences in",my_list1.count(3))
else:
    print("NO!")
my_list1.pop(my_list1.index(3))#删除根据对应下标
print(my_list1)
my_list1.remove("a")#根据值删除
print(my_list1)
#my_list1.clear()#清空
print(my_list1)
ret = list(reversed(my_list1))
print(ret)
ret.sort()
print(my_list1)
'''
'''
#(2
from typing import Tuple

tup1,tup2 = ("a","b","c"),("d","e","f")
list1 = [2,2,2]
print("tup1[0]:",tup1[0],"tup2[0:3]:",tup1[0:3],"tup1 + tup2:",tup1 + tup2)
#founction cmp()python3中用operator.eq le gt代替,len(),max(),min(),tuple()
import operator
print(operator.le(tup1,tup2))#tup1 <= tup2
print(len(tup1),max(tup1),min(tup1),tuple(list1))
'''
#(3)len() clear() key() values() items() setdefault() get() enumerate()
dict1 = {1:"alex",2:"21",}
print(dict1[1])#通过key寻找value
print(len(dict1),dict1.keys(),dict1.values(),dict1.items(),sep = '\n')
if 1 in dict1:
    print("YES")
print(dict1.setdefault(13,"qwe"))#key存在 得value,key不存在 得到的value1,会把(key-value1)组成
print(dict1.get(13))
#ergodic
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)
for item in dict1.items():
    print(item)
for key,value in dict1.items():
    print(key,value)
for key,value in enumerate(dict1):#enumerate() 枚举
    print(key,value)
#(4)
