# main.py
from datetime import datetime

# Get current date and day of the week
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
day_of_week = now.strftime("%A")

# Print the date and day of the week
print(f"Date: {date_str}")
print(f"Day of the Week: {day_of_week}")