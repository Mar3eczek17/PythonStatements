def count_primes(num):
    ctr = 0
    for i in range(num):
        if i <= 1:
            continue
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            ctr += 1
    print(ctr)


# Check
count_primes(100)
