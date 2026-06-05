import pandas as pd

df = pd.read_csv(r"weather.csv")

df["date"] = pd.to_datetime(df["date"])


hottest = df[df["temperature"] == df["temperature"].max()] #df[df["column"] == value] — filtering rows
print(hottest)

coldest = df[df["temperature"] == df["temperature"].min()]      
print(coldest)

df["month"] = df["date"].dt.month          #.dt.month — extracting month from a date

monthly_rain = df.groupby("month")["rainfall"].sum()        #groupby().sum() — total per group

print(monthly_rain)

montly_temp = df.groupby("month")["temperature"].mean()          #groupby().mean() — average per group
print(montly_temp)   


rainy_days = df[df['rainfall']>0]
print(len(rainy_days))
