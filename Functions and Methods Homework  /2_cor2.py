def ran_check(num, low, high):
    if num in range(low, high + 1):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('{} is not in the range between {} and {}'.format(num, low, high))


# Check
ran_check(7, 2, 7)
