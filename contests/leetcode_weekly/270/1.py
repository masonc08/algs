class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        sol = set()
        L = len(digits)
        for i in range(L):
            if digits[i] == 0:
                continue
            for j in range(L):
                if j == i:
                    continue
                for k in range(L):
                    if digits[k]%2 == 1 or k == i or k == j:
                        continue
                    sol.add(digits[i]*100 + digits[j]*10 + digits[k])
        return sorted(list(sol))
