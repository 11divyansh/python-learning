import pandas as pd

df = pd.DataFrame({
    "name": ["Rahul", "Aman", "Priya", "Neha"],
    "age": [21, 22, 20, 23],
    "marks": [85, 92, 78, 88]
})

#We want to answer questions like:
#What's the average age?
#What's the highest mark?
#What's the lowest mark?
#What's the standard deviation?
#How many values are present?
#That's what these functions do.

#df.sum()
print(df.sum())
#pandas performs the sum column-wise by default
#name     RahulAmanPriyaNeha
#age                       86
#marks                    343
#dtype: object

#strings get concatenated, if you only want numeric columns then:
print(df.sum(numeric_only=True))

#df.mean()
#mean=average
print(df.mean(numeric_only=True))

#df.median()
#median is the middle value after sorting
print(df.median(numeric_only=True))
#median is especially useful when your data has outliers

#df.mode()
#mode=the most frequently occuring value
df = pd.DataFrame({
    "age": [20, 21, 21, 22, 21]
})
print(df["age"].mode())
# there can be multiple modes so mode() can return a series containing multiple values

#df.std()
#this is standard deviation, which tells how spread out are the values from theri mean
#suppose class A: 49,50,51 so std is small, the values are close to average
#now class B:10,50,90, these spread out much more, so std is larger
df.std(numeric_only=True)

df.describe()                          # count, mean, std, min, quartiles, max for numeric cols
df.describe(include="all")             # include non-numeric columns too
df.describe(include=["object"])        # only object/string columns