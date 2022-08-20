my_list = [72, 64, 32, 34, 82, 29, 59, 89, 32, 10, 41, 6, 7]

elements_greater_than_two_neighbors = []
for index in range(1, len(my_list) - 1):
    if my_list[index-1] < my_list[index] > my_list[index+1]:
        elements_greater_than_two_neighbors.append(index)

print(f"Elements greater than two neighbors: "
      f"{elements_greater_than_two_neighbors}")
print(f"Count of elements that are greater than two neighbors: "
      f"{len(elements_greater_than_two_neighbors)}")
