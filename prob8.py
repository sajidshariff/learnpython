# Write a Python program to test whether a number is within 100 of 1000 or 2000
''' 
def under_100(n):
    if num in range(900,1101):
        print(f'The number {num} is within 100 of 1000')
    elif num in range(1900,2101):
        print(f'The number {num} is within 100 of 2000')
    else:
        print('Number not in specified range.')

num = int(input('Enter a number: '))
under_100(num)
'''

def nearest_thousand(n):
    if (abs(1000 - n)) <= 100:
        print(f'The number {n} is near 1000')
    elif (abs(2000 - n)) <= 100:
        print(f'The number {n} is near 2000')
    else:
        print(f'The number {n} is neither close to 1000 nor 2000')

num = int(input('Enter a number: '))
nearest_thousand(num)