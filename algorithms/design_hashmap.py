"""
Leetcode 706
Runtime: 268 ms, faster than 37.71% of Python3 online submissions for Design HashMap.
Memory Usage: 17.6 MB, less than 38.57% of Python3 online submissions for Design HashMap.
"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 0
        self.table = [None]*16


    def _expand(self):
        new = [None]*(len(self.table)*2)
        for key in self.table:
            if key is not None and key != '*':
                i = key[0]%len(new)
                while new[i] is not None:
                    i = self.wrap(i+1, len(new))
                new[i] = key
        self.table = new


    wrap = lambda self, i, size: (i+size)%size


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = key%len(self.table)
        while self.table[i] != '*' and self.table[i] is not None and self.table[i][0] != key:
            i = self.wrap(i+1, len(self.table))
        if self.table[i] is None or self.table[i] == '*':
            self.table[i] = [key, value]
            self.capacity += 1
        elif self.table[i][0] == key:
            self.table[i][1] = value
            return
        if self.capacity > (len(self.table)//4*3):
            self._expand()
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = key%len(self.table)
        while self.table[i] is not None and (self.table[i] == '*' or self.table[i][0] != key):
            i = self.wrap(i+1, len(self.table))
        if self.table[i] is None:
            return -1
        if self.table[i][0] == key:
            return self.table[i][1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = key%len(self.table)
        while self.table[i] is not None and (self.table[i] == '*' or self.table[i][0] != key):
            i = self.wrap(i+1, len(self.table))
        if self.table[i] is None:
            return
        if self.table[i][0] == key:
            self.table[i] = '*'
            self.capacity -= 1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)