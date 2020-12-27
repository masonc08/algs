"""
Leetcode 1705
Leetcode weekly contest 221
Runtime: 632 ms, faster than 100.00% of Python3 online submissions for Maximum Number of Eaten Apples.
Memory Usage: 19.2 MB, less than 66.67% of Python3 online submissions for Maximum Number of Eaten Apples.
"""


import heapq


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        sol = 0
        L = len(apples)
        heap = []
        cur = 0
        while cur < L or heap:
            cur < L and heapq.heappush(heap, (cur+days[cur], cur))
            while heap and heap[0][0] <= cur:
                heapq.heappop(heap)
            if heap:
                _, i = heap[0]
                apples[i] -= 1
                sol += 1
                if apples[i] == 0:
                    heapq.heappop(heap)
            cur += 1
        return sol
