"""
Leetcode 621
Runtime: 664 ms, faster than 11.79% of Python3 online submissions for Task Scheduler.
Memory Usage: 15 MB, less than 6.24% of Python3 online submissions for Task Scheduler.
"""


import heapq
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        ct = collections.Counter(tasks)
        heap = [ [-ct[key], key] for key in ct ]
        heapq.heapify(heap)
        recent = collections.deque()
        sol = 0
        while heap or recent:
            sol += 1
            if heap:
                job = heapq.heappop(heap)
                job[0] += 1
                if job[0] != 0:
                    recent.append((sol, job))
            if recent and recent[0][0] == sol-n:
                _, freed_job = recent.popleft()
                heapq.heappush(heap, freed_job)
        return sol
