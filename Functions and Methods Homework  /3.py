def up_low(s):
    out = []
    for i in s:
        out.append(i)
    count_upper = 0
    count_lower = 0
    for i in out:
        if i[0].isupper():
            count_upper += 1
        elif i[0].islower():
            count_lower += 1
    print('Original String :  Hello Mr. Rogers, how are you this fine Tuesday?')
    print('No. of Upper case characters :  {}'.format(count_upper))
    print('No. of Lower case Characters :  {}'.format(count_lower))


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
