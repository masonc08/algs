def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def quick_sort(nums):
    if len(nums) == 0:
        return nums
    pivot = nums[-1]
    i, j = 0, len(nums) - 1
    while 1:
        while nums[i] < pivot and i != j:
            i += 1
        while nums[j] >= pivot and i != j:
            j -= 1
        if i != j:
            swap(nums, i, j)
        else:
            swap(nums, i, -1)
            nums = quick_sort(nums[:i]) + [nums[i]] + quick_sort(nums[i+1:])
            return nums


print(quick_sort([1, 2, 3, 5, 9]))
