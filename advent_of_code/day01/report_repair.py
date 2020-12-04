class ReportRepair:
    def get_lines(self):
        with open('./advent_of_code/day01/expense_report.txt') as reader:
            lines = reader.readlines()
        return [ int(line.strip()) for line in lines ]


    def part1(self):
        nums = self.get_lines()
        seen = set()
        T = 2020
        for num in nums:
            diff = T-num
            if diff in seen:
                return num*diff
            seen.add(num)
        raise Exception()

    def part2(self):
        nums = self.get_lines()
        nums.sort()
        T = 2020
        for i in range(len(nums)-2):
            a = nums[i]
            s, e = i+1, len(nums)-1
            while s <= e:
                b, c = nums[s], nums[e]
                if a+b+c == T:
                    return a*b*c
                elif a+b+c < T:
                    s += 1
                else:
                    e -= 1
        raise Exception()



print(ReportRepair().part2())