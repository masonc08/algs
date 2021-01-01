"""
Leetcode 636
Runtime: 64 ms, faster than 96.68% of Python3 online submissions for Exclusive Time of Functions.
Memory Usage: 14.5 MB, less than 19.89% of Python3 online submissions for Exclusive Time of Functions.
"""


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        sol = [0]*n
        stk = []
        for log in logs:
            f, op, time = log.split(':')
            f, time = int(f), int(time)
            if op == 'start':
                if stk:
                    last_f, last_t = stk[-1]
                    sol[last_f] += time-last_t
                stk += [f, time],
            if op == 'end':
                time += 1
                start_time = stk.pop()[1]
                sol[f] += time-start_time
                if stk:
                    stk[-1][1] = time
        return sol
