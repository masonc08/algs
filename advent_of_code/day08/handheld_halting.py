class HandheldHalting:
    def __init__(self):
        self.loop_path = None
        self.instructions = None


    def get_instructions(self):
        if self.instructions is None:
            with open('./advent_of_code/day08/instructions.txt') as reader:
                instructions = reader.readlines()
            self.instructions = [ instruction.split() for instruction in instructions ]
        return self.instructions


    def traverse(self, instructions, i=0, visited=set(), path=[]):
        while i not in visited and i < len(instructions):
            visited.add(i)
            cmd, param = instructions[i]
            param = int(param)
            cur = 0 if len(path) == 0 else path[-1][-1]
            if cmd == "acc":
                path.append((i, cur+param))
                i += 1
            elif cmd == "jmp":
                path.append((i, cur))
                i += param
            elif cmd == "nop":
                path.append((i, cur))
                i += 1
            else:
                raise Exception("Invalid instruction")
        return path, i < len(instructions)


    def get_loop_path(self):
        if self.loop_path is None:
            instructions = self.get_instructions()
            loop_path, is_loop = self.traverse(instructions)
            if not is_loop:
                raise Exception("No loop detected")
            self.loop_path = loop_path
        return self.loop_path


    def part1(self):
        return self.get_loop_path()[-1][-1]


    def part2(self):
        loop_path = self.get_loop_path()
        instructions = self.get_instructions()
        seen = set([ visited for visited, _ in loop_path ])
        for idx, v in enumerate(loop_path):
            i, _ = v
            cmd, param = instructions[i]
            param = int(param)
            if cmd == "jmp" or cmd == "nop":
                cur_path, is_loop = self.traverse(instructions, (i+1) if cmd == "jmp" else (i+param), seen, loop_path[:idx+1])
                if not is_loop:
                    return cur_path[-1][-1]
            elif cmd == "acc":
                continue
            else:
                raise Exception("Invalid instruction")
        raise Exception("No way to terminate program")
