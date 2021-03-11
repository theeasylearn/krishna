#write a program to findout largest number from 3 given number 
num1 = int(input("Enter first integer number"))
num2 = int(input("Enter second integer number"))
num3 = int(input("Enter third integer number"))
if num1>num2:
    if num1>num3:
        print("num1 is the largest number")
    else:
        print("num3 is the largest number")
else:
    if num2>num3:
        print("num2 is the largest number")
    else: 
        print("num3 is the largest number")
print("Good Bye")