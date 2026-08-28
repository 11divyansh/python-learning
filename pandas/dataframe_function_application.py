import pandas as pd

def add_five(x):
    return x + 5

df.pipe(add_five)     # applies a function to the whole DataFrame

df.apply(np.sum, axis=0)     # apply down each column (default)
df.apply(np.sum, axis=1)     # apply across each row
df.apply(lambda row: row["a"] + row["b"], axis=1)

df.applymap(lambda x: x * 2)      # apply to every individual element (older pandas)
df["a"].map(lambda x: x * 2)      # Series equivalent
# Note: in pandas 2.1+, applymap is deprecated in favo