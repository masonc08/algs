"""
Leetcode 430

"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def helper(runner):
            while runner:
                if runner.child:
                    child_tail = helper(runner.child)
                    a, b, c, d = runner, runner.child, child_tail, runner.next
                    a.next, b.prev = b, a
                    if d:
                        c.next, d.prev = d, c
                    runner.child = None
                    runner = child_tail
                if runner.next:
                    runner = runner.next
                else:
                    break
            return runner

        helper(head)
        return head
