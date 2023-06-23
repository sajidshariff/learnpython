elf_with_max_calories = 0
current_elf = 0
total_calories = 0
max_calories = 0

total_calories_list = []

with open("calories.txt", "r") as fd:
    for line in fd:
        sanitized_line = line.splitlines()[0]
        if sanitized_line != "":
            calorie = int(sanitized_line)
            total_calories = total_calories + calorie
        else:
            # Done with an elf
            total_calories_list.append(total_calories)
            if total_calories > max_calories:
                max_calories = total_calories
                elf_with_max_calories = current_elf
            current_elf = current_elf + 1
total_calories_list.append(total_calories)
if total_calories > max_calories:
    max_calories = total_calories
    elf_with_max_calories = current_elf
current_elf = current_elf + 1
print("elf with max calories: ", current_elf)
print("max calories: ", max_calories)
print("list of total calories: ", total_calories_list)

#Make this more efficient (hint: use functions)