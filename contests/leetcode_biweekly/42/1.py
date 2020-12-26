"""
Leetcode 1700
Leetcode biweekly contest 42
Runtime: 40 ms, faster than 33.33% of Python3 online submissions for Number of Students Unable to Eat Lunch.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Number of Students Unable to Eat Lunch.
"""


import collections


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = collections.deque(students)
        sandwiches.reverse()
        reps = 0
        while students and sandwiches:
            pref, sand = students.popleft(), sandwiches[-1]
            if pref == sand:
                sandwiches.pop()
                reps = 0
            else:
                students.append(pref)
                reps += 1
                if reps == len(students):
                    return reps
        return 0
