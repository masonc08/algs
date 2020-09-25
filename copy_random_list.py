# Leetcode 138


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        runner = head
        new_head = self
        maker = new_head
        while runner:
            maker.next = Node(runner.val, None, runner)
            maker = maker.next
            temp = runner
            runner = runner.next
            temp.next = maker
        runner = head
        maker = new_head.next
        while maker:
            maker.random = maker.random.random.next if maker.random.random else None
            maker = maker.next
        return new_head.next
