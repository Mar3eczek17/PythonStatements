def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


# Check
has_33([1, 3, 3])
# Check
has_33([1, 3, 1, 3])
# Check
has_33([3, 1, 3])
