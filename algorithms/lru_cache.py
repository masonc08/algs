"""
Leetcode 146
O(1) getting and putting, O(c) space, where c is the capacity
Runtime: 212 ms, faster than 46.86% of Python3 online submissions for LRU Cache.
Memory Usage: 23.8 MB, less than 21.64% of Python3 online submissions for LRU Cache.
"""


class Node:
    def __init__(self, k=-1, v=-1, pre=None, nex=None):
        self.k, self.v, self.pre, self.nex = k, v, pre, nex


class LRUCache:
    def __init__(self, capacity: int):
        self.keys, self.cap = {}, capacity
        self.head, self.tail = Node(), Node()
        self.tail.next, self.head.pre = self.head, self.tail

    def _remove(self, b):
        a, c = b.pre, b.nex
        a.nex, c.pre = c, a
        b.nex = b.pre = None
        del self.keys[b.k]

    def _insert(self, b):
        a, c = self.head.pre, self.head
        a.nex = c.pre = b
        b.pre, b.nex = a, c
        self.keys[b.k] = b

    def get(self, key: int) -> int:
        if key in self.keys:
            node = self.keys[key]
            self._remove(node)
            self._insert(node)
            return node.v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.get(key)
            self.head.pre.v = value
            return
        len(self.keys) == self.cap and self._remove(self.tail.nex)
        self._insert(Node(k=key, v=value))
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# class Node:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None


# class LRUCache:
#     def __init__(self, capacity: int):
#         if capacity < 0:
#             raise Exception()
#         self.capacity = capacity
#         self.head = Node(0, 0)
#         self.tail = Node(0, 0)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.mp = {}

#     def get(self, key: int) -> int:
#         if key in self.mp:
#             node = self.mp[key]
#             self._remove(node)
#             self._add(node)
#             return node.val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.mp:
#             self._remove(self.mp[key])
#         node = Node(key, value)
#         self._add(node)
#         self.mp[key] = node
#         if len(self.mp) > self.capacity:
#             n = self.head.next
#             self._remove(n)
#             del self.mp[n.key]

#     def _remove(self, node):
#         prev = node.prev
#         next_node = node.next
#         prev.next = next_node
#         next_node.prev = prev

#     def _add(self, node):
#         p = self.tail.prev
#         p.next = node
#         self.tail.prev = node
#         node.prev = p
#         node.next = self.tail


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)