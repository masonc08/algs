"""
Leetcode 1687
Leetcode biweekly contest 41
Runtime: 2872 ms, faster than 16.67% of Python3 online submissions for Delivering Boxes from Storage to Ports.
Memory Usage: 64.7 MB, less than 66.67% of Python3 online submissions for Delivering Boxes from Storage to Ports.
"""


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        dp = [0]*(len(boxes)+1)
        ttlw = j = ports = 0
        for i, (p, w) in enumerate(boxes):
            if i-j >= maxBoxes:
                ttlw -= boxes[j][1]
                if boxes[j][0] != boxes[j+1][0]:
                    ports -= 1
                j += 1
            ttlw += w
            if i > 0 and boxes[i-1][0] != p:
               ports += 1
            while ttlw > maxWeight:
                ttlw -= boxes[j][1]
                if boxes[j][0] != boxes[j+1][0]:
                    ports -= 1
                j += 1
            while j < i and dp[j] == dp[j+1]:
                ttlw -= boxes[j][1]
                if boxes[j][0] != boxes[j+1][0]:
                    ports -= 1
                j += 1
            dp[i+1] = ports + 2 + dp[j]
        return dp[-1]
