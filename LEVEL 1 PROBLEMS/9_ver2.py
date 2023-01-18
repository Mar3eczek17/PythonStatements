def count_primes(num):
    # Check for 0 or 1 input
    if num < 2:
        return 0
    #################
    # 2 or greater
    ##############

    # Store our prime numbers
    primes = [2]
    # Counter going up to the input num
    x = 3

    # x is going through every number up to input num
    while x <= num:
        # Check if x is prime
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    print(len(primes))


# Check
count_primes(100)
