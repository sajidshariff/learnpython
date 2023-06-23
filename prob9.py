# Write a Python program to count the number 4 in a given list.

four_counter = 0
random_list = [2, -4, 4, 4, 0, 5, 6, 7, 5, 3, 4, 4, 4]
list_len = len(random_list)
for value in random_list:
    if value == 4:
        four_counter += 1

print(four_counter)