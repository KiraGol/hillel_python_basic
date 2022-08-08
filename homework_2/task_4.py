year_number = int(input("Enter the number of the year to be checked: "))
if year_number % 4 == 0 and year_number % 100 != 0 or year_number % 100 == 0:
    print("YES")
else:
    print("NO")