import math

user_input = None
elements_to_operate = []
while user_input != 0:
    user_input = int(input("Enter the number: "))
    elements_to_operate.append(user_input)

count_of_numbers = len(elements_to_operate) - 1
print(f"Count of numbers: {count_of_numbers}")

sum_of_numbers = sum(elements_to_operate)
print(f"Sum of numbers: {sum_of_numbers}")

multiplication_of_numbers = math.prod(elements_to_operate)
print(f"Multiplication of numbers: {multiplication_of_numbers}")

average_value_from_elements = float(sum_of_numbers / count_of_numbers)
print(f"Average value from elements: {average_value_from_elements}")

max_number = max(elements_to_operate)
index_elem = elements_to_operate.index(max_number)
print(f"Max. number: {max_number}, serial number: {index_elem + 1}")

paired_elements = []
unpaired_elements = []
for elem in elements_to_operate:
    if elem % 2 == 0:
        paired_elements.append(elem)
    else:
        unpaired_elements.append(elem)
count_of_paired_elements = len(paired_elements)
count_of_unpaired_elements = len(unpaired_elements)
print(f"Count of paired elements: {count_of_paired_elements}")
print(f"Count of unpaired elements: {count_of_unpaired_elements}")

new_list = []
for elem in elements_to_operate:
    if elem != max_number:
        new_list.append(elem)
second_max_element = max(new_list)
print(f"Second max element: {second_max_element}")

new_list_2 = []
for elem in elements_to_operate:
    if elem == max_number:
        new_list_2.append(elem)
count_of_elements_equal_max_elem = len(new_list_2) - 1
print(f"Count of elements equal max elem: {count_of_elements_equal_max_elem}")
