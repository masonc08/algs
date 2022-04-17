"""
bsearch
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


def solve(nums: List[int]):
    smallest = min(nums)
    tmp = nums.index(smallest)
    nums.remove(smallest)
    scndsmallest = min(nums)
    nums.insert(tmp, smallest)
    gap = scndsmallest-smallest
    val_to_index = lambda v: divmod(v-smallest, gap)
    for i in range(len(nums)):
        while 1:
            j, rem = val_to_index(nums[i])
            if rem != 0:
                return False
            if i == j:
                # this element is already in the right place
                break
            jo, remo = val_to_index(nums[j])
            if remo == 0 and j == jo:
                # conflict, two elements belong to the same index
                return False
            nums[i], nums[j] = nums[j], nums[i]
    return True
