import pandas as pd
s = pd.Series(["John", "alice", "  BOB  ", "eve123"])

s.str.lower()
s.str.upper()
s.str.strip()                    # remove leading/trailing whitespace
s.str.len()
s.str.replace("l", "L")
s.str.contains("a", case=False)
s.str.split("i")
s.str.startswith("J")
s.str.endswith("3")
s.str.cat(sep=", ")               # join all strings in the series
s.str.get_dummies()               # one-hot encode categorical text
s.str.extract(r"(\d+)")           # regex extraction into a new column