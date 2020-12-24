"""
Leetcode 24
December Leetcoding challenge
Runtime: 28 ms, faster than 82.02% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14.4 MB, less than 10.51% of Python3 online submissions for Swap Nodes in Pairs.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        self.next = head
        run = self
        while run and run.next and run.next.next:
            a, b, c, d = run, run.next, run.next.next, run.next.next.next
            a.next, b.next, c.next = c, d, b
            run = b
        return self.next


# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None:
#             return head
#         runner = head
#         head = runner.next
#         temp = runner.next.next
#         runner.next.next = runner
#         runner.next = temp
#         while runner and runner.next and runner.next.next:
#             temp = runner.next.next
#             runner.next.next = runner.next.next.next
#             temp.next = runner.next
#             runner.next = temp
#             runner = runner.next.next
#         return head