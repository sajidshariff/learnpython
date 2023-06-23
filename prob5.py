# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

def sum_of_nums(n1, n2, n3):
    sum_of_3_nums = sum([n1, n2, n3])
    if(n1 == n2) and (n2 == n3):
        print(3*sum_of_3_nums)
    else:
        print(sum_of_3_nums)

sum_of_nums(3, 3, 3)