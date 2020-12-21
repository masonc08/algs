import collections


class AllergenAssessment:
    def __init__(self):
        self.mp = {}
        self.ingredients = collections.Counter()

    def read_ingredients(self):
        if not self.mp or not self.ingredients:
            with open('./advent_of_code/day21/ingredients_list.txt') as reader:
                lines = [line.strip() for line in reader.readlines()]
            for line in lines:
                ingr_list, aller_list = line[:-1].split(' (contains ')
                ingr_list = set(ingr_list.split(' '))
                self.ingredients.update(ingr_list)
                aller_list = aller_list.split(', ')
                for aller in aller_list:
                    if aller in self.mp:
                        self.mp[aller] &= ingr_list
                    else:
                        self.mp[aller] = set(ingr_list)
        return self.mp, self.ingredients

    def solve(self):
        aller_mp, _ = self.read_ingredients()
        allergic_ingredients = {}
        while aller_mp:
            li = list(aller_mp)
            for key in li:
                ingrs = aller_mp[key]
                if len(ingrs) == 1:
                    ingr = next(iter(ingrs))
                    allergic_ingredients[ingr] = key
            for key in list(aller_mp):
                aller_mp[key] -= set(allergic_ingredients)
                if len(aller_mp[key]) == 0:
                    del aller_mp[key]
        sol = 0
        for key in self.ingredients:
            if key not in allergic_ingredients:
                sol += self.ingredients[key]
        li = sorted([ (k, allergic_ingredients[k]) for k in allergic_ingredients ], key=lambda x: x[1])
        li = [ ingr for ingr, _ in li ]
        return sol, ','.join(li)

print(AllergenAssessment().solve())
