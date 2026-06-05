import pandas as pd

df = pd.read_csv(r"weather.csv")

df["date"] = pd.to_datetime(df["date"])
"""It took the date column which was plain text like "2026-01-01" and c
onverted it into a real date that pandas understands. Now we can do things like:
Filter by month
Sort by date
Extract just the month or day from the date"""

print(df.head()) #first 5 row of dataset

print(df.shape) #number of rows and columns

print(df.info()) #information about dataset

print(df.describe()) #statistical measures of dataset
