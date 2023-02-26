"""
codeforces 1608-B

"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def solve(self, n, a, b):
        diff = a-b
        if abs(diff) > 1 or a+b+2 > n:
            return [-1]
        if a == b == 0:
            return list(range(1, n+1))
        sol = [0]*n
        if diff == 1: # 1 more peak than valleys
            x = a+b+2
            largest_x_nums = range(n-x+1, n+1)
            for i in range(len(largest_x_nums)//2):
                sol[i*2] = largest_x_nums[i]
                sol[i*2+1] = largest_x_nums[~i]
            i += 1
            sol[i*2] = largest_x_nums[i]
            sol[i*2+1:] = list(range(n-x, 0, -1))
        elif diff == -1: # 1 more valley than peaks
            x = a+b+2
            smallest_x_nums = range(1, x+1)
            for i in range(len(smallest_x_nums)//2):
                sol[i*2] = smallest_x_nums[~i]
                sol[i*2+1] = smallest_x_nums[i]
            i += 1
            sol[i*2] = smallest_x_nums[i]
            sol[i*2+1:] = list(range(x+1, n+1))
        else: # same amount of valleys as peaks
            x = a+b+2
            largest_x_nums = range(n-x+1, n+1)
            for i in range(len(largest_x_nums)//2):
                sol[i*2] = largest_x_nums[~i]
                sol[i*2+1] = largest_x_nums[i]
            i += 1
            sol[i*2:] = list(range(n-x, 0, -1))
        return sol

if __name__ == "__main__":
    for _ in range(int(input())):
        args = list(map(int, input().split()))
        sol = Solution().solve(*args)
        print(" ".join(map(str, sol)))
