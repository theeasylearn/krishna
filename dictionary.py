#example of dictionary 
book = {'name':'Atomic Habit','price':300,'weight':300.99}
print(book)
print(book['name'])
book['name'] = 'THE SECRET'
book['isbn'] = '1234 5678 01001'
print(book)
del book['name']
print(book)