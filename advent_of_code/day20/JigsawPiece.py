class JigsawPiece:
    def __init__(self, tile_num, pattern):
        self.used = False
        self.tile_num = tile_num
        if not pattern or len(pattern) == 0 or len(pattern[0]) == 0:
            raise Exception("Invalid input")
        self.pattern = pattern
        top, bottom = pattern[0], pattern[-1][::-1]
        left = ''.join([ pattern[i][0] for i in range(len(pattern)-1, -1, -1) ])
        right = ''.join([ pattern[i][-1] for i in range(len(pattern)) ])
        self.sides = [ top, right, bottom, left ]

    @property
    def top(self):
        return self.sides[0]

    @property
    def right(self):
        return self.sides[1]

    @property
    def bottom(self):
        return self.sides[2]

    @property
    def left(self):
        return self.sides[3]

    def rotate(self):
        def subarray_reverse(i=0, j=len(self.sides)-1):
            while i < j:
                self.sides[i], self.sides[j] = self.sides[j], self.sides[i]
                i, j = i+1, j-1
        for _ in range(4):
            yield
            subarray_reverse()
            subarray_reverse(1)
            self.pattern = [ ''.join(arr) for arr in zip(*self.pattern[::-1]) ]
        self.pattern = [ line[::-1] for line in self.pattern ]
        top, bottom = self.pattern[0], self.pattern[-1][::-1]
        left = ''.join([ self.pattern[i][0] for i in range(len(self.pattern)-1, -1, -1) ])
        right = ''.join([ self.pattern[i][-1] for i in range(len(self.pattern)) ])
        self.sides = [ top, right, bottom, left ]
        for _ in range(4):
            yield
            subarray_reverse()
            subarray_reverse(1)
            self.pattern = [ ''.join(arr) for arr in zip(*self.pattern[::-1]) ]
