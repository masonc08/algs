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
