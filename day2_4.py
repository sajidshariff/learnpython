# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program
list_of_values = []
csvalues = input("Enter a list of cs values: ")
values = csvalues.split(",")
lenght_of_values = len(values)
for num in values:
    list_of_values.append(int(num))
tuple_of_values = tuple(list_of_values)
print(list_of_values)
print(tuple_of_values)