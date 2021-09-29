"""
Leetcode 725
September Leetcoding challenge
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def get_length(node, i=0):
            while node:
                node, i = node.next, i+1
            return i
        L = get_length(head)
        size, largeruntil, sol = L//k, L%k, [None]*k
        for i in range(k):
            end = L//k+1 if i < largeruntil else L//k
            for j in range(end):
                if sol[i] is None:
                    sol[i] = head
                if j == end-1:
                    tmp = head.next
                    head.next = None
                    head = tmp
                else:
                    head = head.next
        return sol
