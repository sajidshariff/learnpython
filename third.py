# Function that takes two numbers as input and returns the maximum of the two.
def maximum(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
max_val=maximum(num1,num2)
print(max_val)
