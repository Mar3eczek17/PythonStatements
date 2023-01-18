def almost_there(n):
    print((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


# Check
almost_there(104)
# Check
almost_there(150)
# Check
almost_there(209)
