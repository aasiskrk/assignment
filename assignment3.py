

a = 10
b = 20
c = a
a = b
b = c
print(a,b)


for i in range(1,11):
   print(f'10 * {i} = {10*i}')


a = [1,2,3,4]
i = 3
b =[]
while i >= 0:
    rev = a[i]
    print(rev)
    i -= 1

for i in range(-10,0,1):
   print(i)

for i in range(1):
    print("done")


num = int(input('Enter a number: '))
fact = 1
for i in range(num,1,-1):
	fact *= i 
print(fact)

my_list=[10,20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(0,len(my_list)):
	if(i%2 != 0):
		print(my_list[i])

# TO FIND CUBE FROM 1 to 6
for i in range(1,7):
	print(i,"-",i**3)




#  FIRST TEN NATURAL NUMBERS
a = 1
while a<11:
    print(a)
    a+=1







