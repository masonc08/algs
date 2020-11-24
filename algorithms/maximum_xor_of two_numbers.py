"""
Leetcode 421
"""


class Solution:
    """
    O(n) time and space complexity using binary tree
    Runtime: 1588 ms, faster than 15.13% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
    Memory Usage: 46.3 MB, less than 33.88% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
    """
    def findMaximumXOR(self, nums: List[int]) -> int:
        class TreeNode:
            def __init__(self):
                self.children = [None, None]

        root = TreeNode()
        for num in nums:
            runner = root
            for i in range(31, -1, -1):
                bit = (num>>i)&1
                if not runner.children[bit]:
                    runner.children[bit] = TreeNode()
                runner = runner.children[bit]
        sol = 0
        for num in nums:
            cur = 0
            runner = root
            for i in range(31, -1, -1):
                bit = (num>>i)&1
                if runner.children[bit^1]:
                    runner = runner.children[bit^1]
                    cur |= (1<<i)
                else:
                    runner = runner.children[bit]
            sol = max(sol, cur)
        return sol
        

    """
    O(n) time and space complexity through process of elimination
    Runtime: 364 ms, faster than 66.78% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
    Memory Usage: 16.1 MB, less than 84.54% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
    """
    # def findMaximumXOR(self, nums: List[int]) -> int:
    #     sol = mask = 0
    #     for i in range(31, -1, -1):
    #         mask |= (1<<i)
    #         prefixes = set()
    #         for num in nums:
    #             prefixes.add(num&mask)
    #         cur = sol|(1<<i)
    #         for prefix in prefixes:
    #             if cur^prefix in prefixes:
    #                 sol = cur
    #                 break
    #     return sol
