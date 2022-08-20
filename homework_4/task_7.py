list_1 = [1, 8, 9, 6, 5, 4, 5, 8, 1]
list_2 = [6, 8, 9, 2, 3, 6]

set_1 = set(list_1)
set_2 = set(list_2)

duplicate_elements_of_both_lists = set_1.intersection(set_2)
print(f"Duplicate elements of both lists: {duplicate_elements_of_both_lists}")

elements_of_the_first_list_that_are_not_in_the_second = set_1.difference(set_2)
print(f"Elements of the first list that are not in the second: "
      f"{elements_of_the_first_list_that_are_not_in_the_second}")

elements_of_the_second_list_that_are_not_in_the_first = set_2.difference(set_1)
unique_elements_of_both_lists = \
    elements_of_the_first_list_that_are_not_in_the_second.union(
        elements_of_the_second_list_that_are_not_in_the_first)
print(f"Unique elements of both lists: {unique_elements_of_both_lists}")
