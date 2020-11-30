"""
Leetcode 1171
Runtime: 48 ms, faster than 43.24% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
Memory Usage: 14.7 MB, less than 15.92% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
"""


import collections


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        self.next = head
        self.val = 0
        mp = collections.OrderedDict()
        runner = self
        cur = 0
        while runner:
            cur += runner.val
            node = mp.get(cur, runner)
            while cur in mp:
                mp.popitem()
            mp[cur] = node
            node.next = runner.next
            runner = runner.next
        return self.next
