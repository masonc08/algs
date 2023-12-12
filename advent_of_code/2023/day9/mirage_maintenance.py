def extrapolate_next(nums):
    if all(v == 0 for v in nums):
        return 0
    L = len(nums)
    nex = tuple(nums[i+1]-nums[i] for i in range(L-1))
    sol = extrapolate_next(nex)
    # return nex[0] + sol
    return nex[0] - sol

def part1():
    with open("advent_of_code/2023/day9/in.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    sol = 0
    for line in lines:
        nums = tuple(map(int, line.split()))
        # sol += nums[-1] + extrapolate_next(nums)
        sol += nums[0] - extrapolate_next(nums)
    return sol

print(part1())