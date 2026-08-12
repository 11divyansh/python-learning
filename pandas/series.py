import pandas as pd
import numpy as np

pd.Series(data, index=None, dtype=None)
# Create an Empty Series python
s = pd.Series(dtype="float64")
print(s)   # Series([], dtype: float64)
# Create a Series from ndarray python
arr = np.array([1, 2, 3, 4])
s = pd.Series(arr)
# custom index:
s = pd.Series(arr, index=["a", "b", "c", "d"])

# Create a Series from dict python
d = {"a": 10, "b": 20, "c": 30}
s = pd.Series(d)
# dict keys become the index automatically

#Create a Series from Scalar python
s = pd.Series(5, index=["a", "b", "c"])
# a    5
# b    5
# c    5
# the scalar is repeated for every index value given
#Accessing Data from Series with Position python
s = pd.Series([10, 20, 30, 40])
s[0]        # 10 -- position-based
s[1:3]      # slice by position -> 20, 30

# Retrieve Data Using Label (Index) python
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
s["a"]              # 10
s[["a", "c"]]        # multiple labels -> Series with a and c