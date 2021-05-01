"""
Leetcode 745
May Leetcoding challenge
Runtime: 2896 ms, faster than 5.26% of Python3 online submissions for Prefix and Suffix Search.
Memory Usage: 79.5 MB, less than 22.37% of Python3 online submissions for Prefix and Suffix Search.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class TrieNode:

    def __init__(self, i):
        self.children = {}
        self.i = i

    def insert(self, key, i):
        runner = self
        for c in key:
            runner.children[c] = runner.children.get(c, TrieNode(i))
            runner = runner.children[c]
            runner.i = i

    def get(self, key, default):
        runner = self
        for c in key:
            if c not in runner.children:
                return default
            runner = runner.children[c]
        return runner.i


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = TrieNode(-1)
        for i, word in enumerate(words):
            L = len(word)
            for j in range(L+1):
                key = f'{word[L-j:]}#{word}'
                self.trie.insert(key, i)

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.get(f'{suffix}#{prefix}', -1)
