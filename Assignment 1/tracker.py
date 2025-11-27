# Author: Priyanshu Pandey
# Date: 9 November 2025
# Assignment Title: Daily Calorie Tracker CLI
# Course: Programming for Problem Solving using Python

import datetime

# Introduction
print("\nDaily Calorie Tracker")
print("Let's track your meals and calories today!\n")

# Input
meal_names = []
meal_calories = []

while True:
    try:
        total_meals = int(input("How many meals or snacks did you have today? "))
        if total_meals < 1:
            print("Enter at least 1 meal.")
            continue
        break
    except ValueError:
        print("Enter a valid number.")

for i in range(total_meals):
    print(f"\nMeal #{i+1}")
    name = input("Meal name (e.g., Breakfast, Lunch): ")
    meal_names.append(name)

    while True:
        try:
            cal = float(input(f"Calories for {name}: "))
            if cal <= 0:
                print("Calories should be more than 0.")
                continue
            meal_calories.append(cal)
            break
        except ValueError:
            print("Enter a number.")

# Calculations
total_calories = sum(meal_calories)
average_calories = total_calories / total_meals

# Daily Limit
while True:
    try:
        daily_limit = float(input("\nEnter your daily calorie limit: "))
        if daily_limit <= 0:
            print("Limit must be more than 0.")
            continue
        break
    except ValueError:
        print("Enter a valid number.")

# Status
print("\nCalorie Status")
if total_calories > daily_limit:
    print(f"You went over your limit of {daily_limit:.0f} by {total_calories - daily_limit:.0f} calories.")
elif total_calories == daily_limit:
    print(f"You hit your daily limit exactly: {daily_limit:.0f} calories.")
else:
    print(f"You're within your limit. You can still have {daily_limit - total_calories:.0f} calories.")

# Summary
print("\n" + "="*50)
print("DAILY CALORIE SUMMARY")
print("="*50)
print("Date & Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Table header
print("\n{:<25} {:>10}".format("Meal Name", "Calories"))
print("-"*36)

# Table rows
for name, cal in zip(meal_names, meal_calories):
    print("{:<25} {:>10.2f}".format(name, cal))

print("-"*36)
print("{:<25} {:>10.2f}".format("TOTAL", total_calories))
print("{:<25} {:>10.2f}".format("AVERAGE", average_calories))
print("="*50)

# Save Report
save = input("\nDo you want to save this report? (y/n): ").lower()

if save == 'y':
    filename = "calorie_log.txt"
    try:
        with open(filename, "a") as f:
            f.write("\n" + "="*50 + "\n")
            f.write("DAILY CALORIE TRACKER LOG\n")
            f.write(f"Date & Time: {datetime.datetime.now()}\n")
            f.write(f"Daily Limit: {daily_limit:.2f}\n\n")
            f.write("{:<25} {:>10}\n".format("Meal Name", "Calories"))
            f.write("-"*36 + "\n")
            for name, cal in zip(meal_names, meal_calories):
                f.write("{:<25} {:>10.2f}\n".format(name, cal))
            f.write("-"*36 + "\n")
            f.write("{:<25} {:>10.2f}\n".format("TOTAL", total_calories))
            f.write("{:<25} {:>10.2f}\n".format("AVERAGE", average_calories))
            if total_calories > daily_limit:
                f.write("Status: OVER LIMIT\n")
            elif total_calories == daily_limit:
                f.write("Status: EXACT LIMIT\n")
            else:
                f.write("Status: WITHIN LIMIT\n")
            f.write("="*50 + "\n")
        print(f"Report saved in '{filename}'.")
    except IOError:
        print("Could not save the report.")
else:
    print("Report not saved.")

print("\nThanks for using the tracker! Stay healthy :)")
