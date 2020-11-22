"""
Leetcode 804
November Leetcoding challenge
Runtime: 32 ms, faster than 78.35% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 14.3 MB, less than 11.47% of Python3 online submissions for Unique Morse Code Words.
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        sol = set()
        for word in words:
            sb = [None]*len(word)
            for j, c in enumerate(word):
                sb[j] = mp[ord(c)-ord('a')]
            sol.add(''.join(sb))
        return len(sol)
