"""
Leetcode 139
Runtime: 36 ms, faster than 79.60% of Python3 online submissions for Word Break.
Memory Usage: 14.2 MB, less than 68.89% of Python3 online submissions for Word Break.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            dp[i] = any([dp[j] and s[j:i] in wordDict for j in range(i)])
        return dp[-1]


    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:

    #     class TrieNode:
    #         def __init__(self, c, children, end=False):
    #             self.children = children
    #             self.end = end
    #             self.c = c 

    #     trie = TrieNode('', {})
    #     for word in wordDict:
    #         runner = trie
    #         for c in word:
    #             tmp = runner.children.get(c, TrieNode(c, {}))
    #             runner.children[c] = tmp
    #             runner = tmp
    #         runner.end = True

    #     def dfs(node, i=0):
    #         c = s[i]
    #         if c in node.children:
    #             child = node.children[c]
    #             if child.end and i != len(s)-1 and dfs(trie, i+1):
    #                 return True
    #             if child.end and i == len(s)-1:
    #                 return True
    #             if i != len(s)-1:
    #                 return dfs(child, i+1)
    #         return False

    #     return dfs(trie)
