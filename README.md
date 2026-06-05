weather-data-analyzer ☁️

i made fake weather data and then analyzed it like it was real. no regrets.


what even is this

so i generated 365 days of completely made up weather data (temperature, humidity, rainfall) and then used pandas and matplotlib to analyze it like a serious data scientist. i am not a serious data scientist. i am a student who was curious.

there are 4 files. each one does a different thing and collectively they make me feel like i know what i'm doing.


the files explained

weather_csv.py — this is where the chaos begins. generates a full year of fake weather data and dumps it into a csv file. temperature, humidity, rainfall — all randomized. run this first or nothing else works.

data.py — loads the csv and immediately starts asking questions. how many rows? what's the shape? give me stats. basically the "so what do we have here" file.

quiry.py — gets nosy. hottest day? coldest day? how much did it rain each month? which days actually had rain? this file is investigating the data like it owes it money.

charts.py — the fun one. draws three charts:


a line chart of temperature across the whole year 🌡️

a bar chart of rainfall per month 🌧️

a scatter plot of temperature vs humidity 🟢


also has a cheat sheet of every chart type at the bottom because i kept forgetting the syntax. you're welcome past me.


how to run

install the libraries first:

bashpip install pandas matplotlib

then run in this order:

bashpython weather_csv.py   # makes the data

python data.py          # explores it

python quiry.py         # questions it

python charts.py        # draws pretty things

⚠️ heads up — charts.py and others have a hardcoded path from my laptop (C:\Users\User\Desktop\...). change it to wherever you put the files or just move everything to the same folder and use "weather.csv" directly.


what i actually learned from this


pandas is insane in a good way. .groupby().sum() does so much work in one line it feels illegal

pd.to_datetime() converts boring text dates into real dates you can actually do math with

scatter plots with 365 dots look really cool with alpha=0.3 (transparency) so they don't all blob together

making fake data and then analyzing it is genuinely a fun way to practice. 10/10 would recommend

