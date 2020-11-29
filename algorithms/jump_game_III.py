"""
Leetcode 1306
November Leetcoding challenge
Runtime: 224 ms, faster than 30.75% of Python3 online submissions for Jump Game III.
Memory Usage: 21 MB, less than 24.24% of Python3 online submissions for Jump Game III.
"""


from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        dp = [False]*len(arr)
        dp[start] = True
        q = deque([start])
        while q:
            cur = q.pop()
            v = arr[cur]
            if cur-v >= 0 and not dp[cur-v]:
                if arr[cur-v] == 0:
                    return True
                dp[cur-v] = True
                q.appendleft(cur-v)
            if cur+v < len(arr) and not dp[cur+v]:
                if arr[cur+v] == 0:
                    return True
                dp[cur+v] = True
                q.appendleft(cur+v)
        return False
