x = 5
y = 'hello world'
this_number = False
print(x)
print(y)
print(this_number)

if(x > 10):
    print('this is larger than 10')
else:
    print('this is not larger than 10')

if (x < 0 and this_number == True):
    print('negative and true')
elif(x > 0 and this_number == False):
    print('positive and false')
elif(x > 100 or this_number == True):
    print('large or true')
else:
    print("i don't know")

