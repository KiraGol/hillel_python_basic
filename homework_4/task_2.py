import math
user_input = None
elements_to_operate = []
while user_input != 0:
    user_input = int(input("Enter the number: "))
    elements_to_operate.append(user_input)

count_of_numbers = len(elements_to_operate) - 1
print(count_of_numbers)

sum_of_numbers = sum(elements_to_operate)
print(sum_of_numbers)

multiplication_of_numbers = math.prod(elements_to_operate)
print(multiplication_of_numbers)

average_value_from_elements = sum_of_numbers/count_of_numbers
print(int(average_value_from_elements))

max_number = max(elements_to_operate)
index_elem = elements_to_operate.index(max_number)
print(max_number, index_elem + 1)

paired_elements = []
unpaired_elements = []
for elem in elements_to_operate:
    if elem % 2 == 0:
        paired_elements.append(elem)
    else:
        unpaired_elements.append(elem)
count_of_paired_elements = len(paired_elements)
count_of_unpaired_elements = len(unpaired_elements)
print(count_of_paired_elements)
print(count_of_unpaired_elements)

new_list = []
for elem in elements_to_operate:
    if elem != max_number:
        new_list.append(elem)
second_max_element = max(new_list)
print(second_max_element)

new_list_2 = []
for elem in elements_to_operate:
    if elem == max_number:
        new_list_2.append(elem)
count_of_elements_equal_max_elem = len(new_list_2) - 1
print(count_of_elements_equal_max_elem)









