# we use dataframe object to represent a tabular data rows/columns
import pandas as pd

df=pd.read_csv("D:/nyc_weather.csv")

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