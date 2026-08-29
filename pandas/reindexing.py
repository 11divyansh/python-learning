df1 = pd.DataFrame({"a": [1,2,3]}, index=[0,1,2])
df2 = pd.DataFrame({"a": [10,20]}, index=[1,2])

df2 = df2.reindex(df1.index)     # align df2's index to match df1's

s = pd.Series([1,2,3], index=[0,2,4])
s.reindex(range(6), method="ffill")   # forward-fill missing new index positions
s.reindex(range(6), method="bfill")   # backward-fill

s.reindex(range(6), method="ffill", limit=1)   # only fill 1 step forward, rest stay NaN

df.rename(columns={"a": "column_a"}, inplace=True)
df.rename(index={0: "row_zero"}, inplace=True)