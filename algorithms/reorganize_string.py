"""
Leetcode 767
Runtime: 40 ms, faster than 13.31% of Python3 online submissions for Reorganize String.
Memory Usage: 14.1 MB, less than 48.63% of Python3 online submissions for Reorganize String.
"""


from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        ct = Counter(S)
        heap = [[-ct[c], c] for c in ct]
        heapq.heapify(heap)
        sb = []
        prev = None
        while heap:
            largest = heapq.heappop(heap)
            if largest[1] == prev:
                if not heap:
                    return ''
                scnd_largest = heapq.heappop(heap)
                heapq.heappush(heap, largest)
                largest = scnd_largest
            sb.append(largest[1])
            largest[0] += 1
            if largest[0] != 0:
                heapq.heappush(heap, largest)
            prev = largest[1]
        return ''.join(sb)
