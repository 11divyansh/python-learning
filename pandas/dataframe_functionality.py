import pandas as pd


df = pd.DataFrame({
    "name": ["Rahul", "Aman", "Priya", "Neha"],
    "age": [21, 22, 20, 23],
    "marks": [85, 92, 78, 88]
})

#transpose
print(df.T)# rows become columns, and columns becomem rows
#before
#    name   age   marks
#0   Rahul   21    85
#1   Aman    22    92
#2   Priya   20    78
#3   Neha    23    88

#after
#          0      1      2      3
#name    Rahul   Aman   Priya   Neha
#age       21     22     20     23
#marks     85     92     78     88

#df.axes
#this tells you the labels of both axes
#for our dataframe
#[
#    [0, 1, 2, 3],
#    ['name', 'age', 'marks']
#]
print(df.axes)
print(df.axes[0])
print(df.axes[1])

#df.dtypes
#this tells you the data type of each column
print(df.dtypes)
#name       str
#age      int64
#marks    int64
#dtype: object

#df.empty
# checks if the dataframe has zero elements
print(df.empty) #False

empty_df=pd.DataFrame()
print(empty_df.empty)#True

#df.ndim
# ndim means number of dimensions
print(df.ndim)#outputs 2 because DataFrame is 2D
print(df["age"].ndim)#gives 1 because Series is 1D

#df.shape
print(df.shape) # the format is (rows, columns)
rows, columns=df.shape

#df.size
#size gives you the total number of elements
print(df.size)# we have 4 rows x 3 columns = 12 elements

#df.values
#returns the underlying data as a NumPy array
print(df.values)#index and column name wont be included here

print(df.to_numpy()) #moders take

#df.head()
#head() gives you the first rows(by default 5)
print(df.head(2))# to get just 2 rows

#df.tail()
# gives last rows
print(df.tail(2))