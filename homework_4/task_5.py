my_string = "123456789"
print(my_string)

third_character_of_the_string = my_string[2]
print(f"Third character of the string: {third_character_of_the_string}")

penultimate_character_of_the_string = my_string[7]
print(
    f"Penultimate character of the string: "
    f"{penultimate_character_of_the_string}")

first_five_characters_of_the_string = my_string[:5]
print(f"First five characters of the string: "
      f"{first_five_characters_of_the_string}")

entire_string_except_for_last_two_characters = my_string[:-2]
print(f"The entire string except for the last two characters: "
      f"{entire_string_except_for_last_two_characters}")

characters_with_paired_indices = my_string[::2]
print(f"Characters with paired indices: {characters_with_paired_indices}")

characters_with_unpaired_indices = my_string[1::2]
print(f"Characters with unpaired indices: {characters_with_unpaired_indices}")

characters_in_reverse_order = my_string[::-1]
print(f"Characters in reverse order: {characters_in_reverse_order}")

all_characters_through_one_in_reverse_order = my_string[::-1][::2]
print(f"All characters through one in reverse order:"
      f"{all_characters_through_one_in_reverse_order}")

string_length = len(my_string)
print(f"String length: {string_length}")