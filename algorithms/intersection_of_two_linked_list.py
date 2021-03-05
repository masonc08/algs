"""
Leetcode 160
March Leetcoding challenge
Runtime: 172 ms, faster than 30.44% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.4 MB, less than 66.09% of Python3 online submissions for Intersection of Two Linked Lists.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        a, b, loops = headA, headB, 0
        while loops < 3 and (a or b) and  a is not b:
            if not a.next or not b.next:
                loops += 1
            a, b = a.next or headB, b.next or headA
        return a if loops < 3 else None
