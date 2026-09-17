df.loc[0]                     # row with index label 0
df.loc[0:2]                    # label-based slice -- INCLUSIVE of both ends (unlike Python slicing!)
df.loc[0, "name"]              # specific cell
df.loc[df["age"] > 20, "name"] # boolean condition + column selection
15.2 .iloc[] — position-based selection
python
df.iloc[0]                # first row, by position
df.iloc[0:2]               # position slice -- EXCLUSIVE of end, like normal Python slicing
df.iloc[0, 1]               # row 0, column 1 by position
df.iloc[:, 0]                # all rows, first column
15.3 .ix() — removed entirely

python
df["age"]              # column access
df[["age", "name"]]     # multiple columns
df[0:2]                  # row slice (works but ambiguous style -- prefer .iloc/.loc explicitly)
df[df["age"] > 20]        # boolean filter