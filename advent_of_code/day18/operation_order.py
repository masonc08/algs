class OperationOrder:
    def __init__(self):
        self.lines = None

    def read_equations(self):
        if self.lines is None:
            with open('./advent_of_code/day18/equations.txt') as reader:
                self.lines = [ line.strip() for line in reader.readlines() ]
        return self.lines

    def calculate(self, a, b, op):
        if op == '+':
            return a+b
        elif op == '*':
            return a*b
        else:
            raise Exception('Incorrect operand in op')

    def part1(self):
        equations = self.read_equations()
        sol = 0
        for equation in equations:
            cur, op, stk = 0, '+', []
            for c in equation:
                if c.isnumeric():
                    c = int(c)
                    cur = self.calculate(cur, c, op)
                elif c == '+' or c == '*':
                    op = c
                elif c == '(':
                    stk += (cur, op),
                    cur, op = 0, '+'
                elif c == ')':
                    a, op = stk.pop()
                    cur = self.calculate(cur, a, op)
                elif c != ' ':
                    raise Exception("Unexpected input")
            sol += cur
        return sol

    def part2(self):
        equations = self.read_equations()
        sol = 0
        for equation in equations:
            cur, op, stk = 1, '*', []
            for c in equation:
                if c.isnumeric():
                    c = int(c)
                    cur = self.calculate(cur, c, op)
                elif c == '+':
                    op = c
                elif c == '*':
                    if stk and stk[-1][1] == '*':
                        a, op = stk.pop()
                        cur = self.calculate(cur, a, op)
                    op = c
                    stk += (cur, op),
                    cur, op = 1, '*'
                elif c == '(':
                    if stk and stk[-1][1] == '*' == op:
                        stk[-1] = (stk[-1][0], '*(')
                    else:
                        stk += (cur, op+c),
                    cur, op = 1, '*'
                elif c == ')':
                    while len(stk[-1][1]) != 2:
                        a, op = stk.pop()
                        cur = self.calculate(cur, a, op)
                    if stk[-1][1][0] == '+':
                        a, op = stk.pop()
                        cur = self.calculate(cur, a, op[0])
                    else:
                        stk[-1] = (stk[-1][0], '*')
                elif c != ' ':
                    raise Exception("Unexpected input")
            while stk:
                cur *= stk.pop()[0]
            sol += cur
        return sol
