"""
Leetcode 147
November Leetcoding Challenge
Runtime: 2020 ms, faster than 16.99% of Python3 online submissions for Insertion Sort List.
Memory Usage: 15.8 MB, less than 13.84% of Python3 online submissions for Insertion Sort List.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        self.next = None
        while head:
            tmp = head.next
            node = head
            i = self
            while 1:
                if i.next is None:
                    i.next = node
                    node.next = None
                    break
                if i.next.val > node.val:
                    node.next = i.next
                    i.next = node
                    break
                i = i.next
            head = tmp
        return self.next

Solution().insertionSortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))