"""
Leetcode 406
"""


class Solution:
    # Runtime: 92 ms, faster than 85.84% of Python3 online submissions for Queue Reconstruction by Height.
    # Memory Usage: 14.8 MB, less than 58.37% of Python3 online submissions for Queue Reconstruction by Height.
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda v: (-v[0], v[1]))
        sol = []
        for v in people:
            sol.insert(v[1], v)
        return sol

    # Runtime: 656 ms, faster than 11.63% of Python3 online submissions for Queue Reconstruction by Height.
    # Memory Usage: 15 MB, less than 20.48% of Python3 online submissions for Queue Reconstruction by Height.
    # def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    #     people.sort()
    #     L = len(people)
    #     sol = [None]*L
    #     for v in people:
    #         h, k = v
    #         i = 0
    #         ct = 0
    #         while ct < k:
    #             if sol[i] is None or sol[i][0] >= h:
    #                 ct += 1
    #             i += 1
    #         while sol[i] is not None:
    #             i += 1
    #         sol[i] = v
    #     return sol

