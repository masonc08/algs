import pathlib

def part1():
    with open(str(pathlib.Path(__file__).parent.resolve()) + "/in.txt") as f:
        lines = f.readlines()
    lines = [ line.strip() for line in lines ]
    lines = [ tuple(map(int, line.split())) for line in lines ]
    safe = 0
    for nums in lines:
        L = len(nums)
        last_diff = 0
        for i in range(L):
            if i == L-1:
                safe += 1
                break
            a, b = nums[i], nums[i+1]
            diff = b-a
            if diff*last_diff < 0 or abs(diff) > 3 or diff == 0:
                break
            last_diff = diff
    return safe
        
print(part1())