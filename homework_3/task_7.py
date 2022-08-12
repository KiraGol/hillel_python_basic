users_number = int(input("Enter the number: "))
counter = 1
factorial = 1
while counter <= users_number:
    factorial *= counter
    counter += 1
print(factorial)
