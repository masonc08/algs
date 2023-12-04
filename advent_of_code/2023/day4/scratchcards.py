def part1():
    with open("advent_of_code/2023/day4/in.txt") as f:
        lines = f.readlines()
    lines = [ line.strip() for line in lines ]
    sol = 0
    games_to_winning_numbers = []
    i = 0
    for line in lines:
        data = line.split(": ")[-1]
        winning_nums, my_nums = data.split(" | ")
        winning_nums = set(map(int, winning_nums.split()))
        my_nums = set(map(int, my_nums.split()))
        my_winning_nums = winning_nums.intersection(my_nums)
        if my_winning_nums:
            sol += 2**(len(my_winning_nums)-1)
        games_to_winning_numbers.append(len(my_winning_nums))
        i += 1
    return games_to_winning_numbers

def part2():
    with open("advent_of_code/2023/day4/in.txt") as f:
        lines = f.readlines()
    lines = [ line.strip() for line in lines ]
    n = len(lines)
    copies = [1]*n
    winning_numbers = part1()
    for i in range(n):
        for j in range(winning_numbers[i]):
            copies[i+j+1] += copies[i]
    return sum(copies)
        

print(part2())
