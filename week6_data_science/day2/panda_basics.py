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


# 5.2 Essential Functionality
## Reindexing
#####  means to create a new object with the data conformed to a new index. 
obj = pd.Series([1, 2, -3, 4], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])      # This will only rearrange the inex keeping the values the same, 'e' will have no data
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj4 = obj3.reindex(range(6), method='ffill')

frame = pd.DataFrame(np.arange(9).reshape((3,3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
states = ['Texas', 'Utah', 'California']
frame3 = frame.reindex(columns=states)
# frame.loc[['a', 'b', 'c', 'd'], states]

## Dropping Entries from an Axis
obj =  pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop(['c', 'd'])
obj.drop('c', inplace=True)

frame = pd.DataFrame(np.arange(16).reshape((4,4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
frame1 = frame.drop(['Colorado', 'Ohio'])      # Will drop the 2 rows
frame2 = frame.drop('two', axis=1)
frame3 = frame.drop(['two', 'four'], axis='columns')


## Indexing, Selection, and Filtering
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
# obj['b'] == obj[1]
obj['b':'c']          # 1, 2  """"Different than normal python
obj['b':'c'] = 5      # 0, 5, 5, 3

frame = pd.DataFrame(np.arange(16).reshape((4,4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
frame[['three', 'one']]
frame[:2]        # First two rows
print(frame[1:2])    # First row only
frame[frame['three'] > 5]  # [2:] rows

#### Selection with loc and iloc
frame.loc['Colorado', ['two', 'three']]    # two   5    three   6
frame.iloc[2, [3, 0, 1]]    # Utah, forth first second places
frame.loc[:'Utah', 'two']    # will include Utah
frame.iloc[:2, 1]            # will not include Utah


## Arithmetic and Data Alignment
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1 + s2
"""
a       5.2
c       1.1
d       NaN
e       0.0
f       NaN
g       NaN
"""

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1 + df2
"""
            b   c     d   e
Colorado  NaN NaN   NaN NaN
Ohio      3.0 NaN   6.0 NaN
Oregon    NaN NaN   NaN NaN
Texas     9.0 NaN  12.0 NaN
Utah      NaN NaN   NaN NaN
"""

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df2.loc[1, 'b'] = np.nan
df1.add(df2, fill_value=0)
"""
      a     b     c     d     e
0   0.0   2.0   4.0   6.0   4.0
1   9.0   5.0  13.0  15.0   9.0
2  18.0  20.0  22.0  24.0  14.0
3  15.0  16.0  17.0  18.0  19.0
"""
1/df1 == df1.rdiv(1)

#### Operations between DataFrame and Series
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                    columns=list('bde'),
                    index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
frame - series
"""
          b    d    e
Utah    0.0  0.0  0.0
Ohio    3.0  3.0  3.0
Texas   6.0  6.0  6.0
Oregon  9.0  9.0  9.0
"""
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
frame + series2
"""
          b   d     e   f
Utah    0.0 NaN   3.0 NaN
Ohio    3.0 NaN   6.0 NaN
Texas   6.0 NaN   9.0 NaN
Oregon  9.0 NaN  12.0 NaN
"""
series3 = frame['d']
frame.sub(series3, axis='index')
"""
        b     d    e
Utah   -1.0  0.0  1.0
Ohio   -1.0  0.0  1.0
Texas  -1.0  0.0  1.0
Oregon -1.0  0.0  1.0
"""

## Function Application and Mapping
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(np.abs(frame))

f = lambda x: x.max() - x.min()
frame.apply(f)
"""
b    1.802165
d    1.684034
e    2.689627
"""
frame.apply(f, axis='columns')
"""
Utah      0.998382
Ohio      2.521511
Texas     0.676115
Oregon    2.542656
"""


## Sorting and Ranking
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())
frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
frame.sort_index()

# 5.3 Summarizing and Computing Descriptive Statistics
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
df.sum()
"""
one    9.25
two   -5.80
"""
df.sum(axis='columns')
"""
a    1.40
b    2.60
c    NaN
d   -0.55
"""
df.mean(axis='columns', skipna=False)
"""
a      NaN
b    1.300
c      NaN
d   -0.275
"""
df.idxmax()      # one    b          two    d
df.describe()    # producing multiple summary statistics in one shot

## Unique Values, Value Counts, and Membership
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()   # ['c', 'a', 'd', 'b']
obj.value_counts()
"""
c    3
a    3
b    2
d    1
"""
mask = obj.isin(['b', 'c'])        # performs a vectorized set membership check
obj[mask]                          # returns all of bs and cs
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
pd.Index(unique_vals).get_indexer(to_match)       # [0, 2, 1, 1, 0, 2]

data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                    'Qu2': [2, 3, 1, 2, 3],
                    'Qu3': [1, 5, 2, 4, 4]})
result = data.apply(pd.value_counts).fillna(0)
"""
   Qu1  Qu2  Qu3
1  1.0  1.0  1.0
2  0.0  2.0  1.0
3  2.0  2.0  0.0
4  2.0  0.0  2.0
5  0.0  0.0  1.0
"""