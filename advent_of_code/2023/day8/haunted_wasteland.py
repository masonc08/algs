from itertools import cycle

def load_data():
    with open("advent_of_code/2023/day8/in.txt") as f:
        lines = f.read()
    instruction_block, routes_block = lines.split("\n\n")
    instructions = instruction_block.strip()
    routes_block = routes_block.strip()
    routes = {}
    for route_line in routes_block.split("\n"):
        origin, b = route_line.split(" = (")
        l, r = b[:-1].split(", ")
        routes[origin] = (l, r)
    return instructions, routes

def part1():
    instructions, routes = load_data()
    cur = "AAA"
    sol = 0
    instructions_gen = cycle(instructions)
    while cur != "ZZZ":
        instr = next(instructions_gen)
        l, r = routes[cur]
        cur = l if instr == "L" else r
        sol += 1
    return sol

def part2():
    instructions, routes = load_data()
    instructions_gen = cycle(instructions)
    sol = 0
    cur = [origin for origin in routes if origin[-1] == "A"]
    while any([loc[-1] != "Z" for loc in cur]):
        instr = next(instructions_gen)
        for i, node in enumerate(cur):
            l, r = routes[node]
            cur[i] = l if instr == "L" else r
        sol += 1
    return sol

print(part2())