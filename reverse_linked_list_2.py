# Leetcode 92

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n or head is None or head.next is None:
            return head
        i = 0
        self.next = head
        runner = self
        while i < m-1:
            runner = runner.next
            i += 1
        a, b = runner, runner.next
        pre = runner
        runner = runner.next
        i += 1
        while i < n:
            pre, runner.next, runner = runner, pre, runner.next
            i += 1
        c, d = runner, runner.next
        pre, runner.next, runner = runner, pre, runner.next
        a.next, b.next = c, d
        return self.next

l = Solution().reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 2, 4)
i = 0
s = []
while i < 10 and l:
    s.append(l.val)
    l = l.next
    i += 1
print(s)