import pandas as pd
import numpy as np
# pandas.DataFrame — signature basics python
pd.DataFrame(data, index=None, columns=None, dtype=None)

# Create DataFrame python
df = pd.DataFrame({"a": [1,2,3], "b": [4,5,6]})

#Create an Empty DataFrame python
df = pd.DataFrame()
print(df)   # Empty DataFrame, Columns: [], Index: []

# Create a DataFrame from Lists python
data = [1, 2, 3, 4]
df = pd.DataFrame(data, columns=["numbers"])

# list of lists (rows)
data = [["John", 20], ["Alice", 22]]
df = pd.DataFrame(data, columns=["name", "age"])

# Create a DataFrame from Dict of ndarrays / Lists python
data = {"name": ["John", "Alice"], "age": [20, 22]}
df = pd.DataFrame(data)
# each dict value becomes a column; all lists/arrays must be the same length

# Create a DataFrame from List of Dicts python
data = [
    {"name": "John", "age": 20},
    {"name": "Alice", "age": 22, "city": "Delhi"}   # missing keys become NaN
]
df = pd.DataFrame(data)
# Create a DataFrame from Dict of Series python
data = {
    "one": pd.Series([1, 2, 3], index=["a", "b", "c"]),
    "two": pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
}
df = pd.DataFrame(data)
# indexes are automatically aligned; mismatched labels get NaN

#Column Selection python
df["name"]           # single column -> Series
df[["name", "age"]]   # multiple columns -> DataFrame

#Column Addition
df["passed"] = df["age"] > 18
df["age_plus_5"] = df["age"] + 5

#Column Deletion
del df["age_plus_5"]
df.pop("passed")
df.drop("name", axis=1)               # returns a new DataFrame, doesn't modify in place
df.drop("name", axis=1, inplace=True) # modifies in place

#Row Selection, Addition, and Deletion

df.loc[0]                              # select row by label
df.iloc[0]                             # select row by position

new_row = pd.DataFrame([{"name": "Zoe", "age": 25}])
df = pd.concat([df, new_row], ignore_index=True)   # add a row (modern way -- .append() is removed)

df = df.drop(0) 

#DataFrame Basic Functionality
df = pd.DataFrame({"a": [1,2,3], "b": [4,5,6]})

df.T              # transpose
df.axes           # list of row/column labels
df.dtypes
df.empty          # True if no data
df.ndim           # number of dimensions
df.shape          # (rows, cols)
df.size           # total number of elements
df.values         # underlying NumPy array
df.head(2)
df.tail(2)