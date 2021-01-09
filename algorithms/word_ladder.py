"""
Leetcode 127
January Leetcoding challenge
Runtime: 100 ms, faster than 94.40% of Python3 online submissions for Word Ladder.
Memory Usage: 17.7 MB, less than 41.30% of Python3 online submissions for Word Ladder.
"""


import collections


class Solution:
    """
    S = average length of each string, N = input size
    O(NMM) runtime, O(NNM) space
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_li = self.get_adj_li(set(wordList + [beginWord]))
        stk, visited, sol = [beginWord], set([beginWord]), 1
        while stk:
            new = []
            while stk:
                node = stk.pop()
                L = len(node)
                for i in range(L):
                    struct = node[:i] + '_' + node[i+1:]
                    for nbr in adj_li[struct]:
                        if nbr not in visited:
                            if nbr == endWord:
                                return sol+1
                            new += nbr,
                            visited.add(nbr)
            stk, sol = new, sol+1
        return 0

    def get_adj_li(self, words):
        adj_li = collections.defaultdict(list)
        for word in words:
            L = len(word)
            for i in range(L):
                struct = word[:i] + '_' + word[:i+1]
                adj_li[struct] += word,
        return adj_li

    """
    S = average length of each string, N = input size
    O(NNM) runtime, O(NN) space
    TLE
    """
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     wordList += beginWord, endWord
    #     L = len(wordList)
    #     adj_li = self.get_adj_li(set(wordList), L)
    #     stk, visited, sol = [L-1], set([L-1]), 1
    #     while stk:
    #         new = []
    #         while stk:
    #             node = stk.pop()
    #             for nbr in adj_li[node]:
    #                 if nbr not in visited:
    #                     if wordList[nbr] == endWord:
    #                         return sol+1
    #                     new += nbr,
    #                     visited.add(nbr)
    #         stk, sol = new, sol+1
    #     return 0

    # def get_adj_li(self, words, L):
    #     adj_li = [set() for _ in range(L)]
    #     for i, s in enumerate(words):
    #         for j in range(i+1, L):
    #             s1 = words[j]
    #             if self.is_one_off(s, s1):
    #                 adj_li[i].add(j)
    #                 adj_li[j].add(i)
    #     return adj_li

    # def is_one_off(self, a, b):
    #     if len(a) != len(b):
    #         return False
    #     edit = False
    #     for c1, c2 in zip(a, b):
    #         if c1 != c2:
    #             if not edit:
    #                 edit = True
    #             else:
    #                 return False
    #     return edit
