import pandas as pd
import numpy as np

# 5.1 Introduction to pandas Data Structures
## Series
obj = pd.Series([4, 7, -5, 3])
print(obj)        # a sequence of valuse and an associated array of index
print(obj.values)
print(obj.index)

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2['d'] = 6
print(obj2[['c', 'a', 'd']])

print(obj2[obj2 > 0])               # [6, 7, 3]
print(obj2 * 2)
print(np.exp(obj2))

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)       # Choose only the ones that match
pd.isnull(obj4)
"""
California     True
Ohio           False
Oregon         False
Texas          False
dtype: bool
"""

print(obj3 + obj4)
obj4.name = 'population'
obj4.index.name = 'state'

## DataFrame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
print(frame.head())       # The head method selects only the first five rows
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop'])
frame3 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame3['state'])
print(frame3.year)
print(frame3.loc['three'])
frame3['dept'] = 16.5
frame3['debt'] = np.arange(6.)
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame3['debt'] = val          #  its labels will be realigned exactly to the DataFrame’s index, inserting missing values in any holes
frame3['eastern'] = frame2.state == 'Ohio'   # Add a new column
print(frame3.columns)
del frame3['eastern']
print(frame3.columns)

pop = {'Nevada': {2001:2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame4 = pd.DataFrame(pop)
"""
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   3.6
"""
frame4.T
"""
        2000  2001  2002
Nevada   NaN   2.4   2.9
Ohio     1.5   1.7   3.6
"""
frame4 = pd.DataFrame(pop, index=[2001, 2002, 2003])
frame4.index.name = 'year'; frame4.columns.name = 'state'
frame4.values
"""
array([[ nan,  1.5],
       [ 2.4,  1.7],
       [ 2.9,  3.6]])
"""

## Index Objects
obj = pd.Series(range(3), index=['a', 'b', 'c'])
print(obj.index)         # ['a', 'b', 'c']
print(obj.index[1:])     # ['b', 'c']       # It's immutable
