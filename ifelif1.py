#write a python program to calculate bmi and display obcity level as per internation standard

weight = float(input("Enter your weight in kg"))
height = float(input("Enter your height in foot & inch")) #5.8

#convert height into inch only 
foot = int(height) #5
height = (foot * 12) + ((height-foot)*10) # 68
#convert inch into centimeter 
cm = height * 2.54
meter = cm/100

#bmi = weight/(meter*meter)
bmi = weight/(meter*meter)
print(bmi)
if bmi>=30.0:
    print("you are obese")
    print("you should eat less and excercise lot")
elif bmi>=25.0:
    print("you are over weight")
    print("you should excercise lot")
elif bmi>=18.0:
    print("you are healthy")
    print("you should maintain this")    
else:
    print("you are underweight")    
    print("you should eat healthy foot")
print("Good bye")