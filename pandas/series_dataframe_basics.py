import pandas as pd
import numpy as np

pd.__version__     # check installed version

s = pd.Series([10, 20, 30])
print(s)

df = pd.DataFrame({
    "name": ["John", "Alice", "Bob"],
    "age": [20, 22, 19]
})
print(df)