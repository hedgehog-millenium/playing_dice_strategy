from dice import dice
import itertools
import numpy as np
import pandas as pd



# comb = list(itertools.permutations([1,2,3,4,5,6], 4))
comb = dice.get_all_poss_comb(4)
df = pd.DataFrame(comb)


print('4 Atempts')
print('One number P: ', 1-(5/6)**4)
print('Two number P: ', 1-(4/6)**4)
print('Three number P: ', 1-(3/6)**4)

print('3 Atempts')
print('One number P: ', 1-(5/6)**3)
print('Two number P: ', 1-(4/6)**3)
print('Three number P: ', 1-(3/6)**3)

print('2 Atempts')
print('One number P: ', 1-(5/6)**2)
print('Two number P: ', 1-(4/6)**2)
print('Three number P: ', 1-(3/6)**2)





