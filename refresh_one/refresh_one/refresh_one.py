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

#Three��1���б�Ķ����������������2��Ԫ��Ķ����������3���ֵ�Ķ������������4�����ϵĶ����������
'''
#(1)
my_list1 = ["a","b","c","d"]
my_list2 = ["p","e","k"]

#���� for/while
for value in my_list:
     print(value)

l = len(my_list)
i = 0
while i < l:
    # ͨ���±�������ȡԪ��
    value = my_list[i]
    print(value)
    i = i + 1

#append()���,extend(),insert(),index(),count(),pop(),remove(),sort(),reversed(),clear()
my_list1.append("p")
print(my_list1)
my_list1.extend(my_list2)
print(my_list1,sep = "\n")
my_list1.insert(2,"m")#��ָ��λ��indexǰ����Ԫ��object
print(my_list1)
#update
my_list1[2] = 3
print(my_list1)
#sequence
if 3 in my_list1:

    print("YES!Index in",format(my_list1.index(3)),"number of occurrences in",my_list1.count(3))
else:
    print("NO!")
my_list1.pop(my_list1.index(3))#ɾ�����ݶ�Ӧ�±�
print(my_list1)
my_list1.remove("a")#����ֵɾ��
print(my_list1)
#my_list1.clear()#���
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
#founction cmp()python3����operator.eq le gt����,len(),max(),min(),tuple()
import operator
print(operator.le(tup1,tup2))#tup1 <= tup2
print(len(tup1),max(tup1),min(tup1),tuple(list1))
'''
#(3)len() clear() key() values() items() setdefault() get() enumerate()
dict1 = {1:"alex",2:"21",}
print(dict1[1])#ͨ��keyѰ��value
print(len(dict1),dict1.keys(),dict1.values(),dict1.items(),sep = '\n')
if 1 in dict1:
    print("YES")
print(dict1.setdefault(13,"qwe"))#key���� ��value,key������ �õ���value1,���(key-value1)���
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
for key,value in enumerate(dict1):#enumerate() ö��
    print(key,value)
#(4)
