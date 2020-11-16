"""
Leetcode 1656
Leetcode weekly contest 215
Runtime: 212 ms, faster than 100.00% of Python3 online submissions for Design an Ordered Stream.
Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Design an Ordered Stream.
"""


class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.li = ['']*(n+1)

    def insert(self, id: int, value: str) -> List[str]:
        sol = []
        self.li[id] = value
        if self.ptr == id:
            while self.ptr < len(self.li) and len(self.li[self.ptr]) != 0:
                sol.append(self.li[self.ptr])
                self.ptr += 1
        return sol
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)