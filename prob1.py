#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

def calculate_sort_of_sum(n):
    sum = n + (n * n) + (n * n * n)
    return(sum)

num = int(input("Please enter an integer: "))
cal = calculate_sort_of_sum(n)(num)
print(cal)