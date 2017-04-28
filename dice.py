from itertools import takewhile

import numpy as np
import itertools


class dice:
    @classmethod
    def get_all_poss_comb(cls, throw_count):
        # return itertools.permutations([1,2,3,4,5,6], throw_count)
        result = []
        nums = range(1, 7)
        for f in nums:
            for s in nums:
                for t in nums:
                    for fo in nums:
                        row = [f, s, t, fo]
                        result.append(row)
        return result





