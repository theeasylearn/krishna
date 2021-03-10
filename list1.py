#example of list 

#person = [] empty list
person = ['ankit',35,True,83.00] #empty list
hobby = ['reading','cycling','music'] #empty list
print(person)
print('first value in person list ',person[0])
print('last value in person list ',person[-1])
print('second last value in person list ',person[-2])
print('First two value in list',person[0:2])
person[0] = 'Ankit Patel'
person[-1] = 78
print(person)
print(person*3)
print(person + hobby)
person_hobby = person + hobby
print(person_hobby)