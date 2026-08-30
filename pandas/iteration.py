import pandas as pd

for col in df:
    print(col)     # prints column names

# pandas < 2.0:
for col_name, series in df.items():   # use .items() now, iteritems() is gone
    print(col_name, series.values)

for index, row in df.iterrows():
    print(index, row["name"], row["age"])

#Performance note: iterrows() is slow (it boxes each row into a Series) and should be avoided for anything performance-sensitive — prefer vectorized operations (df["col"] * 2) or .apply() where possible. Use iterrows() only for small data or genuinely row-by-row logic that can't be vectorized.


for row in df.itertuples():
    print(row.name, row.age)     # faster than iterr