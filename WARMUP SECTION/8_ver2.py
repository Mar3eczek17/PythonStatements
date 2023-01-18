def lesser_of_two_evens(a, b):
    # BOTH NUMBERS ARE EVEN!
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        # ONE OR BOTH NUMBERS ARE ODD!
        return max(a, b)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))
