def part1():
    with open("advent_of_code/2023/day2/in.txt") as f:
        lines = f.readlines()
    sol = 0
    for line in lines:
        line = line.strip()
        rounds = line.split(": ")[-1]
        game_number = int(line.split(": ")[0].split(" ")[-1])
        if is_game_possible(rounds):
            sol += game_number 
    return sol

def is_game_possible(rounds):
    for round in rounds.split("; "):
        if not is_round_possible(round):
            return False
    return True


def is_round_possible(round):
    for quant_and_die in round.split(", "):
        quantity, die = quant_and_die.split(" ")
        quantity = int(quantity)
        if die == "red" and quantity > 12:
            return False
        elif die == "green" and quantity > 13:
            return False
        elif die == "blue" and quantity > 14:
            return False
        elif die not in ("red", "green", "blue"):
            raise Exception("unexpected color: " + quant_and_die)
    return True

def part2():
    with open("advent_of_code/2023/day2/in.txt") as f:
        lines = f.readlines()
    sol = 0
    for line in lines:
        line = line.strip()
        rounds = line.split(": ")[-1]
        sol += get_power(rounds)
    return sol

def get_power(rounds):
    max_red = max_blue = max_green = 0
    for round in rounds.split("; "):
        for quant_and_die in round.split(", "):
            quantity, die = quant_and_die.split(" ")
            quantity = int(quantity)
            if die == "red":
                max_red = max(max_red, quantity)
            elif die == "blue":
                max_blue = max(max_blue, quantity)
            elif die == "green":
                max_green = max(max_green, quantity)
            else:
                raise Exception("unexpected color: " + quant_and_die)
    return max_red*max_blue*max_green

print(part2())