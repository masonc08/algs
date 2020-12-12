"""
Leetcode 1665
Leetcode contest 216
Runtime: 1276 ms, faster than 85.71% of Python3 online submissions for Minimum Initial Energy to Finish Tasks.
Memory Usage: 59.8 MB, less than 57.14% of Python3 online submissions for Minimum Initial Energy to Finish Tasks.
"""


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        cur = sol = sum([task[0] for task in tasks])
        tasks.sort(key=lambda x: -(x[1]-x[0]))
        additional = 0
        for actual, minimum in tasks:
            if minimum > cur:
                additional = max(additional, minimum-cur)
            cur -= actual
        return sol+additional

    # def minimumEffort(self, tasks: List[List[int]]) -> int:
    #     tasks.sort(key=lambda x: -(x[1]-x[0]))
    #     sol = cur = 0
    #     for actual, minimum in tasks:
    #         if minimum > cur:
    #             sol += (minimum - cur)
    #             cur = minimum
    #         cur -= actual
    #     return sol
