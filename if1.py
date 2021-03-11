#write a program to calculate and display qube of given positive number 
number = input("Enter positive number")
number = int(number)
if number<0:
    number = 0 - number
    print("you have given negative number but it is coverted into positive number")
qube = number * number * number
print("qube is ",qube)
