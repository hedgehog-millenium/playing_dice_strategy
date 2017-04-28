import math
f = math.factorial

class mystatistics:

    @classmethod
    def combinations(cls, c, r):
        return f(c)//f(r)//f(c-r)

    @classmethod
    def permutations(cls, c, r):
        return f(c)//f(c-r)