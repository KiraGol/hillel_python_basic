number_from_user = float(input("Enter a floating point number: "))
integer_number = str(number_from_user).split(".")[0]
fraction = number_from_user - float(integer_number)
print(format(fraction, '.2f'))
first_number_after_point = str(number_from_user).split(".")[1][0]
print(f"First number after point: {first_number_after_point}")
