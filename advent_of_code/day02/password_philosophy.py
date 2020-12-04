import collections


class PasswordPhilosophy:

    class Password:
        def __init__(self, s, e, c, pw):
            self.s = s
            self.e = e
            self.c = c
            self.pw = pw


    def get_passwords(self):
        with open('./advent_of_code/day02/password_database.txt') as reader:
            lines = reader.readlines()
        lines = [ line.strip() for line in lines ]
        sol = [None]*len(lines)
        for i in range(len(sol)):
            line = lines[i]
            parts = line.split(" ")
            lims = parts[0].split('-')
            s, e = int(lims[0]), int(lims[1])
            c = parts[1][0]
            sol[i] = self.Password(s, e, c, parts[2].strip())
        return sol


    def part1(self):
        sol = 0
        pws = self.get_passwords()
        for pw in pws:
            cnt = collections.Counter(pw.pw)
            if pw.s <= cnt[pw.c] <= pw.e:
                sol += 1
        return sol


    def part2(self):
        sol = 0
        pws = self.get_passwords()
        for pw in pws: 
            if (pw.pw[pw.s-1] == pw.c) ^ (pw.pw[pw.e-1] == pw.c):
                sol += 1
        return sol


print(PasswordPhilosophy().part2())
