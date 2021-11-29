import re
import collections


class HandyHaversacks:
    class Rule:
        def __init__(self, s):
            self.bag, s = s.split(" bags contain ")
            self.holds = {}
            self.total = None
            if "no other bags" in s:
                return
            contents = re.split(r' bags?[.,] ?', s)
            for content in contents:
                # Sample `content`: ['1 wavy lime', '1 vibrant green', '3 light yellow', '']
                if content:
                    qty = int(content[0])
                    bag_type = content[2:]
                    self.holds[bag_type] = qty


    OWN_BAG = "shiny gold"


    def get_rules(self):
        with open('./advent_of_code/day07/rules.txt') as reader:
            lines = reader.readlines()
        rules = [ self.Rule(line.strip()) for line in lines ]
        return dict([ (rule.bag, rule) for rule in rules ])


    def part1(self):
        rules = self.get_rules()
        adj_list = collections.defaultdict(set)
        for rule in rules:
            rule = rules[rule]
            for contains in rule.holds:
                adj_list[contains].add(rule.bag)
        seen = set()
        q = collections.deque([self.OWN_BAG])
        while q:
            bag = q.pop()
            seen.add(bag)
            for can_hold in adj_list[bag]:
                (can_hold not in seen) and q.appendleft(can_hold)
        return len(seen)-1


    def part2(self):
        rules = self.get_rules()
        def dfs(bag):
            sol = 0
            bag = rules[bag]
            if bag.total is not None:
                return bag.total
            for hold in bag.holds:
                sol += (bag.holds[hold]*(1+dfs(hold)))
            bag.total = sol
            return sol
        return dfs(self.OWN_BAG)
