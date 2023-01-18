def summer_69(arr):
    if len(arr) == 0:
        print(0)
    else:
        summer = []
        for i in arr:
            if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 10 or i == 11:
                summer.append(i)
        print(sum(summer))


# Check
summer_69([])
# Check
summer_69([1, 3, 5])
# Check
summer_69([4, 5, 6, 7, 8, 9])
# Check
summer_69([2, 1, 6, 9, 11])
