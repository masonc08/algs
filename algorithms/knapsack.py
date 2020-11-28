from typing import List


class Knapsack:
    def solve(self, weights: List[int], values: List[int], capacity: int) -> int:
        prev, cur = [0]*(capacity+1), [0]*(capacity+1)
        for weight, value in zip(weights, values):
            for j in range(capacity+1):
                x = 0
                if weight <= j:
                    x = value+prev[j-weight]
                cur[j] = max(prev[j], x)
            prev = cur
            cur = [0]*(capacity+1)
        return prev[-1]

f = Knapsack().solve

assert f([4, 2, 1, 3, 5, 8], [2, 5, 6, 0, 0, 2], 7) == 13
assert f([1, 3, 4, 5], [2, 2, 5, 1], 6) == 7
