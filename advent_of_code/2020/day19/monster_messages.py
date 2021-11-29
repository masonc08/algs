import functools

class MonsterMessages:
    def __init__(self):
        self.rules = []
        self.strings = []

    def read_input(self):
        if not self.rules or not self.strings:
            # Note: the input.txt file has the modified version of the data from part 2.
            # The data will not work to give the correct solution for part 1.
            with open('./advent_of_code/day19/input.txt') as reader:
                rules_unparsed, strings_unparsed = reader.read().split('\n\n')
            split_rules = rules_unparsed.split('\n')
            self.rules = ['']*len(split_rules)
            for line in split_rules:
                i, rule = line.split(': ')
                self.rules[int(i)] = rule
            self.strings = strings_unparsed.split()

    @functools.lru_cache(None)
    def follows(self, s, rule_list, rule_i):
        if rule_i == len(rule_list):
            return len(s) == 0
        if len(s) == 0:
            return False
        for i in range(len(s)):
            if self.dfs(s[:i+1], int(rule_list[rule_i])) and self.follows(s[i+1:], rule_list, rule_i+1):
                return True
        return False

    @functools.lru_cache(None)
    def dfs(self, s, rule_y):
        rule = self.rules[rule_y]
        if rule[0] == '"':
            if len(s) == 1 and s == rule[1]:
                return True
            return False
        options = rule.split(' | ')
        for option in options:
            option = tuple(option.split())
            if self.follows(s, option, 0):
                return True
        return False

    def part1(self):
        self.read_input()
        sol = 0
        for s in self.strings:
            if self.dfs(s, 0):
                sol += 1
        return sol

