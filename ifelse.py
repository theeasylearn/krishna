#write a progam to accept blood level in his/her body and if blood level is less then 7 percentage or above 14 percentage  then print message you need medical treatment otherwise print message you are healthy  
blood_level = float(input("enter your blood percentage level in decimal/float value"))
if blood_level>=7.0 and blood_level<=14: #< > <= >= == !=/<>
    print("you are healthy")
else:
    print("you need medical treatment")
print("Have a nice day")