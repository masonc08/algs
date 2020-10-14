# Leetcode 206

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, runner = None, head
        while runner:
            pre, runner.next, runner = runner, pre, runner.next
        return pre