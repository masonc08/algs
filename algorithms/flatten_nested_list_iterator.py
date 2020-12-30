"""
Leetcode 341

"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


"""
O(n) runtime, O(L) space, where L is the number of lists
Fetching next item on the fly
Runtime: 72 ms, faster than 35.39% of Python3 online submissions for Flatten Nested List Iterator.
Memory Usage: 17.6 MB, less than 57.20% of Python3 online submissions for Flatten Nested List Iterator.
"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.cur = (-1, nestedList)
        self.stk = []
        self._go_to_next()

    def _go_to_next(self):
        i, li = self.cur
        i += 1
        while i == len(li) or not li[i].isInteger():
            while i == len(li):
                if not self.stk:
                    self.cur = None
                    return
                last = self.stk.pop()
                i, li = last[0]+1, last[1]
            while not li[i].isInteger():
                self.stk += (i, li),
                i, li = 0, li[i].getList()
        self.cur = i, li
        
    def next(self) -> int:
        i, li = self.cur
        self._go_to_next()
        return li[i].getInteger() 
    
    def hasNext(self) -> bool:
        return bool(self.cur)


"""
O(n) runtime and space
Storing all values upon construction
Runtime: 68 ms, faster than 59.60% of Python3 online submissions for Flatten Nested List Iterator.
Memory Usage: 17.7 MB, less than 30.38% of Python3 online submissions for Flatten Nested List Iterator.
"""
# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.li = []
#         def helper(cur):
#             for v in cur:
#                 if v.isInteger():
#                     self.li += v.getInteger(),
#                 else:
#                     helper(v.getList())
#         helper(nestedList)
#         self.i = 0

#     def next(self) -> int:
#         sol = self.li[self.i]
#         self.i += 1
#         return sol
    
#     def hasNext(self) -> bool:
#         return self.i != len(self.li)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
