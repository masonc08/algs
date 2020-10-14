# Leetcode 61


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        self.k = k
        self.head = head
        _, new_head, _ = self._rotateRight(head, 0)
        head = new_head
        return head

    def _rotateRight(self, node, clen):
        if node == None:
            self.k %= clen
            if self.k == 0:
                return clen, self.head, True
            return clen, None, False
        mlen, new_head, done = self._rotateRight(node.next, clen+1)
        if done:
            return mlen, new_head, done
        if clen == mlen-1 and self.k != 0:
            node.next = self.head
        if mlen-self.k == clen:
            return mlen, node, False
        if mlen-1-self.k == clen:
            node.next = None
            return mlen, new_head, True
        return mlen, new_head, done



l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# e = []
# run = l
# while run:
#     e.append(run.val)
#     run = run.next
# print(e)
s = Solution().rotateRight(l, 2)
# e = []
# run = s
# i = 0
# while run:
#     e.append(run.val)
#     run = run.next
#     i += 1
#     if i == 10:
#       break
# print(e)