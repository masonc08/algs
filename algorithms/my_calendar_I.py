"""
Leetcode 729
"""


from sortedcontainers import SortedSet


"""
Python TreeMap
"""
class MyCalendar:

    def __init__(self):
        self.intervals = SortedSet(key=lambda x: x[0])

    def book(self, start: int, end: int) -> bool:
        if start > end:
            return False
        i = self.intervals.bisect((start, end))
        sol = True
        if i != 0:
            sol &= self.intervals[i-1][1] <= start
        if sol and i != len(self.intervals):
            sol &= self.intervals[i][0] >= end
        sol and self.intervals.add((start, end))
        return sol

"""
Runtime: 228 ms, faster than 85.85% of Python3 online submissions for My Calendar I.
Memory Usage: 14.7 MB, less than 91.29% of Python3 online submissions for My Calendar I.
"""
# class MyCalendar:

#     def __init__(self):
#         self.intervals = []

#     def book(self, start: int, end: int) -> bool:
#         if start > end:
#             return False 
#         i, j = 0, len(self.intervals)
#         while i < j:
#             m = (i+j)//2
#             v = self.intervals[m][0]
#             if start < v:
#                 j = m
#             else:
#                 i = m+1
#         sol = True
#         if i != 0:
#             sol &= self.intervals[i-1][1] <= start
#         if sol and i != len(self.intervals):
#             sol &= self.intervals[i][0] >= end
#         sol and self.intervals.insert(i, (start, end))
#         return sol


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)