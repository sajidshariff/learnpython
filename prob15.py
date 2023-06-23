# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:

values = input("Enter a list of comma seperated values: ")
list_of_values = values.split(",")
print(list_of_values)
tuple_of_values = tuple(list_of_values)
print(tuple_of_values)