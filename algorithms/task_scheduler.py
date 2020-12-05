"""
Leetcode 621
"""


import heapq
import collections

class Solution:
    """
    O(n) runtime, O(1) space by optimized counting
    Runtime: 408 ms, faster than 53.98% of Python3 online submissions for Task Scheduler.
    Memory Usage: 15 MB, less than 6.24% of Python3 online submissions for Task Scheduler.
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = [0]*26
        for task in tasks:
            ct[ord(task)-ord('A')] += 1
        ct.sort()
        i = 25
        while i >= 0 and ct[i] == ct[-1]:
            i -= 1
        return max(len(tasks), (ct[25]-1)*n+ct[25]+25-i-1)


    """
    O(n) runtime, O(1) space by simulation
    Runtime: 664 ms, faster than 11.79% of Python3 online submissions for Task Scheduler.
    Memory Usage: 15 MB, less than 6.24% of Python3 online submissions for Task Scheduler.
    """
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     if n == 0:
    #         return len(tasks)
    #     ct = collections.Counter(tasks)
    #     heap = [ [-ct[key], key] for key in ct ]
    #     heapq.heapify(heap)
    #     recent = collections.deque()
    #     sol = 0
    #     while heap or recent:
    #         sol += 1
    #         if heap:
    #             job = heapq.heappop(heap)
    #             job[0] += 1
    #             if job[0] != 0:
    #                 recent.append((sol, job))
    #         if recent and recent[0][0] == sol-n:
    #             _, freed_job = recent.popleft()
    #             heapq.heappush(heap, freed_job)
    #     return sol
