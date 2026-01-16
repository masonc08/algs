import pathlib, collections

def part2():
    with open(str(pathlib.Path(__file__).parent.resolve()) + "/in.txt") as f:
        lines = f.readlines()
    lines = [ line.strip() for line in lines ]
    lines = [ tuple(map(int, line.split())) for line in lines ]
    safe = collections.Counter() 
    for nums in lines:
        L = len(nums)
        last_diff = 0
        removed = False
        i = 0
        while i < L:
            if i == L-1:
                safe[tuple(nums)] += 1
                break
            a, b = nums[i], nums[i+1]
            diff = b-a
            if diff*last_diff < 0 or abs(diff) > 3 or diff == 0:
                if removed or i >= L-2:
                    break
                c = nums[i+2]
                diff = c-a
                if diff*last_diff < 0 or abs(diff) > 3 or diff == 0:
                    break
                removed = True
                i += 1
            last_diff = diff
            i += 1
    return safe
        
print(part2())