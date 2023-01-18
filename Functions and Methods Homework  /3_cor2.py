def up_low(s):
    count_upper = 0
    count_lower = 0

    for char in s:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        else:
            pass

    print('Original String :  Hello Mr. Rogers, how are you this fine Tuesday?')
    print(f'No. of Upper case characters :  {count_upper}')
    print(f'No. of Lower case Characters :  {count_lower}')


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
