
def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)

entered_number = int(input("Enter an integer to calculate it's factorial: "))
print(fact(entered_number))