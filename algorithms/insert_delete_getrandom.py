"""
Leetcode 380
Runtime: 100 ms, faster than 60.62% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 18.5 MB, less than 45.22% of Python3 online submissions for Insert Delete GetRandom O(1).
"""


import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.mp = [], {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.mp:
            return False
        self.mp[val] = len(self.nums)
        self.nums += val,
        return True 
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.mp:
            return False
        idx = self.mp[val]
        self.mp[self.nums[-1]] = idx
        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
        self.nums.pop()
        del self.mp[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randrange(0, len(self.nums))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
