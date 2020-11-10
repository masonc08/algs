"""
Leetcode 832
November Leetcoding Challenge
Runtime: 52 ms, faster than 53.41% of Python3 online submissions for Flipping an Image.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Flipping an Image.
"""


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for image in A:
            for i in range(len(image)//2):
                image[i], image[len(image)-i-1] = (image[len(image)-i-1]+1)%2, (image[i]+1)%2
            if len(image)%2 == 1:
                image[len(image)//2] += 1
                image[len(image)//2] %= 2
        return A
