import random

number_of_attempts = 3
while number_of_attempts:
    user_input = int(input("Enter any number from 1 to 10: "))
    random_number = random.randint(1, 10)
    if user_input == random_number:
        print("You won!")
        break
    number_of_attempts -= 1
    if number_of_attempts > 0:
        print("Try again!")
    else:
        print("You lose!")
