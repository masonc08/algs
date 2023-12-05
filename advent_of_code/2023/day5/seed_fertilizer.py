def get_seeds(s):
    return tuple(map(int, s.split()[1:]))

def get_seeds_interval(s):
    li = tuple(map(int, s.split()[1:]))
    intervals = []
    for i in range(0, len(li), 2):
        intervals.append((s[i], s[i+1]))
    return intervals

def get_mappings(s):
    mappings = []
    for block in s:
        mapping = []
        for line in block.split("\n")[1:]:
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
    with open("advent_of_code/2023/day5/in_sample.txt") as f:
        lines = f.read()
    blocks = lines.split("\n\n")
    seeds_line = blocks[0].strip()
    mapping_lines = blocks[1:]
    seed_intervals = get_seeds_interval(seeds_line)
    mappings = get_mappings(mapping_lines)
    
    sol = 0x7fffffff

    def translate_interval(start, end, mappings, i):
        if i == len(mappings):
            sol = min(sol, start)
        mapping = mappings[i]
        for j, (dest_bound, start_bound, range) in enumerate(mapping[1:]):
            if start < start_bound:
                last_mapping = mapping[j-1]
                last_start_bound = last_mapping[1]
                last_range = last_mapping[2]
                last_source_bound_end = last_start_bound + last_range
                translate_interval(last_source_bound_end+1, min(end), mappings, i+1)
                return
            if start < start_bound:
                translate_interval(start, start_bound-1)
                if end <= start_bound+range:
                    translate_interval(dest_bound, dest_bound+(start_bound+range-end))
                elif end > start_bound+range:
                    translate_interval(dest_bound, dest_bound+range)

    for start, end in seed_intervals:
        translate_interval(start, end, mappings, 0)


print(part1())