"""
Leetcode 208
Runtime: 136 ms, faster than 83.40% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 27.7 MB, less than 5.92% of Python3 online submissions for Implement Trie (Prefix Tree).
"""


import collections


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        nested_dd = lambda: collections.defaultdict(nested_dd)
        self.mp = collections.defaultdict(nested_dd)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        runner = self.mp
        for c in word:
            runner = runner[c]
        runner['.'] = None
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        runner = self.mp
        for c in word:
            if c not in runner:
                return False
            runner = runner[c]
        return '.' in runner
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        runner = self.mp
        for c in prefix:
            if c not in runner:
                return False
            runner = runner[c]
        return True
        


# Your Trie object will be instantiated and called as such:
word = "apple"
prefix = "appl"
obj = Trie()
obj.insert(word)
param_2 = obj.search(word+'a')
param_3 = obj.startsWith(prefix)
print(param_2)
print(param_3)