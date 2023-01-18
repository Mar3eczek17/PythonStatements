def up_low(s):
    # Dictionary
    d = {'upper': 0, 'lower': 0}

    for char in s:
        if char.isupper():
            d['upper'] += 1
        elif char.islower():
            d['lower'] += 1
        else:
            pass

    print('Original String :  Hello Mr. Rogers, how are you this fine Tuesday?')
    print(f'No. of Upper case characters :  {d["upper"]}')
    print(f'No. of Lower case Characters :  {d["lower"]}')


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
