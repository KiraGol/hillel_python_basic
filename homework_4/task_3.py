the_number_a = int(input("Enter A: "))
the_number_b = int(input("Enter B: "))
if the_number_a < the_number_b:
    for i in range(the_number_a, the_number_b + 1, 1):
        print(i)
else:
    for i in range(the_number_a, the_number_b - 1, -1):
        print(i)
