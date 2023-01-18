def ran_check(num,low,high):
    if low <= num <= high:
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('{} is not in the range between {} and {}'.format(num, low, high))


# Check
ran_check(5,2,7)