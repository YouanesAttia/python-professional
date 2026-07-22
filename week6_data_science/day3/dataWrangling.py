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


# 8.2 Combining and Merging Datasets
## Database-Style DataFrame Joins
#### Many-to-One combination
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
pd.merge(df1, df2, on='key')
########  If that information is not specified, merge uses the overlapping column names as the keys
"""
   data1 key  data2
0      0   b      1
1      1   b      1
2      6   b      1
3      2   a      0
4      4   a      0
5      5   a      0
"""

df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})

pd.merge(df3, df4, left_on='lkey', right_on='rkey')    # Do inner Join; only couples allowed
"""
   data1 lkey  data2 rkey
0      0    b      1    b
1      1    b      1    b
2      6    b      1    b
3      2    a      0    a
4      4    a      0    a
5      5    a      0    a
"""
pd.merge(df1, df2, how='outer')           # Outer Join: takes the union of the keys
"""
   data1 key  data2
0    0.0   b    1.0
1    1.0   b    1.0
2    6.0   b    1.0
3    2.0   a    0.0
4    4.0   a    0.0
5    5.0   a    0.0
6    3.0   c    NaN
7    NaN   d    2.0
"""
pd.merge(df1, df2, how='left')           # Use all key combinations found in the left table

#### Many-to-Many combination
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': range(5)})
pd.merge(df1, df2, on='key', how='left')
"""
    data1 key  data2
0       0   b    1.0
1       0   b    3.0
2       1   b    1.0
3       1   b    3.0
4       2   a    0.0
5       2   a    2.0
6       3   c    NaN
7       4   a    0.0
8       4   a    2.0
9       5   b    1.0
10      5   b    3.0
"""

pd.merge(df1, df2, how='inner')
"""
   data1 key  data2
0      0   b      1
1      0   b      3
2      1   b      1
3      1   b      3
4      5   b      1
5      5   b      3
6      2   a      0
7      2   a      2
8      4   a      0
9      4   a      2
"""

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})

right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})

pd.merge(left, right, on=['key1', 'key2'], how='outer')

"""
  key1 key2  lval  rval
0  foo  one   1.0   4.0
1  foo  one   1.0   5.0
2  foo  two   2.0   NaN
3  bar  one   3.0   6.0
4  bar  two   NaN   7.0
"""

pd.merge(left, right, on='key1', suffixes=('_left', '_right'))

## Merging on Index
left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                      'value': range(6)})

right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
pd.merge(left1, right1, left_on='key', right_index=True)
"""
  key  value  group_val
0   a      0        3.5
2   a      2        3.5
3   a      3        3.5
1   b      1        7.0
4   b      4        7.0
"""

lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio',
                               'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})

righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio',
                              'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])

pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
"""
   data    key1  key2  event1  event2
0   0.0    Ohio  2000       4       5
0   0.0    Ohio  2000       6       7
1   1.0    Ohio  2001       8       9
2   2.0    Ohio  2002      10      11
3   3.0  Nevada  2001       0       1
"""

left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=['a', 'c', 'e'],
                     columns=['Ohio', 'Nevada'])

right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=['b', 'c', 'd', 'e'],
                      columns=['Missouri', 'Alabama'])

left2.join(right2, how='outer')
"""
   Ohio  Nevada  Missouri  Alabama
a   1.0     2.0       NaN      NaN
b   NaN     NaN       7.0      8.0
c   3.0     4.0       9.0     10.0
d   NaN     NaN      11.0     12.0
e   5.0     6.0      13.0     14.0
"""

left1.join(right1, on='key')
"""
  key  value  group_val
0   a      0        3.5
1   b      1        7.0
2   a      2        3.5
3   a      3        3.5
4   b      4        7.0
5   c      5        NaN
"""

## Concatenating Along an Axis
arr = np.arange(12).reshape((3, 4))
np.concatenate([arr, arr], axis=1)
"""
[[ 0,  1,  2,  3,  0,  1,  2,  3],
[ 4,  5,  6,  7,  4,  5,  6,  7],
[ 8,  9, 10, 11,  8,  9, 10, 11]]
"""
np.concatenate([arr, arr], axis=0)

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
pd.concat([s1, s2, s3])
"""
a    0
b    1
c    2
d    3
e    4
f    5
g    6
"""

pd.concat([s1, s2, s3], axis=1)     # Outer Join by default
"""
    0     1    2
a  0.0  NaN  NaN
b  1.0  NaN  NaN
c  NaN  2.0  NaN
d  NaN  3.0  NaN
e  NaN  4.0  NaN
f  NaN  NaN  5.0
g  NaN  NaN  6.0
"""
s4 = pd.concat([s1, s3])
pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])
"""
     0    1
a  0.0  0.0
c  NaN  NaN
b  1.0  1.0
e  NaN  NaN
"""

result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
"""
one    a    0
       b    1
two    a    0
       b    1
three  f    5
       g    6
"""

result.unstack()
"""
         a    b    f    g
one    0.0  1.0  NaN  NaN
two    0.0  1.0  NaN  NaN
three  NaN  NaN  5.0  6.0
"""

## Combining Data with Overlap
a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])

b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])

b[-1] = np.nan
np.where(pd.isnull(a), b, a)         # array([ 0. ,  2.5,  2. ,  3.5,  4.5,  nan])

b[:-2].combine_first(a[2:])
"""
a    NaN
b    4.5
c    3.0
d    2.0
e    1.0
f    0.0
"""

df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],
                    'b': [np.nan, 2., np.nan, 6.],
                    'c': range(2, 18, 4)})

df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],
                    'b': [np.nan, 3., 4., 6., 8.]})

df1.combine_first(df2)
"""
     a    b     c
0  1.0  NaN   2.0
1  4.0  2.0   6.0
2  5.0  4.0  10.0
3  3.0  6.0  14.0
4  7.0  8.0   NaN
"""
# combine_first = "Take everything from the left. Fill its missing values from the right. If the right has extra index labels, append them too."

# 8.3 Reshaping and Pivoting
## Reshaping with Hierarchical Indexing
data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'], name='number'))

result = data.stack()  # pivots the columns into the rows, producing a Series:
"""
state     number
Ohio      one       0
          two       1
          three     2
Colorado  one       3
          two       4
          three     5
"""
result.unstack()        # By default the innermost level is unstacked
"""
number    one  two  three
state                    
Ohio        0    1      2
Colorado    3    4      5
"""

result.unstack(0)
result.unstack('state')
"""
state   Ohio  Colorado
number                
one        0         3
two        1         4
three      2         5
"""

s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])
data2.unstack()
"""
       a    b    c    d    e
one  0.0  1.0  2.0  3.0  NaN
two  NaN  NaN  4.0  5.0  6.0
"""

data2.unstack().stack(dropna= False)       # Stacking filters out missing data by default

df = pd.DataFrame({'left': result, 'right': result + 5},
                  columns=pd.Index(['left', 'right'], name='side'))

"""
side             left  right
state    number             
Ohio     one        0      5
         two        1      6
         three      2      7
Colorado one        3      8
         two        4      9
         three      5     10
"""

## Pivoting “Long” to “Wide” Format
raw_data = {
    'year': [1959, 1959, 1959, 1959],
    'quarter': [1, 2, 3, 4],
    'realgdp': [2710.3, 2778.8, 2775.4, 2785.2],
    'infl': [0.00, 2.34, 2.74, 0.27],
    'unemp': [5.8, 5.1, 5.3, 5.6]
}
df = pd.DataFrame(raw_data)
print("--- 1. RAW DATA (WIDE FORMAT) ---")
print(df)
# PURPOSE: Data is "Wide" (each variable has its own column). 
# Time is split across two columns (year/quarter).


# --- STEP 1: CREATE A SINGLE TIME INDEX ---
periods = pd.PeriodIndex(year=df.year, quarter=df.quarter, name='date')
df.index = periods.to_timestamp('D', 'end') 
print("\n--- 2. AFTER SETTING DATE INDEX ---")
print(df)
# PURPOSE: Combine year/quarter into a single recognizable Date.
# 'end' ensures the date is the last day of the quarter (e.g., 1959-03-31).


# --- STEP 2: FILTER COLUMNS ---
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
df = df.reindex(columns=columns)
print("\n--- 3. AFTER FILTERING COLUMNS ---")
print(df)
# PURPOSE: Remove unnecessary columns. 
# We also name the column axis 'item' to prepare for the stack.


# --- STEP 3: THE "STACK" (TRANSFORM TO LONG) ---
# We chain three things here:
# A) .stack() -> Moves column names into the rows
# B) .reset_index() -> Turns the index levels back into normal columns
# C) .rename() -> Fixes the name of the column containing the actual numbers
ldata = df.stack().reset_index().rename(columns={0: 'value'})

print("\n--- 4. THE LONG FORMAT (ldata) ---")
print(ldata)
# PURPOSE: This is "Long Format." 
# Every row is now a single measurement. 
# Great for SQL databases and certain charting libraries (like Seaborn).


# --- STEP 4: PIVOTING (TRANSFORM BACK TO WIDE) ---
pivoted = ldata.pivot(index='date', columns='item', values='value')
print("\n--- 5. PIVOTED BACK TO WIDE ---")
print(pivoted)
# PURPOSE: This "undos" the stack. 
# It turns the unique values in 'item' back into individual column headers.


# --- STEP 5: PIVOTING MULTIPLE COLUMNS ---
# Let's add a fake "value2" column to show how pivot handles two data columns
ldata['value2'] = np.random.randn(len(ldata))
pivoted_multi = ldata.pivot(index='date', columns='item')

print("\n--- 6. PIVOTING WITH MULTIPLE VALUE COLUMNS ---")
print(pivoted_multi.head())
# PURPOSE: If you don't specify the 'values' argument in .pivot(), 
# Pandas creates "Hierarchical Columns" (Value and Value2 both get their own GDP/Infl/Unemp).


## Pivoting “Wide” to “Long” Format
df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})

melted = pd.melt(df, ['key'])
"""
Out[160]: 
   key variable  value
0  foo        A      1
1  bar        A      2
2  baz        A      3
3  foo        B      4
4  bar        B      5
5  baz        B      6
6  foo        C      7
7  bar        C      8
8  baz        C      9
"""

reshaped = melted.pivot('key', 'variable', 'value')
"""
variable  A  B  C
key              
bar       2  5  8
baz       3  6  9
foo       1  4  7
"""
reshaped.reset_index()
"""
variable  key  A  B  C
0         bar  2  5  8
1         baz  3  6  9
2         foo  1  4  7
"""
pd.melt(df, id_vars=['key'], value_vars=['A', 'B'])
"""
   key variable  value
0  foo        A      1
1  bar        A      2
2  baz        A      3
3  foo        B      4
4  bar        B      5
5  baz        B      6
"""