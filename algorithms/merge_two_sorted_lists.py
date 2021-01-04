"""
Leetcode 21
January Leetcoding challenge
Runtime: 36 ms, faster than 74.67% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.3 MB, less than 25.77% of Python3 online submissions for Merge Two Sorted Lists.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.next = None
        tail = self
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next , l2 = l2, l2.next
            tail = tail.next
            tail.next = None
        tail.next = l1 or l2 or None
        return self.next
