def ascending_order(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left
def restoreSortedArray(nums):
    pivot = ascending_order(nums)
    return nums[pivot:] + nums[:pivot]
nums = [3, 4, 5, 1, 2]
sorted_nums = restoreSortedArray(nums)
print(sorted_nums)
