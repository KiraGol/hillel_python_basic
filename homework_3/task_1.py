numbers_from_user = input("Enter a three-digit number: ")
sum_of_entered_numbers = sum([int(num) for num in numbers_from_user])
print(f"Sum of the entered numbers: {sum_of_entered_numbers}")
