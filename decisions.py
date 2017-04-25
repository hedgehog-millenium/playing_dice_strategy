import numpy as np


class Decisions:
    @classmethod
    def get_value(cls, x, step_breakers):
        rows, columns = x.shape
        steps = len(step_breakers)
        if steps >= columns:
            raise ValueError("Steps count are more or equal to columns in dataset")

        y = np.zeros(shape=(rows, 2))
        for i in range(rows):
            y[i, 1] = max(x[i])
            y[i, 0] = x[i, columns-1]
            for step in range(steps):
                if x[i, step] > step_breakers[step]:
                    y[i, 0] = x[i, step]
                    break
        return y