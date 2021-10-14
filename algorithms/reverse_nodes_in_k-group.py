"""
Leetcode 25

"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length(node):
            i = 0
            while node:
                node, i = node.next, i+1
            return i
        def reverse(node, k):
            prev = None
            for _ in range(k):
                tmp = node.next
                node.next = prev
                prev, node = node, tmp
            return prev, node
        L, start, run = get_length(head), head, self
        for _ in range(L//k):
            tmp = start
            run.next, start = reverse(start, k)
            run = tmp
        run.next = start
        return self.next
