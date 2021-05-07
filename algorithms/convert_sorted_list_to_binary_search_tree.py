"""
Leetcode 109
May Leetcoding challenge
Runtime: 128 ms, faster than 74.84% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 17.9 MB, less than 71.52% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return TreeNode(
            mid.val,
            self.sortedListToBST(head),
            self.sortedListToBST(mid.next)
        )

