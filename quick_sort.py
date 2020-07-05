def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def quick_sort(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums
    pivot = nums[-1]
    i, j = 0, len(nums) - 2
    while 1:
        if nums[i] > pivot >= nums[j]:
            swap(nums, i, j)
        if i >= j:
            if nums[i] >= pivot:
                swap(nums, i, -1)
            return quick_sort(nums[:i]) + [nums[i]] + quick_sort(nums[i+1:])
        if nums[i] < pivot and i != j:
            i += 1
        if nums[j] >= pivot and i != j:
            j -= 1


print(quick_sort([2, 1, 8, 9, 3]))
