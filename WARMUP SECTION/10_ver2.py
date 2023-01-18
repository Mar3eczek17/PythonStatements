def makes_twenty(n1, n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20


# Check
print(makes_twenty(20, 10))
# Check
print(makes_twenty(12, 8))
# Check
print(makes_twenty(2, 3))
