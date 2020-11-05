"""
Leetcode 904
Runtime: 820 ms, faster than 64.06% of Python3 online submissions for Fruit Into Baskets.
Memory Usage: 19.6 MB, less than 63.65% of Python3 online submissions for Fruit Into Baskets.
"""


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        fruit_types = [-1, -1]
        qty = [0, 0]
        last_idx = [-1, -1]
        i = j = 0
        sol = 0
        cumu = 0
        while j < len(tree):
            fruit = tree[j]
            if fruit in fruit_types:
                idx = fruit_types.index(fruit)
                qty[idx] += 1
                last_idx[idx] = j
                if idx != 1:
                    fruit_types.reverse()
                    qty.reverse()
                    last_idx.reverse()
                cumu += 1
            else:
                tmp = last_idx.pop(0)
                cumu -= tmp-i
                i = tmp+1
                fruit_types.pop(0)
                qty.pop(0)
                last_idx.append(j)
                fruit_types.append(fruit)
                qty.append(1)
            sol = max(sol, cumu)
            j += 1
        return sol
