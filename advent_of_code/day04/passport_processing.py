import re


class PassportProcessing:
    required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


    def get_passports(self):
        with open('./advent_of_code/day04/passports.txt') as reader:
            lines = reader.read()
        passports = [ line.split() for line in lines.split('\n\n') ]
        i = 0
        for passport in passports:
            new = {}
            for pair in passport:
                k, v = pair.split(':')
                new[k] = v
            passports[i] = new
            i += 1
        return passports


    def has_all_fields(self, passport):
        doesnt_have = set(self.required_fields)
        for key in passport:
            if key in doesnt_have:
                doesnt_have.remove(key)
        return len(doesnt_have) == 0


    def get_passports_has_all_fields(self):
        passports = self.get_passports()
        sol = []
        for passport in passports:
            if self.has_all_fields(passport):
                sol.append(passport)
        return sol


    def validate_passport(self, passport):
        try:
            for k in passport:
                v = passport[k]
                if k == "byr":
                    assert v.isnumeric()
                    assert len(v) == 4
                    assert int(v) >= 1920
                    assert int(v) <= 2002
                elif k == "iyr":
                    assert v.isnumeric() 
                    assert len(v) == 4 
                    assert int(v) >= 2010 
                    assert int(v) <= 2020
                elif k == "eyr":
                    assert v.isnumeric() 
                    assert len(v) == 4
                    assert int(v) >= 2020
                    assert int(v) <= 2030
                elif k == "hgt":
                    unit = v[-2:]
                    v = v[:-2]
                    if unit == "cm":
                        assert v.isnumeric() 
                        assert int(v) >= 150 
                        assert int(v) <= 193
                    elif unit == "in":
                        assert v.isnumeric() 
                        assert int(v) >= 59 
                        assert int(v) <= 76
                    else:
                        raise Exception()
                elif k == "hcl":
                    assert re.match("#[0-9a-f]{6}", v)
                elif k == "ecl":
                    assert re.match("amb$|blu$|brn$|gry$|grn$|hzl$|oth$", v)
                elif k == "pid":
                    assert v.isnumeric()
                    assert len(v) == 9
            return True
        except:
            return False


    def part1(self):
        return len(self.get_passports_has_all_fields())


    def part2(self):
        passports = self.get_passports_has_all_fields()
        sol = 0
        for passport in passports:
            if self.validate_passport(passport):
                sol += 1
        return sol
