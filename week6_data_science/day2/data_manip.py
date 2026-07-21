import pandas as pd
import sys
import csv

# 6.1 Reading and Writing Data in Text Format
df = pd.read_csv('./example/ex1.csv')
df = pd.read_table('./example/ex1.csv', sep=',')
print(df)
df2 = pd.read_csv('./example/ex2.csv', header=None, names=['a', 'b', 'c', 'd', 'message'])

parsed = pd.read_csv('./example/csv_mindex.csv', index_col=['key1', 'key2'], skiprows=[0, 2, 3])
print(parsed)

result = pd.read_csv('example/ex5.csv')
print(pd.isnull(result))  # returns true for NA and NULL

sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
print(pd.read_csv('example/ex5.csv', na_values=sentinels))


## Reading Text Files in Pieces
pd.options.display.max_rows = 10
pd.read_csv('examples/ex6.csv', nrows=5)
chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

## Writing Data to Text Format
data = pd.read_csv('example/ex5.csv')
data.to_csv('example/out.csv')

data.to_csv(sys.stdout, sep='|', na_rep='NULL', index=False, header=False, columns=['a', 'b', 'c'])


## Working with Delimited Formats
f = open('example/ex7.csv')
reader = csv.reader(f)
for line in reader:
    print(line)

with open('examples/ex7.csv') as f:
    lines = list(csv.reader(f))
    header, values = lines[0], lines[1:]