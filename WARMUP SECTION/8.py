def lesser_of_two_evens(a,b):
    # BOTH NUMBERS ARE EVEN!
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    else:
        # ONE OR BOTH NUMBERS ARE ODD!
        if a > b:
            return a
        else:
            return b

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

