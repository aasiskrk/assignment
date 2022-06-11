
x = [1,2,3,4,5,6,7,8,9]
print(min(x))

x = [1,2,3,4,5,6,7,8]
y = []
if not len(x):
    print('the list is empty')
else:
    print('the list is not empty')
if not len(y):
    print('the list is empty')
else:
    print('the list is not empty')

import random
x  = [1,2,3,4,'python',5,6]
print(random.choice(x))

x = [1,2,3,4,'python',5,6]
y = x.copy()
print(y)


def second_largest(x):
    large = max(x)
    x.remove(large)
    large = max(x)
    return large
p = []
n = int(input('Enter the size of list'))
for i in range(0,n):
    y = int(input('Enter the element of list'))
    p.append(y)
print('The second largest element in',p,'is')
print(second_largest(p))


def my_list(li):
    a =[]
    x = [li[3]]
    for i in li:
        if i not in x:
            a.append(i)
    return a
print(my_list([1,2,3,'putting',5,7]))


num = (0,1,2,3,4,5,6,7,8,9,10)
count_odd = 0
count_even = 0
for i in num:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print('Number of even number :',count_even)
print('Number of odd number:',count_odd)


x = [1,2,3,4,5,6,7,8]
y = tuple(x)
print(y)

x = (1,2,3,4,5,6,7,8)
y = list(x)
print(y)

x = (1,2,3,4,5,6,7,8,'ge')
y = str(x)
print(y)


x = [('name', 9)]
y = dict(x)
print(y)


x = {0: 10, 1: 20}
x.update({5:67})
print(x)


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict4={}
dict4.update(dic1)
dict4.update(dic2)
dict4.update(dic3)
print(dict4)


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
key_present(5)
key_present(9)


d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)  


x = {1:'a',2:'b'}
y = {3:'b',5:'g'}
print(x | y)


third_largest = [1,2,3,4,5,6,7,8,9]
third_largest.sort()
print(max(third_largest)-1)


x = {1,2,3,4,5,6,7,8,9}
print(x)
print(type(x))


x = {1,2,3,4,5,6,7}
for i in x:
    print(i)


x = {1,2,3,4,5,6,7}
x.add(8)
print(x)


x = {1,2,3,4,5,6,7}
x.remove(7)
print(x)


x = {1,2,3,4,5,6,7}
x.discard(98)
print(x)


a = {1,2,3,4,5,6,7,8}
b = {7,6,8,9,10}
intersection = a & b
print(intersection)


a = {1:'pu',2:'par'}
if 'pu' in a.values():
    print('present')
else:
    print('not present') 