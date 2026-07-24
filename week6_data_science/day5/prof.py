import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('./examples/2015.csv')

profile = ProfileReport(df, title="EDA Report")
profile.to_file("report.html")