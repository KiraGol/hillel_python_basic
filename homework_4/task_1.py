x = int(input("Enter how many kilometers the athlete ran on the first day: "))
y = int(input("Enter how many kilometers the athlete ran in total: "))
day = 1
while y - x > 0:
    x = x + (x * 0.1)
    day += 1
print(f"Number of the day on which the athlete ran the total distance: {day}")