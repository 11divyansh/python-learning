# we use dataframe object to represent a tabular data rows/columns
import pandas as pd

# dataframe is a 2D table of data, basically like an excel spreadsheet or sql table
# pd.DataFrame(data, index=None, columns=None, dtype=None)

# rows->identified by index
# columns->identified by column names
# values->the actual data
df=pd.read_csv("D:/nyc_weather.csv")

#method 1 - use a dictionary(dict keys is column names and dict values is column data)
# each dict value becomes a column, all list must be of same size

#Index
# by default, pandas gives rows numerical indexs i.e. 0,1,2...
# You can specify your index
df = pd.DataFrame(
    {
        "Name": ["Rahul", "Aman", "Priya"],
        "Age": [21, 22, 20]
    },
    index=["student1", "student2", "student3"]
)

print(df)
#          Name  Age
# student1 Rahul   21
# student2 Aman    22
# student3 Priya   20

# you can access the rows using these labels
print(df.loc['student1'])

# Columns: you can control which columns you want and their order
data = {
    "Name": ["Rahul", "Aman", "Priya"],
    "Age": [21, 22, 20],
    "City": ["Delhi", "Mumbai", "Pune"]
}
df = pd.DataFrame(data,columns=["Name","City"])# gives only name and city
# columns=["City", "Name"] can be used to change the order of columns
# you can also specify a column that doesnt exist in your original dict
df=pd.DataFrame(data, columns=["Name","Age","Salary"])
#    Name  Age  Salary
# 0  Rahul   21     NaN
# 1  Aman    22     NaN
# 2  Priya   20     NaN
# NaN means missing value since "salary" was not present pandas fills it with NaN

#dtype
# it allows you to specify the data type
df = pd.DataFrame(
    {
        "Age": [20, 21, 22]
    },
    dtype="float" # tries to convert all the data of all columns into float
)
print(df)
#    Age
# 0  20.0
# 1  21.0
# 2  22.0
print("Type:",df.dtypes)#to check the type

# Method - 2 From a list
data = [
    ["Rahul", 21, "Delhi"],
    ["Aman", 22, "Mumbai"],
    ["Priya", 20, "Pune"]
]
df = pd.DataFrame(data)
print(df)
# here pandas doesnt know the column name so it will use numerical
# values for both row and column so you can just provide it with columns=["Name", "Age", "City"]

# Method - 3 Dataframe from a list of dict
print("Method 3")
data = [
    {"Name": "Rahul", "Age": 21},
    {"Name": "Aman", "Age": 22},
    {"Name": "Priya", "Age": 20, "city":"Delhi"} #missing keys becomes NaN
]
df = pd.DataFrame(data)
print(df)
#    Name  Age
# 0  Rahul   21
# 1   Aman   22
# 2  Priya   20
# here each dictionary represent one row

students = {
    "Name": ["Aman", "Riya", "Karan", "Neha"],
    "Math": [85, 92, 78, 88],
    "Science": [90, 89, 82, 95],
    "Age": [20, 21, 19, 20]
}
df = pd.DataFrame(students)
print(df)
print(df["Math"])

# Column selection
df = pd.DataFrame({
    "name": ["Rahul", "Aman", "Priya"],
    "age": [21, 22, 20],
    "marks": [85, 92, 78]
})
print(df)
print(df["name"])
# 0    Rahul
# 1     Aman
# 2    Priya
# Name: name, dtype: object
# This returns a series, a series is essentially one labeled column

print(df[["name", "age"]]) # give me multiple columns
#    name  age
# 0  Rahul   21
# 1   Aman   22
# 2  Priya   20
# this returns a dataframe, the outer [] is a DataFrame selection,
# while the inner[] creates a python list of col names

# Column addition
# ex:1 Boolean Column
df["passed"] = df["age"] > 18
# our age column is 21,22,20, pandas compares each value with 18
# so df["age"]>18 produces a Series then df["passed"] creates a new column
# pandas does it element by element you dont need a loop,
# this is called vectorized operation

# Ex:2 Mathematical Operatiton
df["age_plus_5"]=df["age"]+5

# Column deletion
# del
del df["age_plus_5"]

# pop()
passed_column=df.pop("passed")
# it returns the column and returns it
print("Popped column: ",passed_column)
# this is important when you want to delete the column but keep the removed data

# drop()
new_df=df.drop("name", axis=1)
# by default, drop() returns a new DataFrame
# it doesnt modify the original, while new_df contains age marks

# so pandas have 2 axes, axis=0->rows/index and axis=1->columns
# so df.drop("name", axis=1) means drop the column named "name"
# df.drop(columns="name"), you can use this also

#inplace=True
df.drop("name", axis=1, inplace=True) # means remove "name" directly from df

# Row Selection
df = pd.DataFrame({
    "name": ["Rahul", "Aman", "Priya"],
    "age": [21, 22, 20],
    "marks": [85, 92, 78]
})

print(df.loc[0]) #selection by label(returns the row whose index label is 0)
#name     Rahul
#age         21
#marks       85
#Name: 0, dtype: object


print(df.iloc[0]) # means selection by position
# currently /loc[0] and .iloc[0] gives same row because our numbering is from 0,1,2..

df.index = ["a", "b", "c"]
#   name   age
#a  Rahul   21
#b  Aman    22
#c  Priya   20

df.loc['a'] # for label
df.iloc[0] # for position

# Row Addition
new_row=pd.DataFrame([ # this creates a tiny dataframe
    {"name":"Zoe", "age":25}
])
df=pd.concat([df,new_row], ignore_index=True)
# combines the 2 dataframe vertically

#Row deletion
df=df.drop(0) # removes row whose index label is 0
#if you have
#    name  age
#0  Rahul   21
#1   Aman   22
#2  Priya   20

# then after df=df.drop(0), gives
#    name  age
#1   Aman   22
#2  Priya   20
# notice the index does not automatically becomes 0,1 it still stays 1, 2
# if you want fresh index then
df = df.reset_index(drop=True)



#create and empty dataframe
df = pd.DataFrame()
print(df)   # Empty DataFrame, Columns: [], Index: []

weather_data = {
    'day': ['1/1/2016', '1/2/2016', '1/3/2016', '1/4/2016', '1/5/2016'],
    'temperature': [38, 36, 40, 25, 20],
    'windspeed': [8, 7, 9, 6, 10],
    'event': ['Sunny', 'Rain', 'Sunny', 'Snow', 'Rain']
}
df =pd.DataFrame(weather_data) # to create a dataframe from map

print(df.shape)
rows, columns=df.shape 
print(f'rows:{rows}, columns:{columns}')
print(df.head(2))# print first few lines
print(df.tail(2)) #print last few lines 
print(df[2:5])#prints [2 to 5) rows

print(df.columns) #prints columns
print(df.day)
print(df.event)
print(df['event'])