# Program that prints the multiplication table of a given number
num=int(input("Enter a number: "))
print(f'Multiplication table of {num}')
for i in range (1,11):
    print(f"{num} X {i} = ", num*i)