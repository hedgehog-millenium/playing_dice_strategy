import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from decisions import Decisions as dc


def get_true_perc(Y1):
    cols = ['my_score', 'max_score']
    df = pd.DataFrame(Y1, columns=cols)
    df['is_beast'] = df['my_score'] == df['max_score']
    vc = df['is_beast'].value_counts()
    true_percentage = vc[True] / (vc[True] + vc[False]) * 100
    return true_percentage


attempt_count = 10000
X = np.random.randint(1, 7, (attempt_count, 4))
strategies = np.array([
    [4, 3, 2],
    [5, 4, 3],
    [3, 3, 3],
    [4, 4, 4],
    [5, 5, 5],
    [6, 6, 6],
    [5, 5, 4]
])

all_results = []
for str in strategies:
    Y = get_true_perc(dc.get_value(X, str))
    all_results.append(Y)
    print('True percentage {} : {}%'.format(str, Y))

str_len = len(strategies)
plt.plot(range(str_len ),all_results)
plt.plot(range(str_len ),all_results,'ro')

x_ticks = strategies
plt.xticks(range(str_len ), x_ticks)
plt.title('Decision Efficiency')
plt.xlabel('Input data')
plt.ylabel('True Percentage %')
plt.show()

plt.bar(range(str_len ),all_results)
plt.show()
