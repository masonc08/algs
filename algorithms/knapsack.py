class Knapsack:
    def solve(self, weights: List[int], values: List[int], capacity: int) -> int:
        prev, cur = [0]*(capacity+1), [0]*(capacity+1)
        for _ in range(len(weights)):
            for j in range(capacity+1):
                x = prev[j-weights[j]] if j-weights[j] >= 0 else 0
                cur[j] = max(prev[j], values[j]+x)
            prev = cur
            cur = [0]*(capacity+1)
        return prev[-1]
