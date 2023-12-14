OPEN_LEFT = ("-", "J", "7")
OPEN_RIGHT = ("-", "L", "F")
OPEN_DOWN = ("|", "7", "F")
OPEN_UP = ("|", "L", "J")

def load_maze():
    with open("advent_of_code/2023/day10/in.txt") as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]

def part1():
    maze = load_maze()
    n, m = len(maze), len(maze[0])

    def get_start():
        for i in range(n):
            for j in range(m):
                if maze[i][j] == "S":
                    return i, j
        raise Exception("No start point found")
    
    def get_adjacent(i, j, init=0):
        adj = []
        pipe = maze[i][j]
        if i != 0 and (init or pipe in OPEN_UP) and maze[i-1][j] in OPEN_DOWN:
            adj.append((i-1, j))
        if i != n-1 and (init or pipe in OPEN_DOWN) and maze[i+1][j] in OPEN_UP:
            adj.append((i+1, j))
        if j != 0 and (init or pipe in OPEN_LEFT) and maze[i][j-1] in OPEN_RIGHT:
            adj.append((i, j-1))
        if j != m-1 and (init or pipe in OPEN_RIGHT) and maze[i][j+1] in OPEN_LEFT:
            adj.append((i, j+1))
        return adj
    path = set()

    start = get_start()
    path.add(start)
    adj = get_adjacent(*start, 1)
    assert len(adj) == 2
    maze[start[0]][start[1]] = "."
    a, b = adj
    sol = 1
    while a != b:
        sol += 1
        adj = get_adjacent(*a)
        maze[a[0]][a[1]] = "."
        path.add(a)
        assert len(adj) == 1
        a = adj[0]
        adj = get_adjacent(*b)
        maze[b[0]][b[1]] = "."
        path.add(b)
        assert len(adj) == 1
        b = adj[0]
    path.add(a)
    path.add(b)
    return sol, path

def part2():
    maze = load_maze()
    _, path = part1()
    n, m = len(maze), len(maze[0])
    sol = 0
    for i, line in enumerate(maze):
        j = 0
        inside = False
        while j < m:
            if (i, j) in path:
                if line[j] == "|":
                    inside = not inside
                elif line[j] in OPEN_RIGHT:
                    opening = line[j]
                    j += 1
                    while j < m and line[j] == "-":
                        j += 1
                    ending = line[j]
                    if (opening, ending) in (("L", "7"), ("F", "J")):
                        inside = not inside
            else:
                sol += inside
            j += 1
    return sol



print(part2())