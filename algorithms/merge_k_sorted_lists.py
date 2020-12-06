"""
Leetcode 23
"""


import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    O(nlgk) runtime, O(1) space by divide and conquer
    Runtime: 116 ms, faster than 46.77% of Python3 online submissions for Merge k Sorted Lists.
    Memory Usage: 17.7 MB, less than 74.28% of Python3 online submissions for Merge k Sorted Lists.
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        rem = len(lists)
        interval = 2
        while interval <= rem:
            j = 0
            for i in range(0, rem, interval):
                if i+1 == rem:
                    lists[j] = lists[i]
                else:
                    lists[j] = self._merge(lists[i], lists[i+1])
                j += 1
            rem = j
        return lists[0] if rem == 1 else None


    def _merge(self, l1, l2):
        d = ListNode()
        runner = d
        while l1 and l2:
            if l1.val > l2.val:
                runner.next = l2
                l2 = l2.next
                runner = runner.next
                runner.next = None
            else:
                runner.next = l1
                l1 = l1.next
                runner = runner.next
                runner.next = None
        if l1:
            runner.next = l1
        elif l2:
            runner.next = l2
        return d.next


    """
    Runtime: 92 ms, faster than 92.70% of Python3 online submissions for Merge k Sorted Lists.
    Memory Usage: 18 MB, less than 41.08% of Python3 online submissions for Merge k Sorted Lists.
    """
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     self.next = None
    #     runner = self
    #     heap = [ (head.val, i, head) for i, head in enumerate(lists) if head ]
    #     heapq.heapify(heap)
    #     i = len(lists)
    #     while heap:
    #         _, _, top = heapq.heappop(heap)
    #         tmp = top.next
    #         runner.next = top
    #         runner = runner.next
    #         runner.next = None
    #         if tmp:
    #             heapq.heappush(heap, (tmp.val, i, tmp))
    #             i += 1
    #     return self.next
