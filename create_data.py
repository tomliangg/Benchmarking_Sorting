import time
import pandas as pd
import numpy as np
from implementations import all_implementations

random_array = np.random.randint(1000, size=10000)
tmp_matrix= []

for i in range(50):
    tmp_list = []
    for sort in all_implementations:
        st = time.time()
        res = sort(random_array)
        en = time.time()
        tmp_list.append(en-st)
    tmp_matrix.append(tmp_list)

data = pd.DataFrame(tmp_matrix, columns=['qs1', 'qs2', 'qs3', 'qs4', 'qs5', 'merge1', 'partition_sort'])
data.to_csv('data.csv', index=False)

