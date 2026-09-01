import pandas as pd
df.sort_index()                    # sort by row index
df.sort_index(axis=1)              # sort by column names
df.sort_index(ascending=False)

df.sort_values("age")                          # sort by column value
df.sort_values("age", ascending=False)
df.sort_values(["age", "name"])                 # multi-column sort
df.sort_values("age", kind="mergesort")          # choose sort algorithm: quicksort (default), mergesort, heapsort
# mergesort is the only STABLE option -- use it when 