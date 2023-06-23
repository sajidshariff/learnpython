# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).

list_of_numbers = []
for num in range(2000,3201):
    if (num % 7) == 0 and (num % 5) != 0:
        list_of_numbers.append(num)
# print(list_of_numbers)
print(len(list_of_numbers))
        
