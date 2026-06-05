import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"weather.csv")

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
monthly_temp = df.groupby("month")["temperature"].mean()

#plt.figure(figsize=(12, 4)) — sets the size of the chart. 12 wide and 4 tall. Without this the chart would be tiny and squished.
plt.figure(figsize=(12, 4))

#plt.plot(df["date"], df["temperature"]) — draws a line chart. First argument is the x axis (date), second is the y axis (temperature).
#color="tomato" — makes the line red. You can use any color name like "blue", "green", "orange" or even hex codes like "#FF5733".
#linewidth=0.8 — makes the line thinner. Default is too thick for 365 data points and looks messy.
plt.plot(df["date"], df["temperature"], color="tomato", linewidth=0.8)
plt.title("Temperature across the year")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

monthly_rain = df.groupby("month")["rainfall"].sum()

plt.figure(figsize=(10, 5))
monthly_rain.plot(kind="bar", color="pink", edgecolor="black")
plt.title("Total Rainfall per Month")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.xticks(ticks=range(12), labels=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))

plt.scatter(df["temperature"], df["humidity"], color="green", alpha=0.3, s=10)
plt.title("Temperature vs Humidity")    
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.show()



"""
Bar chart
pythonplt.bar(x, y, color="blue", edgecolor="black", width=0.8)

Line chart
pythonplt.plot(x, y, color="red", linewidth=1.5, linestyle="--", marker="o")

linestyle — "-" solid, "--" dashed, ":" dotted
marker — "o" circle, "^" triangle, "s" square


Pie chart
pythonplt.pie(values, labels=labels, autopct="%1.1f%%", colors=["red","blue","green"])

autopct — shows percentage on each slice


Scatter plot
pythonplt.scatter(x, y, color="green", alpha=0.5, s=50)

alpha — transparency, 0 is invisible, 1 is solid
s — size of dots


Histogram
pythonplt.hist(values, bins=20, color="purple", edgecolor="black")

bins — how many bars to split data into


Box plot
pythondf.boxplot(column="rating", by="genre")

Common accessories for all charts
pythonplt.title("title here")
plt.xlabel("x label")
plt.ylabel("y label")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""
