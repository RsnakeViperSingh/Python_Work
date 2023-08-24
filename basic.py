DataTypes
#Airthematic Operators
a = 3
b = 4

print("The value of 3+4 is", 3+4)
print("the value of 3-4 is", a-b)
print("The value of 3*4is", 3*4)
print("The value of 3/4 is", 3/4)
The value of 3+4 is 7
the value of 3-4 is -1
The value of 3*4is 12
The value of 3/4 is 0.75
Assignment Operators
a = 30
a += 2
a -= 2
a *= 2
a /= 2
print(a)
30.0
Comparison Operators
b = (4>7)
print(b)
False
a = (7>3)
print(a)
True
a = (7>=4)
print(a)
True
a = (23!=4)
print(a)
True
Logical Operators
bool1 = True
bool2 = False
print("The value of bool1 and bool 2 is", (bool1 and bool2))
print("The value of bool1 and bool 2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))
The value of bool1 and bool 2 is False
The value of bool1 and bool 2 is True
The value of not bool2 is True
Typecasting (Way to convert one data type two another ..Only when valid data type is present)
a = "3434"

print(type(a))
<class 'str'>
a = "3434"
a = int(a)

print(type(a))
print(a + 5)
<class 'int'>
3439
Input Function
a = input("Enter your name:")
print(a)
Enter your name:

a = input("Enter a Number:")
a = int(a) #Converet a to an integer(If POssible)
print(type(a))
Enter a Number:21
<class 'int'>
Write a program for add two numbers
a = 23
b = 33
print("The sum of a and b is", a + b)
The sum of a and b is 56
Write a program for finf remainder when a number is divided by 2
a = 22
b = 3

print("The remainder when a is divided by b is", a%b)
The remainder when a is divided by b is 1
Write a program to find average of two numbers entered by the user
a = input("Enter First number: ")
b = input("Enter Second Number: ")
a = int (a)
b = int (b)
avg = (a + b)/2
print("The average value of a and b is",avg)
Enter First number: 12
Enter Second Number: 11
The average value of a and b is 11.5
