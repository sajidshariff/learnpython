# Calculate the total calories carried by the elf who carries the most calories
with open('input_day1.txt', 'r') as file:
    content = file.read()

max_calories = 0
current_elf_calories = 0
elf_with_max_calories = None
current_elf = 1

for line in content.split('\n'):
    if line.strip():
        calories = int(line)
        current_elf_calories += calories
    else:
        if current_elf_calories > max_calories:
            max_calories = current_elf_calories
            elf_with_max_calories = current_elf
            current_elf_calories = 0
            current_elf += 1

if current_elf_calories > max_calories:
    max_calories = current_elf_calories
    elf_with_max_calories = current_elf

print("Elf", elf_with_max_calories + 1, "carried the most Calories:", max_calories)