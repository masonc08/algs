class RambunctiousRecitation:
    def __init__(self):
        self.starting_numbers = None

    def get_starting_numbers(self):
        if not self.starting_numbers:
            with open('./advent_of_code/day15/starting_numbers.txt') as reader:
                lines = reader.readline()
            self.starting_numbers = [ int(num) for num in lines.strip().split(',') ]
        return self.starting_numbers

    def part1(self, lim=2021):
        nums = self.get_starting_numbers()
        dp = {}
        for i, num in enumerate(nums):
            dp[num] = i+1
        last = nums[-1]
        for i in range(len(dp)+1, 30000001):
            tmp = dp.get(last, i-1)
            dp[last] = i-1
            last = i-1-tmp
        return last

    def part2(self):
        return self.part1(30000001)

print(RambunctiousRecitation().part1())