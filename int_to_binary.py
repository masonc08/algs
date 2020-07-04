# Convert a base 10 integer into a string of binary
def int_to_binary(num):
    sol = []
    while num != 0:
        lsb = num % 2
        sol.append(str(lsb))
        num >>= 1
    return ''.join(reversed(sol))


print(int_to_binary(17))
