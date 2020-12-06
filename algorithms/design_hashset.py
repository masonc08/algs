"""
Leetcode 705
Runtime: 220 ms, faster than 49.53% of Python3 online submissions for Design HashSet.
Memory Usage: 18.5 MB, less than 78.45% of Python3 online submissions for Design HashSet."""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 0
        self.table = [None]*16


    def _expand(self):
        new = [None]*(len(self.table)*2)
        for key in self.table:
            if key is not None and key is not '*':
                i = key%len(new)
                while new[i] is not None:
                    i = self.wrap(i+1, len(new))
                new[i] = key
        self.table = new
    

    wrap = lambda self, i, size: (i+size)%size


    def add(self, key: int) -> None:
        i = key%len(self.table)
        while self.table[i] != '*' and self.table[i] is not None and self.table[i] != key:
            i = self.wrap(i+1, len(self.table))
        if self.table[i] == key:
            return
        self.table[i] = key
        self.capacity += 1
        if self.capacity > (len(self.table)//4*3):
            self._expand()


    def remove(self, key: int) -> None:
        i = key%len(self.table)
        while self.table[i] != key and self.table[i] is not None:
            i = self.wrap(i+1, len(self.table))
        if self.table[i] is None:
            return
        if self.table[i] == key:
            self.table[i] = '*'
            self.capacity -= 1
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = key%len(self.table)
        while self.table[i] != key and self.table[i] is not None:
            i = self.wrap(i+1, len(self.table))
        if self.table[i] is None:
            return False
        if self.table[i] == key:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
