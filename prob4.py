# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

# n1 = float(input('Enter a number: '))

def abs_diff(num):
    diff = abs(17 - num)
    if num > 17:
        print(diff*2)
    else:
        print(diff)

abs_diff(88)
abs_diff(6)
abs_diff(-32)
