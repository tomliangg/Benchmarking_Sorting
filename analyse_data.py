import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = pd.read_csv('data.csv')

qs1_data = data['qs1']
qs2_data = data['qs2']
qs3_data = data['qs3']
qs4_data = data['qs4']
qs5_data = data['qs5']
merge1_data = data['merge1']
partition_sort_data = data['partition_sort']

anova = stats.f_oneway(qs1_data, qs2_data, qs3_data, qs4_data, qs5_data, merge1_data, partition_sort_data)
print(anova.pvalue)
# ANOVA p-value is 9.9e-55 so definitely different means among different sorting algorithms

# it's time to do Post Hoc Analysis 
x_data = pd.DataFrame({'qs1':qs1_data, 'qs2':qs2_data, 'qs3':qs3_data, 'qs4':qs4_data, 'qs5':qs5_data, 'merge1':merge1_data, 'partition_sort':partition_sort_data})
x_melt = pd.melt(x_data)
posthoc = pairwise_tukeyhsd(
    x_melt['value'], x_melt['variable'],
    alpha=0.05)

print(posthoc)
# from the posthoc result table, we can tell that qs1 is the fastest
# take a look at the reject column, we know that these 4 pairs can't be distinguished:
"""
partition_sort      qs2 
partition_sort      qs3
qs2            qs3
qs4            qs5
"""

# use the plot to help us visualize the results 
fig = posthoc.plot_simultaneous()
fig.savefig('result_plot.png')


