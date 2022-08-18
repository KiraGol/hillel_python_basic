my_list = [72, 64, 32, 34, 82, 29, 59, 89, 32, 10, 41, 6, 7]

for index in range(1, len(my_list) - 1):
    if my_list[index-1] < my_list[index] > my_list[index+1]:
        print(index)
