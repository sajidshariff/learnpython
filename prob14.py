# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

input_values = input(("Enter a list of comma-seperated values: "))
list_of_val = input_values.split(',')
tuple_of_val = tuple(list_of_val)
print(list_of_val)
print(tuple_of_val)