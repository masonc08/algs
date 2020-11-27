class GCD:
    """
    Logarithmic runtime going down
    """
    def get(self, a, b):
        while b:
            a, b = b, a%b
        return a


    """
    Linear runtime going down
    """
    # def get(self, a, b):
    #     i = min(a, b)
    #     while i > 0:
    #         if a%i == b%i == 0:
    #             return i
    #         i -= 1
    #     return 1


f = GCD().get
assert f(3, 6) == 3
assert f(2, 2) == 2
assert f(12, 16) == 4
