"""
Leetcode 1721
Leetcode weekly contest 223
O(n) runtime, O(1) space
Runtime: 1712 ms, faster than 100.00% of Python3 online submissions for Swapping Nodes in a Linked List.
Memory Usage: 48.9 MB, less than 100.00% of Python3 online submissions for Swapping Nodes in a Linked List.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_len(self, node):
        i = 0
        while node:
            node = node.next
            i += 1
        return i

    def get(self, node, i):
        i -= 1
        for _ in range(i):
            node = node.next
        return node

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        L = self.get_len(head)
        a, b = self.get(head, k), self.get(head, L-k+1)
        a.val, b.val = b.val, a.val
        return head
