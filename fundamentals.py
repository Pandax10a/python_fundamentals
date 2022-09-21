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

array_x = ['this is', 'a long string', 'from the strings']

array_num = [10, 7, 5, 3, 1, 2, 4, 6, 8]

for a_x in array_x:
    print(a_x)

for a_num in array_num:
    print('look at this number ', a_num)

