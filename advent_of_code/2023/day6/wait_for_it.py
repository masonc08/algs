def get_data():
    with open("advent_of_code/2023/day6/in.txt") as f:
        lines = f.readlines()
    time_line, distance_line = lines
    time_line = time_line.strip().split()[1:]
    distance_line = distance_line.strip().split()[1:]
    data = []
    for time, distance in zip(time_line, distance_line):
        data.append((int(time), int(distance)))
    return data

def get_distance(hold_down_time, total_time):
    moving_time = total_time - hold_down_time
    speed = hold_down_time
    return speed*moving_time

def part1():
    data = get_data()
    sol = 1
    for time, dist in data:
        start, end = 0, time//2+1
        while start < end:
            mid = (start+end)//2
            if dist < get_distance(mid, time):
                end = mid
            elif dist >= get_distance(mid, time):
                start = mid+1
        ways_to_win = (time//2-start+(time%2))*2 + (time%2 == 0)
        sol *= ways_to_win
    return sol

print(part1())