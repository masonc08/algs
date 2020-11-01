"""
Leetcode 1290
November Leetcoding Challenge #1
Runtime: 28 ms, faster than 79.99% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sol = 0
        while head:
            sol <<= 1
            sol |= head.val
            head = head.next
        return sol
