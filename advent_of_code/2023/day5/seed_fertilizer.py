import functools


def get_seeds(s):
    return tuple(map(int, s.split()[1:]))

def get_seeds_interval(s):
    li = tuple(map(int, s.split()[1:]))
    intervals = []
    for i in range(0, len(li), 2):
        intervals.append((li[i], li[i] + li[i+1]))
    return intervals

def get_mappings(s):
    mappings = []
    for block in s:
        mapping = []
        for line in block.strip().split("\n")[1:]:
            mapping.append(tuple(map(int, line.split())))
        mappings.append(mapping)
        mapping.sort(key=lambda x: x[1])
    return mappings


def translate(mapping, n):
    for dest, start, range in mapping:
        if n < start:
            return n
        if start <= n <= start+range:
            return dest+(n-start)
    return n


def part1():
    with open("advent_of_code/2023/day5/in.txt") as f:
        lines = f.read()
    blocks = lines.split("\n\n")
    seeds_line = blocks[0].strip()
    mapping_lines = blocks[1:]
    seeds = get_seeds(seeds_line)
    mappings = get_mappings(mapping_lines)

    sol = 0x7fffffff
    for seed in seeds:
        prev = seed
        for mapping in mappings:
            new = translate(mapping, prev)
            prev = new
        sol = min(sol, prev)
    return sol

def part2():
    with open("advent_of_code/2023/day5/in_modified.txt") as f:
        lines = f.read()
    blocks = lines.split("\n\n")
    seeds_line = blocks[0].strip()
    mapping_lines = blocks[1:]
    seed_intervals = get_seeds_interval(seeds_line)
    mappings = get_mappings(mapping_lines)

    sol = [111111111111]

    @functools.lru_cache(None)
    def translate_interval(seed_start, seed_end, i):
        if i == len(mappings):
            sol[0] = min(sol[0], seed_start)
            return
        mapping = mappings[i]
        for j, (dest_start, source_start, range) in enumerate(mapping[1:]):
            j = j+1
            source_end = source_start + range
            dest_end = dest_start + range
            if seed_end <= source_start: # Type A
                last_mapping = mapping[j-1]
                prev_source_end = last_mapping[1] + last_mapping[2]
                if prev_source_end < seed_end:
                    translate_interval(max(prev_source_end, seed_start), seed_end, i+1)
            elif seed_start < source_start and seed_end <= source_end: # Type B
                translate_interval(seed_start, source_start, i+1)
                translate_interval(dest_start, dest_start+(seed_end-source_start), i+1)
            elif source_start <= seed_start < seed_end <= source_end: # Type C
                translate_interval(dest_start+(seed_start-source_start), dest_start+(seed_end-source_start), i+1)
            elif source_start <= seed_start < source_end < seed_end: # Type D
                translate_interval(dest_start+(seed_start-source_start), dest_end, i+1)

    for start, end in seed_intervals:
        translate_interval(start, end, 0)
    return sol[0]

print(part2())
