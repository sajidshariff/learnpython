# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
'''
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
'''
import math

c = 50
h = 30
csvalues = input("Enter comma separated numbers: ")
values = csvalues.split(",")
# iterations = len(values)
final_values_list = []

def calculate_q(num):
    q = int(math.sqrt((2*c*int(num)/h)))
    final_values_list.append(q)


for value in values:
    calculate_q(value)
print(final_values_list)