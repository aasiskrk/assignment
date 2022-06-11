
def arg(*x):
    print(x)
arg(10,20)


# outer function
def fun(a, b):
    # inner function
    def addition(a, b):
        return a + b
    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5
result = fun(5, 10)
print(result)


def student(name, age):
    print(name, age)
# call using original name
student("ggg", 16)
# assign new name
showStudent = student
# call using new name
showStudent("anna", 26)


x=[1,2,3,4,5,6,7,8]
print(max(x))

'''
In Python ** is an exponential operator.
The double asterisk form of **kwargs is used to pass a keyword, 
variable-length argument dictionary to a function.
'''
'''
Global variables are those which are not defined 
inside any function and have a global scope whereas 
local variables are those which are defined inside a function and 
its scope is limited to that function only.
'''

x = int(input('Enter the number:'))
def fizz_buzz():
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fizz')
    else:
        print(x)
fizz_buzz()


def speed_check(speed):
    global warning_point
    max_speed = 70
    if speed <= max_speed:
        print ("OK")
    elif speed >= max_speed +10:
        print ("Warning")
    else:
        pass
speed_check(67)
speed_check(90)


a = 10
d= int(input("enter num"))
while a>=1:
    for i in range(1,11):
        c = d*i
        print(d,"x",i,"=",c)
        a-=1




x = 'parameter'
print(len(x))


def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))


a = [8,2,3,-1,7]
multiply =1
x[i] = 0
# x[i] = len(a)-1
while(x[i]<len(a)):
    multiply *= a[x[i]]
    x[i] += 1
print(multiply)


x = [8, 2, 3, 0, 7]
sum = 0
for x[i] in x:
    sum +=x[i]
print(sum)


x = [8, 2, 3, 0, 7]
sum = 0
x[i] = 0
while(x[i]<len(x)):
    sum +=x[x[i]]
    x[i] += 1
print(sum)


x = input('Enter the string:')
even = []
odd = []
for i in range(len(x)):
    if i % 2 == 0:
        even.append(x[i])
    else:
        odd.append(x[i])
print('even character',even)
print('odd character',odd)

i=1
sum = 0
while i <11:
    sum += i
    i += 1
print(sum)

def num(l):
    enum = []
    for i in l:
        if i % 2 == 0:
            enum.append(i)
    return enum
print(num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def num(l):
    onum = []
    for i in l:
        if i % 2 != 0:
            onum.append(i)
    return onum
print(num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

x = int(input('Enter the number:'))
if x < 41:
    print('Failed')
elif x >= 41 and x < 55:
    print('Fair')
elif x >= 55 and x < 65:
    print('Good')
elif x >= 65:
    print('Excellent')
else:
    pass

