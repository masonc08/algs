"""
Leetcode 2
January Leetcoding challenge
Runtime: 64 ms, faster than 89.71% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.4 MB, less than 11.42% of Python3 online submissions for Add Two Numbers.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.next, run, c = None, self, 0
        while l1 or l2 or c:
            a, b = l1.val if l1 else 0, l2.val if l2 else 0
            v = a+b+c
            run.next, c = ListNode(v%10), v//10
            l1, l2, run = l1 and l1.next, l2 and l2.next, run.next
        return self.next
