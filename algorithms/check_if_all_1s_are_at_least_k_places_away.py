"""
Leetcode 1437
O(n) runtime, O(1) space
January Leetcoding challenge
Runtime: 552 ms, faster than 82.33% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
Memory Usage: 16.9 MB, less than 64.65% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
"""


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count, counting = 0, False
        for n in nums:
            if n == 0 and counting:
                count += 1
            elif n == 1:
                if not counting:
                    counting = True
                    count = 0
                else:
                    if count < k:
                        return False
                    count = 0
        return True
