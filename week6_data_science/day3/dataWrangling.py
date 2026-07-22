import pandas as pd
import numpy as np

# 8.1 Hierarchical Indexing
data = pd.Series(np.random.rand(9), index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],[1, 2, 3, 1, 3, 1, 2, 2, 3]])
"""
a  1   -0.204708
   2    0.478943
   3   -0.519439
b  1   -0.555730
   3    1.965781
c  1    1.393406
   2    0.092908
d  2    0.281746
   3    0.769023
"""

data['b']
"""
1   -0.555730
3    1.965781
"""
data['b':'c']           # From b to c (including c)
data.loc[:, 2]          # All 2s in the series

data.unstack()          # Rearrange into a dataframe
data.unstack().stack()  # Doesn't do anything
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                    index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                    columns=[['Ohio', 'Ohio', 'Colorado'],
                             ['Green', 'Red', 'Green']])

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
"""
state      Ohio     Colorado
color     Green Red    Green
key1 key2                   
a    1        0   1        2
     2        3   4        5
b    1        6   7        8
     2        9  10       11
"""

frame['Ohio']
frame.loc['a']
frame[0:2]             # Returns the first two rows (by position).


## Reordering and Sorting Levels
frame.swaplevel('key1', 'key2')       # index names not columns
"""
state      Ohio     Colorado
color     Green Red    Green
key2 key1                   
1    a        0   1        2
2    a        3   4        5
1    b        6   7        8
2    b        9  10       11
"""

frame.sort_index(level=1)
"""
state      Ohio     Colorado
color     Green Red    Green
key1 key2                   
a    1        0   1        2
b    1        6   7        8
a    2        3   4        5
b    2        9  10       11
"""

## Summary Statistics by Level
frame.sum(level='key2')
"""
state  Ohio     Colorado
color Green Red    Green
key2                    
1         6   8       10
2        12  14       16
"""

frame.sum(level='color', axis=1)


## Indexing with a DataFrame’s columns
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two',
                            'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})

"""
   a  b    c  d
0  0  7  one  0
1  1  6  one  1
2  2  5  one  2
3  3  4  two  0
4  4  3  two  1
5  5  2  two  2
6  6  1  two  3
"""
frame2 = frame.set_index(['c', 'd'], drop=True)  # drop is true by default, it deletes the columns we want to use as index
"""
       a  b
c   d      
one 0  0  7
    1  1  6
    2  2  5
two 0  3  4
    1  4  3
    2  5  2
    3  6  1
"""
frame2.reset_index()           # does the opposite of set_index
