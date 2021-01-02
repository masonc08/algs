"""
Daily Coding Problem #6
https://i.imgur.com/bcpOfH6.png
"""


get_pointer = lambda x: 0x7fffffff
dereference_pointer = lambda x: XORNode()

class XORNode:
    def __init__(self, v=0, prev=None, next=None):
        self.v = v
        self.hash = 0
        self.add_nbr(prev)
        self.add_nbr(next)

    def add_nbr(self, nbr=None):
        nbr = get_pointer(nbr) if nbr else 0
        self.hash ^= nbr

    def remove_nbr(self, nbr=None):
        self.add_nbr(nbr)

    def get_nbr(self, nbr=None):
        addr = get_pointer(nbr) if nbr else 0
        return dereference_pointer(self.hash^addr)

class XORLinkedList:
    def __init__(self):
        self.head = XORNode()
        self.tail = XORNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, v):
        prev = self.tail.get_nbr(0)
        self.tail.remove_nbr(prev)
        prev.remove_nbr(self.tail)
        new = XORNode(v, prev=prev, next=self.tail)
        prev.add_nbr(new)
        self.tail.add_nbr(new)

    def get(self, e):
        p = self.head
        run = self.head.get_nbr(0)
        for _ in range(e):
            p, run = run, run.get_nbr(p)
        return run
