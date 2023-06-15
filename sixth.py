# Program that calculates the factorial of a given number using a for loop
def fact(n):
    product=1
    for i in range(1,n+1):
        product=product*i



x=int(input())
# fact(5) = ((((5*4)*3)*2)*1)