"""
Leetcode 1649
January Leetcoding challenge
"""


from sortedcontainers import SortedList


class Solution:
    MOD = 10**9+7
    """
    O(nlogm) runtime, O(n) space
    Fenwick tree
    Runtime: 6044 ms, faster than 45.61% of Python3 online submissions for Create Sorted Array through Instructions.
    Memory Usage: 29 MB, less than 49.71% of Python3 online submissions for Create Sorted Array through Instructions.
    """
    def createSortedArray(self, instructions: List[int]) -> int:
        m = max(instructions)
        li = [0]*(m+1)
        def update(x):
            while x <= m:
                li[x] += 1
                x += x&-x

        def query(x):
            sol = 0
            while x > 0:
                sol += li[x]
                x ^= x&-x
            return sol
        
        sol = 0
        for i, v in enumerate(instructions):
            sol = (sol+min(query(v-1), i-query(v)))%self.MOD
            update(v)
        return sol
                


    """
    O(nlogn) runtime, O(n) space
    SortedList
    Runtime: 8008 ms, faster than 20.47% of Python3 online submissions for Create Sorted Array through Instructions.
    Memory Usage: 29.5 MB, less than 30.12% of Python3 online submissions for Create Sorted Array through Instructions.
    """
    # def createSortedArray(self, instructions: List[int]) -> int:
    #     sol = 0
    #     li = SortedList()
    #     for n in instructions:
    #         L = len(li)
    #         sol = (sol+min(li.bisect_left(n), L-li.bisect_right(n)))%self.MOD
    #         li.add(n)
    #     return sol
