class CustomCustoms:
    def get_responses(self):
        with open('./advent_of_code/day06/responses.txt') as reader:
            lines = reader.read()
        return [ line.split() for line in lines.split('\n\n') ]

    def part1(self):
        responses = self.get_responses()
        sol = 0
        for response in responses:
            answered = set()
            for person in response:
                answered.update(person)
            sol += len(answered)
        return sol


    def part2(self):
        responses = self.get_responses()
        sol = 0
        for response in responses:
            answered = set([ chr(i+ord('a')) for i in range(26) ])
            for person in response:
                answered.intersection_update(person)
            sol += len(answered)
        return sol


print(CustomCustoms().part2())
