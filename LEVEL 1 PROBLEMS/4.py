def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:
            return True
        else:
            return False


# Check
has_33([1, 3, 3])
# Check
# has_33([1, 3, 1, 3])
# Check
# has_33([3, 1, 3])
