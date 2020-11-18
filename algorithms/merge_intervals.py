# Leetcode 53

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda interval: interval[0])
        sol = []
        for interval in intervals:
            Solution._merge(sol, interval)
        return sol

    @staticmethod
    def _merge(li, new_interval):
        if len(li) == 0:
            li.append(new_interval)
            return
        last_interval = li.pop()
        a = last_interval[0]
        b = last_interval[1]
        c = new_interval[0]
        d = new_interval[1]
        if c > b:
            li.append(last_interval)
            li.append(new_interval)
        else:
            li.append([a, max(b, d)])
    
    """
    November Leetcoding challenge attempt
    Runtime: 80 ms, faster than 87.94% of Python3 online submissions for Merge Intervals.
    Memory Usage: 15.8 MB, less than 66.66% of Python3 online submissions for Merge Intervals.
    """
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     intervals.sort(key=lambda x: x[0])
    #     sol = [intervals[0]]
    #     for i in range(1, len(intervals)):
    #         c, d = intervals[i]
    #         a, b = sol[-1]
    #         if c <= b:
    #             sol[-1][1] = max(b, d)
    #         else:
    #             sol.append(intervals[i])
    #     return sol
