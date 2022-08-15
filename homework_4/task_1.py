x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
day = 1
while y - x > 0:
    x = x + (x * 0.1)
    day += 1
print(day)