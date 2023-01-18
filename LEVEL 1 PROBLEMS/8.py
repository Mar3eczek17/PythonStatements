def spy_game(nums):
    out = []
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            out.append(nums[i])
        else:
            pass
    if out == [0,0,7]:
        print(True)
    else:
        print(False)


# Check
spy_game([1,2,4,0,0,7,5])
# Check
spy_game([1,0,2,4,0,5,7])
# Check
spy_game([1,7,2,0,4,5,0])