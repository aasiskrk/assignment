
#What is the output of 'banana'>'BANANA'?
print('banana'>'BANANA')
#True



list = [1, 2, 3, 4, 5]
print('Checking weather 5 in list or not:')
if 5 in list:
    print('5 is in the list')
else:
    print('Your entry is not in list')



x = int(input('Enter the number'))
y = int(input('Enter the number'))
z = int(input('Enter the number'))
if x>=y<=z:
    print(y)
elif y>=x<=z:
    print(x)
else:
    print(z)



x = int(input('Enter the three digit number:'))
a = x//100 # it helps to find out fist digit
b = x//10%10 # it helps to find out second digit
c = x%10 # it helps to find out third digit
print('The sum of its number is:')
print(a + b + c)



x = int(input('Enter the month code:'))
if x == 1:
        print("janaury")
elif x == 2:
        print("febuary")     
elif x == 3:
        print("march")
elif x == 4:
        print("april")
elif x== 5:
        print("may")
elif x == 6:
        print("june")
elif x == 7:
        print("july")
elif x == 8:
        print("august")
elif x== 9:
        print("september")
elif x == 10:
        print("october")
elif x == 11:
        print("november")
elif x == 12:
        print("december")
else:
        print("invalid")



x = 5
x += 3  # it is assignment operator which is used to assign the varible
print(x)


x = int(input('Enter the number:\n'))
if x > 1:
    for i in range(2, x):
        if x % i == 0:
            print(x, 'is not a prime number')
            break
    else:
        print(x, 'is a prime number')


x = int(input('Enter the marks:'))
if x < 25:
    grade = 'F'
elif x >= 25 and x < 45: # and operator gives true if both statement are true
    grade = 'E'
elif x >=45 and x < 50:
    grade = 'D'
elif x >=50 and x <60:
    grade = 'C'
elif x >=60 and x <= 80:
    grade = 'B'
else:
    grade = 'A'
print('the grade is:', grade)



a = input('Enter your age')
b = input('Enter your age')
c = input('Enter your age')
if a >= b and a >= c:
    print('Oldest is', a)
elif b >=a and b >= c:
    print('Oldest is', b)
elif c >=a and c >= b:
    print('Oldest is', c)
else:
    print('invalid entry')
if a <=b and a <=c:
    print('Youngest is', a)
elif b <=a and b <=c:
    print('Youngest is', b)
elif c <=a and c <=b:
    print('Youngest is', c)
else:
    print('invalid entry')



x = int(input('Enter your age'))
y = input("enter nationality")
if x >=18 and y =="NEPALI":
    print ('Congratulation you are eligible for voting')
else:
    print ('Sorry your age is not validity for voting')


x = int(input('Enter the number'))
if x % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')



x = int(input('Enter the number:'))
if x % 7 ==0:
    print(x, 'is divisible by 7')
else:
    print(x, 'is not divisible by 7')



x = int(input('Enter the number:'))
if x % 5 == 0:
    print('Hello')
else:
    print('Bye')



x = int(input('Enter the percentage:'))
if x > 90:
    grade = 'A'
elif x > 80 and x <= 90:
    grade = 'B'
elif x >= 60 and x <= 80:
    grade = 'C'
elif x < 60:
    grade = 'D'
else:
    print('Invalid')
print('The grade is', grade)



city = input('Enter the name of city:')
if city.lower() == 'delhi':
    print('The monument name is: Red Fort')
elif city.lower() == 'agra':
    print('The monument name is: Taj Mahal')
elif city.lower() == 'jaipur':
    print('The monument name is: Jai Mahal')
else:
    print('Please enter the correct city')



a = 9
if a > 5 and a <= 10:
    print('Hello')
else:
    print('Bye')



x = int(input('Enter the number:'))
if x % 2 == 0  and x % 3 == 0:
    print(x,'is divisible by 2 and 3 both')
else:
    print(x,'is not divisible by 2 and 3 both')



x = input('Enter the character:').lower()
y = ['a', 'e', 'i', 'o', 'u']
if x in y:
    print('The character you enter is vowel')
else:
    print('The character you enter is not vowel')


x = int(input('Enter the fisrt number:'))
y = int(input('Enter the second number:'))
z = input('Enter the mathematical operator:')
if z == '+':
    print('The answer is',x + y)
elif z == '-':
    print('The answer is',x - y)
elif z == '/':
    print('The answer is',x / y)
elif z == '%':
    print('The answer is',x % y)
