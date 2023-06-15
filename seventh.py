# Function that takes a list of numbers as input and returns the sum of all the even numbers in the list.


sum=0
numbers = [32, 54, 11, 76, 43, 72]
for num in numbers:
    if (num % 2) == 0:
        sum=sum+num

print(sum)