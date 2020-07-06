def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def quick_select(nums, k, start=0):
    if len(nums) == 1:
        return nums[0]
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
            if start + i < k - 1:
                return quick_select(nums[i+1:], k, start+i+1)
            elif start + i > k - 1:
                return quick_select(nums[:i], k, start)
            else:
                return nums[i]


print(quick_select([7, 6, 5, 4, 3, 2, 1], 6))
