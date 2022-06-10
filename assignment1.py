
a = 5
b = 4
if a == b:
    print('1')
elif a>b:
    print('2')
else:
    print('3')



a = 'krki'
b = 'krki'
c = 'no'
d = 'aassi'
if a == b and c == d:
    print('Hello')
else:
    print("invalid")


a = 'lambda'
b = 'laptop'
c = 'har'
d = 'krk'
if a == b or c == d:
    print('Hello')
else:
    print('Does not exist')



x = int(input("enter any int"))
if x > 0:
    print('True')
elif x < 0:
    print('False')
else:
    print('Zero')



x = int(input('Enter the number:'))
if x % 2 == 0:
    print('It is even number')
else:
    print('It is odd number')


print('Enter the marks of four Subject:')
Maths = int(input('Enter the marks of Maths:'))
Science = int(input('Enter the marks of science:'))
Social = int(input('Enter the marks of social:'))
English = int(input('Enter the marks of english:'))
WAP = Maths + Science + Social + English
Percentage = ( WAP / 400 ) * 100
if Percentage >= 70:
    print('Distinction')
    Grade = 'A'
elif Percentage >= 60:
    print('first division')
    Grade = 'B'
elif Percentage >= 40:
    print('\tPass')
    Grade = 'C'
else:
    print('Fail')
    Grade = 'E'
print('The Total Marks is:', WAP)
print('The Percentage is:', Percentage)
print('The Grade is:', Grade)



# What is the output of 'APPLE' > 'apple'??
print('APPLE'>'apple')
#False


print("Personal details")
name = 'Aashista karki'
age = 19
address = 'Naya Baneshwor'
print(name)
print(age)
print(address)

 

from math import pi
r = int(input('Enter the radius of the circle:'))
Area = pi * (r**r)
print('The area of circle:' , Area)



a = int(input('Enter the no of students in class a:'))
b = int(input('Enter the no of students in class b:'))
c = int(input('Enter the no of students in class c:'))
print('The possible no of desk that can be purchase is:')
print(a//2 + b//2 + c//2 + a%2 + b%2 + c%2)                 #snakify theorem
# '//' means floor division helps to find out the no of desk
# '%' means modulus helps to find out the reminder
# the final result of this code is find out the exact no of desk


x = int(input('Enter the number:'))
y = int(input('Enter the number:'))
z = int(input('Enter the number:'))
if x >= y <= z:
    print(y)
elif y >= x <= z:
    print(x) 
else:
    print(z) 



m = int(input('Enter the number:'))
n = int(input('Enter the number:'))
o = int(input('Enter the number:'))
print(m + n + o)



x = int(input('Enter the hight of right angled tringle:'))
y = int(input('Enter the lenght of base:'))
print(x * y /2)


N = int(input('Number of students:'))
K = int(input('Number of Apples:'))
print(K // N)
# print(K // N) represent the no of apples got by the single students
print(K % N)
# print(K % N) represent the no of apples remain in the basket
