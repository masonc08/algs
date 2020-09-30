# Cracking The Coding Interview #3.1
# Three in One, implement 3 stacks usine one array

class ThreeInOne:
    def __init__(self):
        l = [None]*(2**32-1)
        stacks = (Stack(0, l), Stack(1, l), Stack(2, l))

    def get_stacks(self):
        return stacks


class Stack:
    def __init__(self, counter, l):
        self.i = counter
        self.l = l

    def push(val):
        l[i] = val
        i += 3

    def pop():
        if i-3 < 0:
            raise Exception()
        i -= 3
        ret = l[i]
        l[i] = None
        return ret

    def peek():
        if i-3 < 0:
            raise Exception()
        return l[i-3]

    def is_empty():
        return i-3 < 0