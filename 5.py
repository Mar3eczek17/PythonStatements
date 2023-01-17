def myfunc(**kwargs): # **kwargs -> returns back a dictionary
    if 'fruit' in kwargs:
        print(kwargs)
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find ay fruit here')

myfunc(fruit='apple', veggie='lettuce')