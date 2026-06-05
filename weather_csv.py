import csv
from datetime import date, timedelta
import random

random.seed(42)

FILENAME = "weather.csv"

start_date = date(2026, 1, 1)

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "temperature", "humidity", "rainfall"])

    for i in range(365):
        current_date = start_date + timedelta(days=i)
        temperature  = round(random.uniform(10, 40), 1)
        humidity     = random.randint(40, 100)
        rainfall     = round(random.uniform(0, 20), 1) if random.random() < 0.3 else 0.0
        writer.writerow([current_date, temperature, humidity, rainfall])

print("weather.csv created successfully!")