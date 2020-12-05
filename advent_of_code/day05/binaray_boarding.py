class BinaryBoarding:
    def get_seats(self):
        with open('./advent_of_code/day05/seats.txt') as reader:
            lines = reader.readlines()
        return [ line.strip() for line in lines ]


    def get_row(self, seat):
        lo, hi = 0, 127
        for i in range(7):
            c = seat[i]
            m = (lo+hi)//2
            if c == 'F':
                hi = m
            elif c == 'B':
                lo = m+1
            else:
                raise Exception(f"Expected F or B but saw {c}")
        return lo


    def get_column(self, seat):
        lo, hi = 0, 7
        for i in range(7, 10):
            c = seat[i]
            m = (lo+hi)//2
            if c == 'L':
                hi = m
            elif c == 'R':
                lo = m+1
            else:
                raise Exception(f"Expected L or R but saw {c}")
        return lo


    def part1(self):
        seats = self.get_seats()
        sol = 0
        for seat in seats:
            sol = max(sol, self.get_row(seat)*8+self.get_column(seat))
        return sol


    def part2(self):
        seats = self.get_seats()
        plane = [[False]*8 for _ in range(128)]
        for seat in seats:
            row, column = self.get_row(seat), self.get_column(seat)
            plane[row][column] = True
        for i, row in enumerate(plane):
            out = False
            vacant = -1
            for j, occupied in enumerate(row):
                if not occupied:
                    if vacant == -1:
                        vacant = j
                    else:
                        out = True
                        break
            if not out and vacant != -1:
                return i*8+vacant
        raise Exception("Did not find the vacant seat")
