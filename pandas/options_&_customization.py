import pandas as pd
pd.get_option("display.max_rows")            # read a setting
pd.set_option("display.max_rows", 100)         # change how many rows print
pd.set_option("display.max_columns", 20)
pd.reset_option("display.max_rows")             # revert to default
pd.describe_option("display.max_rows")          # print docs for that setting

with pd.option_context("display.max_rows", 5):   # temporary setting, reverts after the block
    print(df)