"""
Leetcode 1268, Daily Coding Problem #11
Runtime: 68 ms, faster than 96.75% of Python3 online submissions for Search Suggestions System.
Memory Usage: 16.9 MB, less than 87.69% of Python3 online submissions for Search Suggestions System.
"""


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        L = len(products)
        s, e = 0, L-1
        sol = []
        for i, c in enumerate(searchWord):
            while s <= e and (len(products[s]) < i+1 or products[s][i] != c):
                s += 1
            while s <= e and (len(products[e]) < i+1 or products[e][i] != c):
                e -= 1
            sol += products[s:s+min(3, e-s+1)],
        return sol
